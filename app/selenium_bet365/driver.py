import datetime
import logging
import os
import re
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import xpath as xp
from config import settings


js_open_all_game_league = """
elements = document.getElementsByClassName('ipn-Competition-closed')
for (let i = 0; i < elements.length; i++)
    elements[0].click()
"""
logger = logging.getLogger(__name__)


class Driver(object):

    def __init__(self):
        options = webdriver.FirefoxOptions()
        if settings.headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1400,1200')

        if settings.local_driver:
            self.driver = webdriver.Firefox(
                executable_path=settings.local_driver_path,
                options=options,
            )
        else:
            self.driver = webdriver.Remote(
                desired_capabilities=DesiredCapabilities.FIREFOX,
                command_executor='http://selenium-container:4444',
            )
        self.driver.get('https://www.bet365.com/#/IP/B1')
        self.driver.set_window_size(1400, 980)

    @property
    def current_url(self):
        return self.driver.current_url

    def _action_element(self, xpath, action=None):
        try:
            element = self.driver.find_element(by=By.XPATH, value=xpath)
            if action == 'click':
                element.click()
                return True
            elif action == 'str':
                return element.text
            elif action == 'int':
                return int(element.text)
            else:
                return element
        except NoSuchElementException as e:
            logger.warning(f'element not found {e}')
            return None

    def login(self):
        element = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, xp.login))
        )
        self.driver.execute_script('arguments[0].click();', element)
        sleep(5)

        username = self._action_element(xp.login_user)
        password = self._action_element(xp.login_pass)
        username.clear()
        password.clear()
        username.send_keys(settings.username)
        password.send_keys(settings.password)

        sleep(1)
        self._action_element(xp.login_btn, 'click')
        logger.info('login is success')

    def quit(self):
        self.driver.close()
        self.driver.quit()

    def click_football_icon(self):
        # element = WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, ep.football_icon))
        # )
        # self.driver.execute_script('arguments[0].click();', element)
        self._action_element(xp.football_icon, 'click')

    def click_top_game(self):
        self.driver.find_elements(by=By.XPATH, value=xp.top_game)[0].click()

    def open_all_game_league(self):
        sleep(2)
        # self.driver.execute_script(js_open_all_game_league)
        for e in self.driver.find_elements(by=By.XPATH, value=xp.closed_league):
            e.click()
        logger.info('all game tag closed clicked')

    def get_game_time_and_score(self):
        timers = self.driver.find_elements(by=By.XPATH, value=xp.game_timer)
        scores = self.driver.find_elements(by=By.XPATH, value=xp.game_scores)

        return timers, scores

    def get_game_detail_info(self):
        # stats info
        if not self._action_element(xp.stats_tag, 'click'):
            print('not stats info')
            return None
        play_time = self._action_element(xp.play_time, 'str')
        attacks = [self._action_element(xp.attacks_1, 'int'), self._action_element(xp.attacks_2, 'int')]
        d_attacks = [self._action_element(xp.d_attacks_1, 'int'), self._action_element(xp.d_attacks_2, 'int')]
        possessions = [self._action_element(xp.possession_1, 'int'), self._action_element(xp.possession_2, 'int')]
        if not (possessions[0] and possessions[1]):
            possessions = [50, 50]
        y_card = [self._action_element(xp.yellow_card_1, 'int'), self._action_element(xp.yellow_card_2, 'int')]
        r_card = [self._action_element(xp.red_card_1, 'int'), self._action_element(xp.red_card_2, 'int')]
        corner_kick = [self._action_element(xp.corner_kick_1, 'int'), self._action_element(xp.corner_kick_2, 'int')]
        on_target = [self._action_element(xp.on_target_1, 'int'), self._action_element(xp.on_target_2, 'int')]
        off_target = [self._action_element(xp.off_target_1, 'int'), self._action_element(xp.off_target_2, 'int')]

        # summary info
        self._action_element(xp.summary_tag, 'click')
        sleep(0.5)
        shifts = [self._action_element(xp.shifts_1, 'int'), self._action_element(xp.shifts_2, 'int')]
        pk = [self._action_element(xp.pk_1, 'int'), self._action_element(xp.pk_2, 'int')]
        goals = [self._action_element(xp.goal_1, 'int'), self._action_element(xp.goal_2, 'int')]

        self._action_element(xp.show_more, 'click')
        goal_times = self.get_goal_time_of_summary()

        return {
            'play_time': play_time,
            'attacks': attacks,
            'd_attacks': d_attacks,
            'possessions': possessions,
            'y_card': y_card,
            'r_card': r_card,
            'corner_kick': corner_kick,
            'on_target': on_target,
            'off_target': off_target,
            'shifts': shifts,
            'pk': pk,
            'goals': goals,
            'goal_times': goal_times}

    def get_goal_time_of_summary(self):
        home_goals = self.driver.find_elements(by=By.XPATH, value=xp.home_goals)
        away_goals = self.driver.find_elements(by=By.XPATH, value=xp.away_goals)

        goal_time = [[], []]
        if home_goals:
            for i in range(len(home_goals)):
                goal_time[0].append(eval(home_goals[i].text.replace("'", '')))
        if away_goals:
            for i in range(len(away_goals)):
                goal_time[1].append(eval(away_goals[i].text.replace("'", '')))
        if goal_time[0] or goal_time[1]:
            return goal_time
        return None

    def exist_fulltime_result(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, xp.fulltime_result_text))
            )
            return True
        except NoSuchElementException:
            return False

    def find_alternative_match_goals(self):
        return len(self.driver.find_elements(By.XPATH, value=xp.number_of_amg))
