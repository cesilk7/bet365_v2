from models.base import init_db, session_scope
from models import BetHistories


if __name__ == '__main__':
    init_db()

    info = {
        'league': 'abcde',
        'teams': ['red', 'blue'],
        'play_time': '63:39',
        'attacks': [78, 69],
        'd_attacks': [44, 38],
        'possessions': [48, 52],
        'y_card': [2, 5],
        'r_card': [0, 0],
        'corner_kick': [5, 3],
        'on_target': [2, 4],
        'off_target': [8, 6],
        'shifts': [4, 1],
        'pk': [1, 0],
        'goals': [2, 1],
        'goal_times': [[23, 44], [69]],
    }
    BetHistories.create(info)
