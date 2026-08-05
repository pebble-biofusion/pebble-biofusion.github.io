"""
Unified engine for the combined multiscale tutorial.

One self-contained module. The single neuron ladder:
    Hodgkin-Huxley (4 states: V,m,h,n)
        -> 3-state fast-m reduction (V,h,n with m = m_inf(V))
        -> 2-state reduction (V,n with h = a - b*n)
        -> discrete spike events {t_i}
    LIF (1 state + threshold) is used at the network scale.
The network / learning layer:
    short-term plasticity (Tsodyks-Markram) on feed-forward synapses,
    long-term plasticity (STDP) on recurrent synapses,
    and an image "learning task" (store & complete an 8x8 picture).

All ODEs are solved with the forward-Euler / exponential-decay schemes of
Appendix B (no external solver needed).
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import numpy as np

# =========================================================================== #
# PART A — SINGLE-NEURON MODELS
# =========================================================================== #
# ---- Hodgkin-Huxley rate functions (modern convention, V in mV, rest ~ -65) - #
def _alpha_n(V): return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))
def _beta_n(V):  return 0.125 * np.exp(-(V + 65.0) / 80.0)
def _alpha_m(V): return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))
def _beta_m(V):  return 4.0 * np.exp(-(V + 65.0) / 18.0)
def _alpha_h(V): return 0.07 * np.exp(-(V + 65.0) / 20.0)
def _beta_h(V):  return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))


def tau_m(V): return 1.0 / (_alpha_m(V) + _beta_m(V))
def tau_h(V): return 1.0 / (_alpha_h(V) + _beta_h(V))
def tau_n(V): return 1.0 / (_alpha_n(V) + _beta_n(V))
def m_inf(V): return _alpha_m(V) / (_alpha_m(V) + _beta_m(V))
def h_inf(V): return _alpha_h(V) / (_alpha_h(V) + _beta_h(V))
def n_inf(V): return _alpha_n(V) / (_alpha_n(V) + _beta_n(V))


def simulate_hh(I_amp=10.0, t_start=5.0, t_end=30.0, duration=50.0, dt=0.01,
                gNa=120.0, gK=36.0, gL=0.3):
    """Full 4-state Hodgkin-Huxley model, forward Euler. Current in uA/cm^2."""
    n = int(duration / dt)
    t = np.arange(n) * dt
    ENa, EK, EL, C = 50.0, -77.0, -54.4, 1.0
    V = np.full(n, -65.0); m = np.full(n, m_inf(-65.0))
    h = np.full(n, h_inf(-65.0)); n_ = np.full(n, n_inf(-65.0))
    I_ext = np.where((t >= t_start) & (t <= t_end), I_amp, 0.0)
    for i in range(1, n):
        am, bm = _alpha_m(V[i - 1]), _beta_m(V[i - 1])
        ah, bh = _alpha_h(V[i - 1]), _beta_h(V[i - 1])
        an, bn = _alpha_n(V[i - 1]), _beta_n(V[i - 1])
        m[i] = m[i - 1] + dt * (am * (1 - m[i - 1]) - bm * m[i - 1])
        h[i] = h[i - 1] + dt * (ah * (1 - h[i - 1]) - bh * h[i - 1])
        n_[i] = n_[i - 1] + dt * (an * (1 - n_[i - 1]) - bn * n_[i - 1])
        I_Na = gNa * m[i] ** 3 * h[i] * (V[i - 1] - ENa)
        I_K = gK * n_[i] ** 4 * (V[i - 1] - EK)
        I_L = gL * (V[i - 1] - EL)
        V[i] = V[i - 1] + dt * (I_ext[i] - I_Na - I_K - I_L) / C
    I_Na = gNa * m ** 3 * h * (V - ENa)
    I_K = gK * n_ ** 4 * (V - EK)
    return dict(t=t, V=V, m=m, h=h, n=n_, I_ext=I_ext, I_Na=I_Na, I_K=I_K)


def simulate_hh_three_variable(I_amp=10.0, t_start=5.0, t_end=6.0, duration=50.0,
                               dt=0.01, gNa=120.0, gK=36.0, gL=0.3):
    """3-state HH: m is replaced by m_inf(V) (timescale-separation reduction).
    State variables are (V, h, n)."""
    n = int(duration / dt)
    t = np.arange(n) * dt
    ENa, EK, EL, C = 50.0, -77.0, -54.4, 1.0
    V = np.full(n, -65.0)
    h = np.full(n, h_inf(-65.0)); n_ = np.full(n, n_inf(-65.0))
    I_ext = np.where((t >= t_start) & (t <= t_end), I_amp, 0.0)
    for i in range(1, n):
        ah, bh = _alpha_h(V[i - 1]), _beta_h(V[i - 1])
        an, bn = _alpha_n(V[i - 1]), _beta_n(V[i - 1])
        h[i] = h[i - 1] + dt * (ah * (1 - h[i - 1]) - bh * h[i - 1])
        n_[i] = n_[i - 1] + dt * (an * (1 - n_[i - 1]) - bn * n_[i - 1])
        m_i = m_inf(V[i - 1])
        I_Na = gNa * m_i ** 3 * h[i] * (V[i - 1] - ENa)
        I_K = gK * n_[i] ** 4 * (V[i - 1] - EK)
        I_L = gL * (V[i - 1] - EL)
        V[i] = V[i - 1] + dt * (I_ext[i] - I_Na - I_K - I_L) / C
    m = m_inf(V)
    I_Na = gNa * m ** 3 * h * (V - ENa)
    I_K = gK * n_ ** 4 * (V - EK)
    return dict(t=t, V=V, m=m, h=h, n=n_, I_ext=I_ext, I_Na=I_Na, I_K=I_K)


def fit_h_from_n(n_traj, h_traj):
    """Fit h ≈ a - b*n along a reference HH trajectory.
    Returns (a, b, R^2)."""
    coeffs = np.polyfit(n_traj, h_traj, 1)
    slope, intercept = float(coeffs[0]), float(coeffs[1])
    a, b = intercept, -slope
    h_pred = a - b * n_traj
    ss_res = np.sum((h_traj - h_pred) ** 2)
    ss_tot = np.sum((h_traj - np.mean(h_traj)) ** 2)
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return a, b, r_squared


def h_from_n(n, a, b):
    """Predicted sodium inactivation from potassium activation: h = a - b*n."""
    return a - b * n


def simulate_hh_two_variable(I_amp=10.0, t_start=5.0, t_end=6.0,
                             a_fit=0.97, b_fit=1.18, duration=50.0,
                             dt=0.01, gNa=120.0, gK=36.0, gL=0.3):
    """2-state HH: m = m_inf(V) AND h = a_fit - b_fit*n.
    State variables are (V, n) only."""
    n = int(duration / dt)
    t = np.arange(n) * dt
    ENa, EK, EL, C = 50.0, -77.0, -54.4, 1.0
    V = np.full(n, -65.0)
    n_ = np.full(n, n_inf(-65.0))
    I_ext = np.where((t >= t_start) & (t <= t_end), I_amp, 0.0)
    for i in range(1, n):
        an, bn = _alpha_n(V[i - 1]), _beta_n(V[i - 1])
        n_[i] = n_[i - 1] + dt * (an * (1 - n_[i - 1]) - bn * n_[i - 1])
        m_i = m_inf(V[i - 1])
        h_i = a_fit - b_fit * n_[i]
        I_Na = gNa * m_i ** 3 * h_i * (V[i - 1] - ENa)
        I_K = gK * n_[i] ** 4 * (V[i - 1] - EK)
        I_L = gL * (V[i - 1] - EL)
        V[i] = V[i - 1] + dt * (I_ext[i] - I_Na - I_K - I_L) / C
    m = m_inf(V)
    h = a_fit - b_fit * n_
    I_Na = gNa * m ** 3 * h * (V - ENa)
    I_K = gK * n_ ** 4 * (V - EK)
    return dict(t=t, V=V, m=m, h=h, n=n_, I_ext=I_ext, I_Na=I_Na, I_K=I_K)


def detect_spikes(t, V, threshold=0.0):
    """Times at which V crosses `threshold` upward (mV)."""
    V0 = V - threshold
    cross = np.where((V0[:-1] <= 0) & (V0[1:] > 0))[0]
    return t[cross]


# ---- FitzHugh-Nagumo (2-state phenomenological reduction) ------------------ #
def simulate_fhn(I_amp=0.5, t_start=5.0, t_end=60.0, duration=80.0, dt=0.05,
                 a=0.7, b=0.8, tau=12.5):
    """FitzHugh-Nagumo: u (excitation), w (recovery)."""
    n = int(duration / dt)
    t = np.arange(n) * dt
    u = np.full(n, -1.2); w = np.full(n, -0.6)
    I_ext = np.where((t >= t_start) & (t <= t_end), I_amp, 0.0)
    for i in range(1, n):
        u[i] = u[i - 1] + dt * (u[i - 1] - u[i - 1] ** 3 / 3.0 - w[i - 1] + I_ext[i])
        w[i] = w[i - 1] + dt * (u[i - 1] + a - b * w[i - 1]) / tau
    return dict(t=t, u=u, w=w, I_ext=I_ext)


# ---- Leaky integrate-and-fire (1 state + threshold) ------------------------ #
def simulate_lif(I_amp=23.0, t_start=30.0, t_end=170.0, duration=200.0, dt=0.1,
                 e_l=-70.0, v_th=-55.0, v_reset=-65.0, tau_m=20.0, t_ref=2.0):
    n = int(duration / dt)
    t = np.arange(n) * dt
    V = np.full(n, e_l)
    spikes, refr = [], 0.0
    I_ext = np.where((t >= t_start) & (t <= t_end), I_amp, 0.0)
    for i in range(1, n):
        if refr > 0:
            refr -= dt
            V[i] = v_reset
        else:
            V[i] = V[i - 1] + dt * (e_l - V[i - 1] + I_ext[i]) / tau_m
            if V[i] >= v_th:
                spikes.append(t[i]); V[i] = v_reset; refr = t_ref
    return dict(t=t, V=V, I_ext=I_ext, spikes=np.array(spikes))


# ---- Exponential synaptic kernel (event -> continuous current) ------------- #
def synaptic_trace(spike_times, tau_s=8.0, dt=0.1, duration=None, weight=1.0):
    """Exponential synaptic kernel driven by discrete spike events.

    Implements:  r <- r + weight at each spike;  r *= exp(-dt/tau_s) each step.
    Returns (t, r) arrays.
    """
    spike_times = np.asarray(spike_times, dtype=float)
    if duration is None:
        duration = (spike_times[-1] + 5 * tau_s) if spike_times.size else 100.0
    n = int(duration / dt)
    t = np.arange(n) * dt
    r = np.zeros(n)
    e_decay = np.exp(-dt / tau_s)
    k = 0
    for i in range(n):
        if i > 0:
            r[i] = r[i - 1] * e_decay
        while k < spike_times.size and spike_times[k] <= t[i]:
            r[i] += weight
            k += 1
    return t, r


# =========================================================================== #
# PART B — SYNAPSE: SHORT-TERM PLASTICITY (Tsodyks-Markram)
# =========================================================================== #
def tsodyks_markram_response(spike_times, U=0.45, tau_rec=750.0, tau_facil=50.0,
                             dt=0.1, t_max=None):
    """Released amount per spike (depressing vs facilitating regimes)."""
    spike_times = np.asarray(spike_times, dtype=float)
    if t_max is None:
        t_max = (spike_times[-1] + 5 * tau_rec) if spike_times.size else tau_rec
    n = int(t_max / dt) + 1
    u, x = U, 1.0
    e_rec = np.exp(-dt / tau_rec); e_fac = np.exp(-dt / tau_facil)
    amps, k = [], 0
    for step in range(n):
        t = step * dt
        while k < spike_times.size and spike_times[k] <= t:
            u = u + U * (1.0 - u); amps.append(u * x); x = x * (1.0 - u); k += 1
        u += -(u - U) * (1.0 - e_fac); x += (1.0 - x) * (1.0 - e_rec)
    return np.array(amps)


def feedforward_demo(rate=45.0, duration=1500.0, dt=0.1,
                     U=0.45, tau_rec=750.0, tau_facil=50.0, A=12.0,
                     e_l=-70.0, tau_m=20.0, tau_syn=15.0, seed=0):
    """Poisson input -> depressing synapse -> ONE output LIF (sub-threshold)."""
    n = int(duration / dt)
    rng = np.random.default_rng(seed)
    e_syn = np.exp(-dt / tau_syn); e_rec = np.exp(-dt / tau_rec); e_fac = np.exp(-dt / tau_facil)
    v_trace = np.full(n, e_l); i_syn = 0.0; v = e_l; u, x = U, 1.0
    in_spikes = []
    for s in range(n):
        i_syn *= e_syn
        u += -(u - U) * (1.0 - e_fac); x += (1.0 - x) * (1.0 - e_rec)
        if rng.random() < rate * dt / 1000.0:
            in_spikes.append(s * dt)
            u = u + U * (1.0 - u); i_syn += A * u * x; x = x * (1.0 - u)
        v += (e_l - v + i_syn) * (dt / tau_m); v_trace[s] = v
    return np.arange(n) * dt, v_trace, np.array(in_spikes)


# =========================================================================== #
# PART C — RECURRENT NETWORK WITH STDP (long-term plasticity)
# =========================================================================== #
@dataclass
class NetParams:
    n_e: int = 64
    dt: float = 1.0
    e_l: float = -70.0; v_th: float = -55.0; v_reset: float = -65.0
    tau_m: float = 20.0; tau_syn: float = 8.0; t_ref: float = 2.0
    w_max: float = 1.3; w_init: float = 0.0
    tau_inh: float = 10.0; g_inh: float = -1.1
    noise: float = 3.0
    stdp_tau: float = 20.0; stdp_a_plus: float = 0.035; stdp_a_minus: float = 0.028


class SpikingNetwork:
    def __init__(self, params: NetParams | None = None, seed: int = 0):
        self.p = params or NetParams()
        self.rng = np.random.default_rng(seed)
        p = self.p
        self.v = np.full(p.n_e, p.e_l); self.i_syn = np.zeros(p.n_e)
        self.inh = 0.0; self.ref = np.zeros(p.n_e)
        self.w = self.rng.uniform(0.0, p.w_init, size=(p.n_e, p.n_e))
        np.fill_diagonal(self.w, 0.0)
        self.x_pre = np.zeros(p.n_e); self.x_post = np.zeros(p.n_e)
        self._e_syn = np.exp(-p.dt / p.tau_syn); self._e_inh = np.exp(-p.dt / p.tau_inh)
        self._e_stdp = np.exp(-p.dt / p.stdp_tau)
        self.spikes = []; self._prev = np.array([], dtype=int)

    def step(self, t, i_ext=None, stdp_on=True):
        p = self.p
        if self._prev.size:
            j = self._prev
            self.i_syn += self.w[:, j].sum(axis=1)
            if stdp_on:
                self.w[:, j] -= p.stdp_a_minus * self.w[:, j] * self.x_post[:, None]
                self.x_pre[j] += 1.0
        self.i_syn *= self._e_syn
        self.x_pre *= self._e_stdp; self.x_post *= self._e_stdp; self.inh *= self._e_inh
        if i_ext is None:
            i_ext = 0.0
        noise = self.rng.normal(0.0, p.noise, p.n_e) if p.noise > 0 else 0.0
        active = self.ref <= 0
        dv = (p.e_l - self.v + self.i_syn + i_ext + noise + self.inh) * (p.dt / p.tau_m)
        self.v[active] += dv[active]
        self.ref -= p.dt
        sp = np.where((self.v >= p.v_th) & active)[0]
        if sp.size:
            self.v[sp] = p.v_reset; self.ref[sp] = p.t_ref
            self.inh += p.g_inh * sp.size / p.n_e
            if stdp_on:
                self.w[sp, :] += p.stdp_a_plus * (p.w_max - self.w[sp, :]) * self.x_pre[None, :]
                self.x_post[sp] += 1.0
            self.spikes.extend((t, int(i)) for i in sp)
        np.fill_diagonal(self.w, 0.0)
        self._prev = sp

    def soft_reset(self):
        p = self.p
        self.v[:] = p.e_l; self.i_syn[:] = 0.0; self.inh = 0.0; self.ref[:] = 0.0
        self.x_pre[:] = 0.0; self.x_post[:] = 0.0
        self._prev = np.array([], dtype=int)


# =========================================================================== #
# PART D — IMAGE LEARNING TASK (store & complete an 8x8 picture)
# =========================================================================== #
SHAPES = {
    "plus": [
        "........", "........", "...XX...", "...XX...",
        "XXXXXXXX", "XXXXXXXX", "...XX...", "...XX...",
    ],
    "ring": [
        "..XXXX..", ".XXXXXX.", "XX....XX", "XX....XX",
        "XX....XX", "XX....XX", ".XXXXXX.", "..XXXX..",
    ],
    "H": [
        "XX....XX", "XX....XX", "XX....XX", "XXXXXXXX",
        "XXXXXXXX", "XX....XX", "XX....XX", "XX....XX",
    ],
    "T": [
        "XXXXXXXX", "XXXXXXXX", "...XX...", "...XX...",
        "...XX...", "...XX...", "...XX...", "...XX...",
    ],
}


def shape_pixels(name):
    """Indices of the 'X' pixels in an 8x8 shape (row-major)."""
    rows = SHAPES[name]
    idx = []
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "X":
                idx.append(r * 8 + c)
    return np.array(idx)


def _default_params(n_e=64, **over):
    p = NetParams(n_e=n_e)
    for k, v in over.items():
        setattr(p, k, v)
    return p


def train_network(pattern, n_e=64, n_trials=45, drive=22.0, t_on=120.0, t_off=160.0,
                  seed=0, **param_over):
    """Learn a cell assembly for `pattern` (array of pixel indices). Returns a
    trained SpikingNetwork and the weight-growth history."""
    p = _default_params(n_e, **param_over)
    net = SpikingNetwork(p, seed=seed)
    dt = p.dt
    d = np.zeros(n_e); d[pattern] = drive
    whist = []
    for trial in range(n_trials):
        net.soft_reset()
        for s in range(int(t_on / dt)):
            net.step(trial * (t_on + t_off) + s * dt, i_ext=d, stdp_on=True)
            net.spikes.clear()
        for s in range(int(t_off / dt)):
            net.step(trial * (t_on + t_off) + t_on + s * dt, stdp_on=True)
            net.spikes.clear()
        idx = np.ix_(pattern, pattern)
        block = net.w[idx].copy(); np.fill_diagonal(block, 0)
        whist.append(block.sum() / (pattern.size * (pattern.size - 1)))
    return net, np.array(whist)


def probe_recall(net, pattern, cue, background=13.0, background_all=0.0, drive=22.0,
                 t_cue=60.0, t_run=260.0):
    """Recall probe: hold pattern sub-threshold, briefly drive `cue`, measure
    completion of the NON-cued pattern and false-positive rate on non-pattern
    neurons. Returns events + per-step image activity + metrics."""
    p = net.p
    dt = p.dt
    net.soft_reset()
    n_steps = int(t_run / dt)
    noncue = np.setdiff1d(pattern, cue)
    non_pattern = np.setdiff1d(np.arange(p.n_e), pattern)
    bg = np.full(p.n_e, background_all)
    bg[pattern] = background
    events = []
    image = np.zeros((n_steps, p.n_e))
    for s in range(n_steps):
        t = s * dt
        i_ext = bg.copy()
        if t < t_cue:
            i_ext[cue] += drive
        net.step(t, i_ext=i_ext, stdp_on=False)
        events.extend(net.spikes); net.spikes.clear()
        sp = net._prev
        if sp.size:
            image[s, sp] = 1.0
    fired = np.unique([nr for (tt, nr) in events if tt >= t_cue / 2])
    completeness = np.intersect1d(fired, noncue).size / max(1, noncue.size)
    false_pos = np.intersect1d(fired, non_pattern)
    false_positive_rate = false_pos.size / max(1, non_pattern.size)
    return dict(events=events, image=image, t_run=t_run, n_steps=n_steps,
                completeness=completeness, false_positive_rate=false_positive_rate,
                pattern=pattern, cue=cue, noncue=noncue)


def image_frames(result, bin_ms=20.0):
    """Collapse the per-step image into time bins (for animation)."""
    dt = result["n_steps"] and (result["t_run"] / result["n_steps"])
    bin_size = max(1, int(round(bin_ms / dt)))
    n = result["n_steps"]
    nb = n // bin_size
    frames = np.zeros((nb, result["image"].shape[1]))
    for b in range(nb):
        seg = result["image"][b * bin_size:(b + 1) * bin_size]
        frames[b] = (seg.sum(axis=0) > 0).astype(float)
    return frames


def recall_activity_map(result):
    """Union of all neurons that fired at any point during the recall period."""
    return (result["image"].sum(axis=0) > 0).astype(float)


@lru_cache(maxsize=8)
def get_trained(shape_name, seed=0):
    """Cached trained network for a shape (so sliders stay responsive)."""
    pattern = shape_pixels(shape_name)
    net, whist = train_network(pattern, seed=seed)
    return net, whist, pattern


# =========================================================================== #
# PART E — SLIDER EXPLORE FUNCTIONS (return matplotlib figures)
# =========================================================================== #
def explore_hh(I_amp=10.0, gK=36.0, t_end=30.0):
    """Interactive HH: injected current and K conductance."""
    import matplotlib.pyplot as plt
    res = simulate_hh(I_amp=I_amp, t_end=t_end, gK=gK)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4))
    axs[0].plot(res["t"], res["V"], color="C0")
    axs[0].axhline(-55, color="r", ls="--", lw=1, label="~-55 mV")
    axs[0].set_title("membrane voltage"); axs[0].set_xlabel("time (ms)")
    axs[0].set_ylabel("V (mV)"); axs[0].legend()
    axs[1].plot(res["t"], res["n"], color="C2", label=r"$n$ (K activation)")
    axs[1].plot(res["t"], res["n"] ** 4, color="C2", ls="--",
                label=r"$n^4$  $\propto$ K conductance")
    axs[1].set_title(r"the four K gates  ($n^4 \Rightarrow$ tetramer)")
    axs[1].set_xlabel("time (ms)"); axs[1].legend()
    fig.suptitle(f"HH  |  I = {I_amp} µA/cm²  |  gK = {gK}  "
                 f"|  spikes = {len(detect_spikes(res['t'], res['V'], -20))}")
    return fig


def explore_recall(shape_name="plus", cue_keep=0.5, noise=3.0):
    """Interactive recall on a pre-trained memory: how much cue / noise survives."""
    import matplotlib.pyplot as plt
    net, whist, pattern = get_trained(shape_name)
    net.p.noise = noise
    rng = np.random.default_rng(123)
    k = max(1, int(round(cue_keep * pattern.size)))
    cue = rng.choice(pattern, size=k, replace=False)
    res = probe_recall(net, pattern, cue, background_all=12.0)

    target = np.zeros(64); target[pattern] = 1.0
    cue_img = np.zeros(64); cue_img[cue] = 1.0
    recall_img = recall_activity_map(res)

    fig, axs = plt.subplots(1, 3, figsize=(12, 3.8))
    axs[0].imshow(target.reshape(8, 8), cmap="Blues", vmin=0, vmax=1)
    axs[0].set_title("target (learned memory)")
    axs[1].imshow(cue_img.reshape(8, 8), cmap="Oranges", vmin=0, vmax=1)
    axs[1].set_title(f"cue shown\n({k}/{pattern.size} pixels)")
    im = axs[2].imshow(recall_img.reshape(8, 8), cmap="Greens", vmin=0, vmax=1)
    axs[2].set_title(f"network recall (all activity)\n"
                     f"completeness={res['completeness']:.2f}  "
                     f"false-pos={res['false_positive_rate']:.2f}")
    for a in axs:
        a.set_xticks([]); a.set_yticks([])
    fig.colorbar(im, ax=axs[2], fraction=0.046, pad=0.04, label="fired (0/1)")
    fig.suptitle(f"'{shape_name}' recall  |  cue_keep={cue_keep:.2f}  "
                 f"|  noise={noise:.1f} mV")
    return fig


def animate_image_recall(shape_name="plus", cue_keep=0.5, noise=3.0, save_path=None):
    """Animate the 8x8 image filling in during recall."""
    import matplotlib
    if save_path:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation, PillowWriter

    net, whist, pattern = get_trained(shape_name)
    net.p.noise = noise
    rng = np.random.default_rng(123)
    k = max(1, int(round(cue_keep * pattern.size)))
    cue = rng.choice(pattern, size=k, replace=False)
    res = probe_recall(net, pattern, cue, background_all=12.0)
    frames = image_frames(res, bin_ms=10.0)

    target = np.zeros(64); target[pattern] = 1.0
    target_img = target.reshape(8, 8)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xticks([]); ax.set_yticks([])
    ax.imshow(target_img, cmap="gray", vmin=0, vmax=1, alpha=0.12)
    im = ax.imshow(frames[0].reshape(8, 8), cmap="Greens",
                   vmin=0, vmax=1, alpha=0.9, interpolation="nearest")
    ax.set_title(f"recall  t~0 ms", fontsize=13)
    ax.set_xlabel(f"target '{shape_name}' shown faint\n"
                  f"cue: {k}/{pattern.size} pixels", fontsize=9)

    def update(i):
        im.set_data(frames[i].reshape(8, 8))
        ax.set_title(f"recall  t~{i * 10} ms", fontsize=13)
        return im,

    ani = FuncAnimation(fig, update, frames=len(frames),
                        interval=100, blit=False)
    plt.close(fig)
    if save_path:
        try:
            ani.save(save_path, writer=PillowWriter(fps=10))
        except Exception:
            pass
    return ani


if __name__ == "__main__":
    # quick self-test
    hh = simulate_hh(I_amp=10.0)
    print("HH spikes:", detect_spikes(hh["t"], hh["V"], -20))
    net, wh = train_network(shape_pixels("plus"), seed=0)
    pat = shape_pixels("plus")
    cue = pat[:pat.size // 2]
    r = probe_recall(net, pat, cue)
    print(f"image task: within-w -> {wh[-1]:.2f}, completeness = {r['completeness']:.2f}")
