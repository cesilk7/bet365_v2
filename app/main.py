import datetime
import logging
import os
import re
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


load_dotenv()
LOCAL_DRIVER = eval(os.environ['LOCAL_DRIVER'])
LOCAL_DRIVER_PATH = os.environ['LOCAL_DRIVER_PATH']
HEADLESS = eval(os.environ['HEADLESS'])

options = webdriver.FirefoxOptions()
if HEADLESS:
    options.add_argument('--headless')
options.add_argument('--window-size=1280,1024')

if LOCAL_DRIVER:
    driver = webdriver.Firefox(
        executable_path=LOCAL_DRIVER_PATH,
        options=options,
    )
else:
    driver = webdriver.Remote(
        desired_capabilities=DesiredCapabilities.FIREFOX,
        command_executor='http://selenium-container:4444',
    )

driver.get('https://www.bet365.com/#/IP/B1')

sleep(60)
