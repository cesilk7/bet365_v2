
BET_GAME_TIME_UNDER = 59
BET_GAME_TIME_OVER = 68

# alternative match goals
AMG_MAX_GOAL = 3
NOT_GOAL_COUNT_1 = 0
NOT_GOAL_COUNT_2 = 3
METHOD_MIN_COUNT = 2
AMG_MAX_NUM = 2
# game status
ATTACKS_COUNT_DIFF = 20
ATTACKS_COUNT_LIMIT = 150
D_ATTACKS_COUNT_DIFF = 20
D_ATTACKS_COUNT_LIMIT = 100
POSSESSION_DIFF = 20
YELLOW_CARD_LIMIT = 10
RED_CARD_LIMIT = 0
CORNER_KICK_LIMIT = 12
ON_TARGET_DIFF = 2
ON_TARGET_LIMIT = 8
OFF_TARGET_DIFF = 3
OFF_TARGET_LIMIT = 12
PK_LIMIT = 0

# fulltime result
FR_MIN_GOAL_DIFF = 3


def check_number_of_amg(amg_num):
    return amg_num >= AMG_MAX_NUM


def can_bet_game_s1(time, score):
    # time
    if time < BET_GAME_TIME_UNDER or BET_GAME_TIME_OVER < time:
        return False

    valid = False

    # Alternative Match Goals
    if sum(score) <= AMG_MAX_GOAL and not (NOT_GOAL_COUNT_1 in score and NOT_GOAL_COUNT_2 in score):
        valid = True
    # Fulltime Result
    if abs(score[0] - score[1]) >= FR_MIN_GOAL_DIFF:
        valid = True
    return valid


def can_bet_game_s2(info):
    """
    :param info:
        play_time: '63:39'
        attacks: [78, 69]
        d_attacks: [44, 38]
        possessions: [48, 52]
        y_card: [2, 5]
        r_card: [0, 0]
        corner_kick: [5, 3]
        on_target: [2, 4]
        off_target: [8, 6]
        shifts: [4, 1]
        pk: [1, 0]
        goals: [2, 1]
        goal_times: [[23, 44], [69]]
    """
    if info is None:
        return False

    a_1 = info['attacks'][0]
    a_2 = info['attacks'][1]
    if a_1 == 0 or a_2 == 0 or ATTACKS_COUNT_DIFF < abs(a_1 - a_2) or \
            ATTACKS_COUNT_LIMIT < a_1 + a_2:
        return False

    da_1 = info['d_attacks'][0]
    da_2 = info['d_attacks'][1]
    if da_1 == 0 or da_2 == 0 or D_ATTACKS_COUNT_DIFF < abs(da_1 - da_2) or \
            D_ATTACKS_COUNT_LIMIT < da_1 + da_2:
        return False

    if POSSESSION_DIFF < abs(info['possessions'][0] - info['possessions'][1]):
        return False

    if YELLOW_CARD_LIMIT < info['y_card'][0] + info['y_card'][1]:
        return False

    if RED_CARD_LIMIT < info['r_card'][0] + info['r_card'][1]:
        return False

    if CORNER_KICK_LIMIT < info['corner_kick'][0] + info['corner_kick'][1]:
        return False

    on_1 = info['on_target'][0]
    on_2 = info['on_target'][1]
    if (on_1 == 0 and on_2 == 0) or ON_TARGET_DIFF < abs(on_1 - on_2) or \
            ON_TARGET_LIMIT < on_1 + on_2:
        return False

    off_1 = info['off_target'][0]
    off_2 = info['off_target'][1]
    if (off_1 == 0 and off_2 == 0) or OFF_TARGET_DIFF < abs(off_1 - off_2) or \
            OFF_TARGET_LIMIT < off_1 + off_2:
        return False

    if PK_LIMIT < abs(info['pk'][0] + info['pk'][1]):
        return False

    return True
