import os

from dotenv import load_dotenv


load_dotenv()

local_driver = eval(os.environ['LOCAL_DRIVER'])
local_driver_path = os.environ['LOCAL_DRIVER_PATH']
headless = eval(os.environ['HEADLESS'])

username = os.environ['BET365_USER']
password = os.environ['BET365_PASS']

database_url = os.environ['DATABASE_URL']

line_token = os.environ['LINE_TOKEN']
slack_url = os.environ['SLACK_URL']

bet_checker_interval = 300
