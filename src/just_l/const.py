"""使用される定数"""
BLOCK_SHAPE_DICT: dict[str, list[list[int]]] = \
    {
        "J": [
                [1, 1, 1],
                [0, 1, 0],
                [1, 1, 0]
             ],
        
        "U": [
                [1, 0, 1],
                [1, 0, 1],
                [1, 1, 1]
             ],
        
        "S": [
                [0, 1, 1],
                [0, 1, 0],
                [1, 1, 0]
             ],
        
        "T": [
                [1, 1, 1],
                [0, 1, 0],
                [0, 1, 0]
             ],
        
        "L": [
                [1, 0, 0],
                [1, 0, 0],
                [1, 1, 1]
             ]
    }

COLOR_DICT: dict[str, str] = \
    {
        "J": "red",
        "U": "green",
        "S": "blue",
        "T": "orange",
        "L": "mediumpurple"
    }
