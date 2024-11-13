"""入力例の生成"""
import random


def generate_input(H: int, W: int, N: int, seed: int) -> str:
    """入力例の生成

    Args:
        H (int): 盤面の縦幅
        W (int): 盤面の横幅
        N (int): 文字の数
        seed (int): 乱数のシード値

    Returns:
        str: _description_
    """
    random.seed(seed)
    used_point = set()
    SRC_list = [f"{H} {W} {N}"]
    for _ in range(N):
        S = random.choice("JUSTL")
        while True:
            R = random.choice(range(1, H + 1))
            C = random.choice(range(1, W + 1))
            if (R, C) not in used_point:
                used_point.add((R, C))
                SRC_list.append(f"{S} {R} {C}")
                break
    return "\n".join(SRC_list)

if __name__ == "__main__":
    """動作確認"""
    print(generate_input(3, 10, 5, 42))
    
    