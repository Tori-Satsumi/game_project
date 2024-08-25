SQUARE_PIXEL = 8
SCREEN_WIDTH =  18 * SQUARE_PIXEL
SCREEN_HEIGHT = 32 * SQUARE_PIXEL
GAP = 2
SCALE = 2.5
Black = (0, 0, 0)
GAME_SPEED = 1.5
MEDAL_RAD = 3 * SQUARE_PIXEL


 # item : (x, y, width, height)
 
Back_ground : list[(int, int, int, int)] = [
    (0, 0, 144, 256),
    (146, 0, 144, 256)
]

GROUND : tuple[(int, int, int, int)] = (292, 0, 144, 56)
BOARD : tuple[(int, int, int, int)] =  (0, 256, 120, 64)
MEDAL : dict[str : (int, int, int, int)] = {
    "bronze medal"   : (111, 476, 24, 24),
    "silver_medal"   : (111, 452, 24, 24),
    "gold_medal"     : (120, 281, 24, 24),
    "platinum medal" : (120, 257, 24, 24),
}

BIRD : dict[str : list] = {
    "blue" : [
        (114, 328, 20, 14),
        (114, 354, 20, 14),
        (86, 490, 20, 14)
    ],
    "yellow" : [
        (2, 490, 20, 14),
        (30, 490, 20, 14),
        (58, 490, 20, 14)
    ],
    "red" : [
        (114, 380, 20, 14),
        (114, 406, 20, 14),
        (114, 432, 20, 14)
    ]
}

NUM : dict[str : list] = {
    "small"      : [
        (138, 323, 6, 7), 
        (138, 332, 6, 7),
        (138, 349, 6, 7),
        (138, 358, 6, 7),
        (138, 375, 6, 7),
        (138, 384, 6, 7),
        (138, 401, 6, 7),
        (138, 410, 6, 7),
        (138, 427, 6, 7),
        (138, 436, 6, 7)
    ],
    "med" : [
        (137, 306, 7, 10),
        (137, 477, 7, 10),
        (137, 489, 7, 10),
        (131, 501, 7, 10),
        (502, 0, 7, 10),
        (502, 12, 7, 10),
        (505, 26, 7, 10),
        (505, 42, 7, 10),
        (293, 242, 7, 10),
        (311, 206, 7, 10)
    ]
}


key_list = list(NUM.keys())
value_list = list()
 
test_name = key_list[len(key_list) - 1]