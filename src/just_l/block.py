"""J, U, S, T, Lのブロックを回転と共に図示する"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

from just_l.const import BLOCK_SHAPE_DICT, COLOR_DICT

fig, axes = plt.subplots(5, 4, figsize=(16, 20), dpi=200)

for i, c in enumerate("JUSTL"):
    mat = np.array(BLOCK_SHAPE_DICT[c])
    cmap = ListedColormap(["white", COLOR_DICT[c]])
    for j in range(4):
        ax = axes[i, j]
        mat_to_show = np.rot90(mat, -j).copy()
        ax.imshow(mat_to_show, cmap)
        for k in range(4):
            ax.hlines(k - 0.5, -0.5, 2.5, color="black", linewidth=2)
        for k in range(4):
            ax.vlines(k - 0.5, -0.5, 2.5, color="black", linewidth=2)
        ax.axis("off")
        if i == 0:
            ax.annotate(f"{j+1} (Rotate {90 * j}° CW)", xy=(0.5, 1.1), xycoords='axes fraction',
                        fontsize=20, ha='center', va='bottom')
        if j == 0:
            ax.annotate(c, xy=(-0.1, 0.5), xycoords='axes fraction',
                        fontsize=20, ha='right', va='center')

plt.savefig("images/blocks.png")
plt.close()
