import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

BG = "#F4F7FB"
INK = "#172033"
MUTED = "#65738B"
GRID = "#D8E0EB"
BLUE = "#4C78E8"
TEAL = "#18A6A6"
CORAL = "#F05A67"
GOLD = "#F2B84B"

# Five toy cells with a local bandwidth for every anchor cell.
x = np.array([0.0, 0.55, 1.40, 2.75, 4.00])
sigma = np.array([0.72, 0.82, 0.70, 0.98, 0.88])
n = len(x)

d2_high = (x[:, None] - x[None, :]) ** 2
high_affinity = np.exp(-d2_high / (2 * sigma[:, None] ** 2))
np.fill_diagonal(high_affinity, 0.0)
p_conditional = high_affinity / high_affinity.sum(axis=1, keepdims=True)
p_joint = (p_conditional + p_conditional.T) / (2 * n)

probability_cmap = LinearSegmentedColormap.from_list(
    "tsne_probability", ["#F7F9FC", "#D9E4FB", "#86A8F2", "#2F5FC7"]
)

fig = plt.figure(figsize=(15.0, 7.2), facecolor=BG)
gs = fig.add_gridspec(
    2, 5,
    height_ratios=[1.0, 1.0],
    width_ratios=[1.45, 1.15, 0.14, 1.0, 1.0],
    left=0.045, right=0.975, top=0.88, bottom=0.11,
    hspace=0.42, wspace=0.52,
)
ax_kernel = fig.add_subplot(gs[0, :2])
ax_neighbor = fig.add_subplot(gs[1, :2])
ax_conditional = fig.add_subplot(gs[:, 3])
ax_p = fig.add_subplot(gs[:, 4])

# A | Kernel shapes.
distance = np.linspace(0, 4.0, 500)
gaussian = np.exp(-(distance ** 2) / 2)
student_t = 1 / (1 + distance ** 2)
ax_kernel.plot(distance, gaussian, color=TEAL, lw=3.0, label="Gaussian affinity")
ax_kernel.plot(distance, student_t, color=CORAL, lw=3.0, label="Student-t affinity")
tail = distance >= 2.0
ax_kernel.fill_between(
    distance[tail], gaussian[tail], student_t[tail],
    color=CORAL, alpha=0.13,
)
ax_kernel.annotate(
    "heavy tail keeps distant points\nable to repel one another",
    xy=(2.55, 1 / (1 + 2.55 ** 2)), xytext=(2.55, 0.47),
    ha="center", va="center", color=MUTED, fontsize=9.3,
    arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2),
)
ax_kernel.set(
    xlim=(0, 4), ylim=(-0.02, 1.04),
    xlabel="distance", ylabel="unnormalized affinity",
    title="A  |  Distance becomes affinity",
)
ax_kernel.legend(frameon=False, loc="upper right", fontsize=9)
ax_kernel.grid(axis="both", color=GRID, lw=0.7, alpha=0.65)

# B | One row of conditional neighbor probabilities.
anchor = 1
bar_colors = [BLUE if j != anchor else GRID for j in range(n)]
bars = ax_neighbor.bar(
    np.arange(n), p_conditional[anchor],
    color=bar_colors, width=0.66, edgecolor="white", linewidth=1.0,
)
for j, (bar, value) in enumerate(zip(bars, p_conditional[anchor])):
    label = "self" if j == anchor else f"{value:.2f}"
    ax_neighbor.text(
        bar.get_x() + bar.get_width() / 2,
        max(value, 0.015) + 0.025,
        label, ha="center", va="bottom",
        color=MUTED if j == anchor else INK,
        fontsize=9, fontweight="bold" if j != anchor else "normal",
    )
ax_neighbor.set(
    xticks=np.arange(n),
    xticklabels=[f"cell {j + 1}" for j in range(n)],
    ylim=(0, max(p_conditional[anchor]) * 1.30),
    ylabel=r"$p_{j\mid i}$",
    title=f"B  |  Cell {anchor + 1} chooses neighbors (row sums to 1)",
)
ax_neighbor.spines[["top", "right"]].set_visible(False)
ax_neighbor.grid(axis="y", color=GRID, lw=0.7, alpha=0.65)

def probability_matrix(ax, matrix, title, vmax):
    ax.imshow(
        matrix, cmap=probability_cmap,
        vmin=0, vmax=vmax, interpolation="nearest",
    )
    ax.set_xticks(range(n), [str(i + 1) for i in range(n)])
    ax.set_yticks(range(n), [str(i + 1) for i in range(n)])
    ax.set_title(title, loc="left", pad=12)
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", bottom=False, left=False)
    for row in range(n):
        for col in range(n):
            value = matrix[row, col]
            if row == col:
                text, color = "—", "#A9B4C5"
            else:
                text = f"{value:.2f}"
                color = "white" if value > 0.58 * vmax else INK
            ax.text(
                col, row, text, ha="center", va="center",
                color=color, fontsize=8.4,
                fontweight="bold" if row != col else "normal",
            )
    for spine in ax.spines.values():
        spine.set_visible(False)

probability_matrix(
    ax_conditional, p_conditional,
    r"C  |  Directional  $p_{j\mid i}$", p_conditional.max(),
)
probability_matrix(
    ax_p, p_joint,
    r"D  |  Symmetric target  $P$", p_joint.max(),
)

ax_conditional.text(
    0.5, -0.16, "each row sums to 1\nbut the matrix is asymmetric",
    transform=ax_conditional.transAxes, ha="center", va="top",
    color=MUTED, fontsize=8.8,
)
ax_p.text(
    0.5, -0.16, r"$p_{ij}=(p_{j|i}+p_{i|j})/(2n)$",
    transform=ax_p.transAxes, ha="center", va="top",
    color=MUTED, fontsize=8.8,
)
fig.suptitle(
    "t-SNE turns pairwise distances into neighbor probabilities",
    x=0.045, y=0.965, ha="left",
    fontsize=20, fontweight="bold", color=INK,
)
plt.show()
