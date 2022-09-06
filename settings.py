from sort.exchanging import *


resolution = {'SD': [640, 480], 'HD': [1280, 720], 'Full HD': [1900, 1020]}
# def settings(mode):
ALTURA, AMPLE = 1000, 1920



HEADER = 100
sep = 20

black = (0, 0, 0)
grey = (211,211,211)
grey_menu = (170, 183, 184)
white = (255, 255, 255)
green = (124,252,0)
green_win = (40, 180, 99)
blue = (135,206,250)
red = (220,20,60)
maroon = (128,0,0)
purple = (221,160,221)
white_dirty = (244, 246, 247)


AVAILABLE_ALGORITHMS = {
    "bubble": Bubble(),
    "cocktailshake": CocktailShake(),
    "gnome": Gnome(),
    "oddeven": OddEven(),
    "comb11": Comb11(),
}