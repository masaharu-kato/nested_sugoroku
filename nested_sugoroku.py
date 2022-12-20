#
#   nested_sugoroku.py
#

import random

N_DICE_NUMS = 6
N_POS = 6

class TooManyRollsError(RuntimeError):
    """ TooManyRollsError """

def roll_dice():
    """ Get a random number of dice """
    return random.randrange(N_DICE_NUMS) + 1

def nested_sugoroku(*, max_rolls: int):
    """ Play Nested Sugoroku """
    try:
        n_rolls = 0
        max_depth = 0
        poses :list[int] = [0]

        while poses:
            max_depth = max(max_depth, len(poses))
            pos = poses[-1]

            while True:
                if pos >= N_POS:
                    poses.pop()
                    break
                if pos:
                    poses.append(0)
                    break
                dice = roll_dice()
                new_pos = min(pos + dice, N_POS)
                # print("Roll #{}, Depth: {}, Dice: {}, Pos: {} -> {}".format(n_rolls, len(poses), dice, pos, new_pos))
                n_rolls += 1
                pos = new_pos
                if n_rolls >= max_rolls:
                    raise TooManyRollsError()

    except TooManyRollsError:
        # print("Failed: {} rolls, max depth: {}".format(n_rolls, max_depth))
        return False
    
    # print("Goaled: {} rolls, max depth: {}".format(n_rolls, max_depth))
    return True

def main():
    """ Main """
    for max_rolls in [10, 100, 1000, 10000, 100000]:
        n_all = 1000
        n_goaled = 0
        random.seed(0)

        for _ in range(n_all):
            result = nested_sugoroku(max_rolls=max_rolls)
            if result:
                n_goaled += 1
        
        print("max rolls: {}, Goaled: {} / {}".format(max_rolls, n_goaled, n_all))

if __name__ == '__main__':
    main()
