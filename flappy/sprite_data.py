SQUARE_PIXEL = 8
SCREEN_WIDTH =  18 * SQUARE_PIXEL
SCREEN_HEIGHT = 32 * SQUARE_PIXEL
GAP = 2
SCALE = 2.5
Black = (0, 0, 0)
GAME_SPEED = 1.5
MEDAL_RAD = 3 * SQUARE_PIXEL


 # item : (x, y, width, height)
 
sprite_data : dict = {
    "bg_day"         : (0, 0, 144, 256),
    "bg_night"       : (144 + GAP, 0, 144, 256),
    "ground"         : (144 * 2 + GAP * 2, 0, 144, 7 * SQUARE_PIXEL),
    "score_board"    : (0, 256, 15 * SQUARE_PIXEL, 8 * SQUARE_PIXEL),
    "bronze medal"   : (14 * SQUARE_PIXEL - 1, 19 * SQUARE_PIXEL + 320 + 4, MEDAL_RAD, MEDAL_RAD),
    "silver_medal"   : (14 * SQUARE_PIXEL - 1, 16 * SQUARE_PIXEL + 320 + 4, MEDAL_RAD, MEDAL_RAD),
    "gold_medal"     : (15 * SQUARE_PIXEL, 256 + MEDAL_RAD + 1, MEDAL_RAD, MEDAL_RAD),
    "platinum medal" : (15 * SQUARE_PIXEL, 256 + 1, MEDAL_RAD, MEDAL_RAD),
    "blue_bird_1"    : (14 * SQUARE_PIXEL + GAP, 320, 17, 12)


}