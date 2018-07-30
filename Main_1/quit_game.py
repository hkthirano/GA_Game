import sys

from variable import *


def quit_game(score, penalty):
    if penalty == 0:
        print('Total Score:' + str(score))
    else:
        print('Total Score:' + str(int(score-penalty*10)))

    sys.exit()
