import logging
from time import sleep

from selenium.common.exceptions import WebDriverException

from selenium_bet365.driver import Driver
from algo.rule_based import can_bet_game_s1, can_bet_game_s2, check_number_of_amg
from service import line
from config import settings


logger = logging.getLogger(__name__)


class Action(object):

    def __init__(self):
        self.driver = Driver()

    def setup(self):
        try:
            self.driver.login()
            sleep(5)
            self.driver.click_football_icon()
            self.driver.click_top_game()
        except WebDriverException as e:
            import traceback
            traceback.print_exc()
            self.driver.quit()
            sleep(10)
            logger.warning('driver restart')
            self.driver = Driver()
            self.setup()

    def bet_checker(self):
        while True:
            self.driver.open_all_game_league()
            self.search_valid_game()

            sleep(settings.bet_checker_interval)

    def search_valid_game(self):
        timers, scores = self.driver.get_game_time_and_score()
        for i in range(len(timers)):
            time = int(timers[i].text[:2])
            score = [int(scores[i*2].text), int(scores[i*2+1].text)]

            if can_bet_game_s1(time, score):
                timers[i].click()
                logger.info(f'game_time={time} score={score}')

                if self.exist_bet_method() and self.check_game_detail():
                    print(self.driver.current_url)
                    line.send_message(self.driver.current_url)

    def exist_bet_method(self):
        exist = False
        if self.driver.exist_fulltime_result():
            exist = True
        if check_number_of_amg(self.driver.find_alternative_match_goals()):
            exist = True
        return exist

    def check_game_detail(self):
        info = self.driver.get_game_detail_info()
        print(info)
        return can_bet_game_s2(info)
