import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


BG = "#F4F7FB"
PANEL = "#FFFFFF"
INK = "#172033"
MUTED = "#66738A"
GRID = "#DCE4EF"
TRACK = "#EDF2F7"
TEAL = "#18A6A6"
CORAL = "#F05A67"
BLUE = "#4C78E8"

genes = [
    "CD3D", "IL7R", "LTB", "CCR7",
    "MKI67", "TOP2A", "STMN1",
    "FOS", "JUN", "DDIT3",
    "MALAT1", "RPLP0",
]

programs = np.array(
    [
        [0.96, 0.84, 0.73, 0.58, 0.02, 0.00, 0.08, 0.08, 0.05, 0.02, 0.24, 0.20],
        [0.02, 0.01, 0.03, 0.02, 1.00, 0.90, 0.76, 0.08, 0.05, 0.03, 0.15, 0.20],
        [0.04, 0.03, 0.05, 0.05, 0.03, 0.01, 0.08, 1.00, 0.88, 0.72, 0.15, 0.15],
    ]
)
activities = np.array([1.00, 0.65, 0.42])
contributions = activities[:, None] * programs
x = contributions.sum(axis=0)
scale = x.max()

program_names = ["T-cell identity", "Cell cycle", "Stress response"]
program_symbols = [r"\mathbf{w}_1", r"\mathbf{w}_2", r"\mathbf{w}_3"]
colors = [TEAL, CORAL, BLUE]
card_x = [0.385, 0.585, 0.785]


def rounded_box(ax, x0, y0, width, height, facecolor=PANEL, edgecolor=GRID, radius=0.018):
    patch = FancyBboxPatch(
        (x0, y0),
        width,
        height,
        boxstyle=f"round,pad=0.008,rounding_size={radius}",
        linewidth=1.2,
        edgecolor=edgecolor,
        facecolor=facecolor,
    )
    ax.add_patch(patch)
    return patch


fig, ax = plt.subplots(figsize=(15.5, 7.0), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(
    0.04,
    0.955,
    "NMF explains a cell as a mixture of reusable gene programs",
    fontsize=24,
    fontweight="bold",
    color=INK,
    va="top",
)

# Observed vector
rounded_box(ax, 0.035, 0.17, 0.285, 0.65)
ax.text(0.055, 0.785, r"one cell's expression  $\mathbf{x}$", fontsize=15, fontweight="bold", color=INK)
ax.text(0.055, 0.752, "genes × 1", fontsize=11, color=MUTED)

row_top = 0.680
row_gap = 0.0405
bar_x = 0.118
bar_width = 0.175
bar_height = 0.021

for gene_index, gene in enumerate(genes):
    y = row_top - gene_index * row_gap
    ax.text(0.055, y + bar_height / 2, gene, fontsize=10.5, color=INK, va="center")
    ax.add_patch(Rectangle((bar_x, y), bar_width, bar_height, color=TRACK, linewidth=0))
    cursor = bar_x
    for program_index, color in enumerate(colors):
        width = bar_width * contributions[program_index, gene_index] / scale
        ax.add_patch(Rectangle((cursor, y), width, bar_height, color=color, linewidth=0))
        cursor += width

ax.text(
    0.177,
    0.198,
    "each entry is a sum",
    fontsize=10.5,
    color=MUTED,
    ha="center",
)

# Decomposition sign
ax.text(0.348, 0.515, r"$\approx$", fontsize=35, fontweight="bold", color=INK, ha="center", va="center")

# Program cards
for program_index, (x0, name, symbol, color) in enumerate(
    zip(card_x, program_names, program_symbols, colors)
):
    rounded_box(ax, x0, 0.17, 0.17, 0.65, facecolor=PANEL)
    ax.add_patch(
        FancyBboxPatch(
            (x0 + 0.012, 0.748),
            0.146,
            0.052,
            boxstyle="round,pad=0.005,rounding_size=0.012",
            linewidth=0,
            facecolor=color,
            alpha=0.14,
        )
    )
    ax.text(x0 + 0.022, 0.78, name, fontsize=12.5, fontweight="bold", color=INK, va="center")
    ax.text(
        x0 + 0.022,
        0.738,
        rf"activity  $h_{program_index + 1}={activities[program_index]:.2f}$",
        fontsize=10.5,
        color=MUTED,
        va="top",
    )

    track_x = x0 + 0.022
    track_width = 0.126
    for gene_index in range(len(genes)):
        y = row_top - gene_index * row_gap
        ax.add_patch(Rectangle((track_x, y), track_width, bar_height, color=TRACK, linewidth=0))
        width = track_width * contributions[program_index, gene_index] / scale
        ax.add_patch(Rectangle((track_x, y), width, bar_height, color=color, linewidth=0))

    ax.text(
        x0 + 0.085,
        0.198,
        rf"$h_{program_index + 1}\,{symbol}$",
        fontsize=13,
        color=color,
        fontweight="bold",
        ha="center",
    )

for plus_x in (0.565, 0.765):
    ax.text(plus_x, 0.515, "+", fontsize=28, fontweight="bold", color=MUTED, ha="center", va="center")

ax.text(
    0.675,
    0.855,
    "same gene axis, different reusable patterns",
    fontsize=11.5,
    color=MUTED,
    ha="center",
)

ax.text(
    0.50,
    0.105,
    r"$\mathbf{x}\;\approx\;h_1\mathbf{w}_1+h_2\mathbf{w}_2+h_3\mathbf{w}_3$"
    r"$\qquad h_k\geq 0,\;\mathbf{w}_k\geq 0$",
    fontsize=19,
    color=INK,
    ha="center",
)
ax.text(
    0.50,
    0.052,
    r"Across cells, NMF reuses the same programs $\mathbf{w}_k$ but learns a different activity vector $\mathbf{h}$ for each cell.",
    fontsize=11.5,
    color=MUTED,
    ha="center",
)

plt.tight_layout(pad=1.0)
plt.show()
