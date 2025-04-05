import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 8))


boxes = [
    ("Farmer App (Voice/Text Input)", 0.1, 0.8),
    ("Voice to Text / Text Processor", 0.4, 0.8),
    ("Advisory Engine", 0.4, 0.6),
    ("Crop Image Diagnosis (CNN)", 0.1, 0.6),
    ("Yield Predictor (ML + GEE)", 0.7, 0.6),
    ("Advisory Output (Regional Lang.)", 0.4, 0.4)
]

for label, x, y in boxes:
    ax.add_patch(patches.FancyBboxPatch((x, y), 0.25, 0.1, boxstyle="round,pad=0.02", edgecolor='black', facecolor='lightgreen'))
    ax.text(x + 0.125, y + 0.05, label, ha='center', va='center')


arrows = [
    ((0.1 + 0.25, 0.85), (0.4, 0.85)),
    ((0.4 + 0.25, 0.85), (0.7, 0.65)),
    ((0.1 + 0.25, 0.65), (0.4, 0.65)),
    ((0.4 + 0.25, 0.65), (0.7, 0.65)),
    ((0.4 + 0.125, 0.6), (0.4 + 0.125, 0.4))
]

for start, end in arrows:
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", lw=2))

ax.axis('off')
plt.tight_layout()
plt.savefig("diagrams/architecture_diagram.png")
plt.show()
