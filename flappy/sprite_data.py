SQUARE_PIXEL = 8
SCREEN_WIDTH =  18 * SQUARE_PIXEL
SCREEN_HEIGHT = 32 * SQUARE_PIXEL
GAP = 2
SCALE = 2.5
Black = (0, 0, 0)
GAME_SPEED = 1.5
MEDAL_RAD = 3 * SQUARE_PIXEL


 # item : (x, y, width, height)
 
sprite_data : dict[str : (int, int, int, int)] = {
    "bg_day"         : (0, 0, 144, 256),
    "bg_night"       : (146, 0, 144, 256),
    "ground"         : (292, 0, 144, 56),
    "score_board"    : (0, 256, 120, 64),
    "bronze medal"   : (111, 476, 24, 24),
    "silver_medal"   : (111, 452, 24, 24),
    "gold_medal"     : (120, 281, 24, 24),
    "platinum medal" : (120, 257, 24, 24),
    "blue_bird_1"    : (114, 328, 20, 14),
    "blue_bird_2"    : (114, 354, 20, 14),
    "blue_bird_3"    : (86, 490, 20, 14),
    "yellow_bird_1"  : (2, 490, 20, 14),
    "yellow_bird_2"  : (30, 490, 20, 14),
    "yellow_bird_3"  : (58, 490, 20, 14),
    "red_bird_1"     : (114, 380, 20, 14),
    "red_bird_2"     : (114, 406, 20, 14),
    "red_bird_3"     : (114, 432, 20, 14),
    "small_num"      : [
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
    "med_num" : [
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
    ],
    
}

key_list = list(sprite_data.keys())
value_list = list(sprite_data.values())
 
test_name = key_list[len(key_list) - 1]