"""盤面の可視化（入力と出力結果の両方）"""

import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from just_l.const import BLOCK_SHAPE_DICT, COLOR_DICT


def visualize_input(lines_in: list[str]) -> tuple[Figure, Axes]:
    """入力盤面の表示

    Args:
        lines (list[str]): 入力文字列

    Returns:
        tuple[Figure, Axes]: (fig, ax)
    """
    # 盤面作成
    H, W, N = (int(x) for x in lines_in[0].split())
    fig, ax = plt.subplots(dpi=200)
    fig.set_size_inches(W, H)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_xticks(range(W + 1))
    ax.set_yticks(range(H + 1))
    ax.grid(which="both", linestyle="-", color="black")
    ax.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
    for i in range(H):
        ax.text(-0.1, H - i - 0.5, str(i + 1), ha='right', va='center', fontsize=10)
    for j in range(W):
        ax.text(j + 0.5, H + 0.1, str(j + 1), ha='center', va='bottom', fontsize=10)

    # 文字描画
    for i in range(N):
        SRC = lines_in[i + 1].split()
        S = SRC[0]
        R = int(SRC[1]) - 1
        C = int(SRC[2]) - 1
        ax.text(C + 0.5, H - R - 0.5, S, color=COLOR_DICT[S], ha='center', va='center', fontsize=12)
    
    return fig, ax


def visualize_output(lines_in: list[str], lines_out: list[str]) -> tuple[Figure, Axes]:
    """出力盤面の表示

    Args:
        lines_in (list[str]): 入力文字列
        lines_out (list[str]): 出力文字列

    Returns:
        tuple[Figure, Axes]: (fig, ax)
    """
    # 盤面作成    
    H, W, N = (int(x) for x in lines_in[0].split())
    fig, ax = visualize_input(lines_in)

    # ブロック描画
    if lines_out[0] == "No":
        return fig, ax
    M = int(lines_out[1])
    for i in range(M):
        TXYZ = lines_out[i + 2].split()
        T = TXYZ[0]
        X, Y, Z = (int(x) - 1 for x in TXYZ[1:])
        block_ = BLOCK_SHAPE_DICT[T]
        block = np.rot90(block_, -Z).copy()
        for i in range(3):
            for j in range(3):
                if block[i][j]:
                    rect = patches.Rectangle((Y + j - 1, H - X - i), 1, 1, color=COLOR_DICT[T], alpha=0.3)
                    ax.add_patch(rect)

    return fig, ax    


if __name__ == "__main__":
    from pathlib import Path
    
    path_to_in = Path("examples/ex1/in.txt")
    with open(path_to_in) as f:
        lines_in = f.readlines()
    
    path_to_out = Path("examples/ex1/out1.txt")
    with open(path_to_out) as f:
        lines_out = f.readlines()

    # visualize_input(lines_in)
    fig, _ = visualize_output(lines_in, lines_out)
    plt.show()
    