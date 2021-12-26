import logging

from selenium_bet365.action import Action


logging.basicConfig(
    level=logging.INFO,
    format='{asctime} [{levelname:.4}] {name}: {message}',
    style='{',
    # filename='',
)


if __name__ == '__main__':
    action = Action()
    action.setup()
    action.bet_checker()
