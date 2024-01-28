import json

from appium import webdriver
from appium.options.common import AppiumOptions


def initialize_appium_driver():
    desired_caps_options = AppiumOptions()

    env_variables = take_env_variables()

    desired_caps_options.set_capability('platformName', f'{env_variables["platformName"]}')
    desired_caps_options.set_capability('platformVersion', f'{env_variables["platformVersion"]}')
    desired_caps_options.set_capability('deviceName', f'{env_variables["deviceName"]}')
    desired_caps_options.set_capability('automationName', f'{env_variables["automationName"]}')

    driver = webdriver.Remote('http://localhost:4723', options=desired_caps_options)
    return driver


def take_env_variables():
    with open('env_file/device_env.json', 'r') as file:
        data = json.load(file)

    return data
