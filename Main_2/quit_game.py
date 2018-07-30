import sys

from variable import *


def quit_game(score, penalty):

    save_file = open('save.txt', 'w')
    save_file.write(str(score-penalty*10))
    save_file.close()

    # if penalty == 0:
    #print('Total Score:' + str(score))
    # else:
    #print('Total Score:' + str(int(score-penalty*10)))

    sys.exit()
