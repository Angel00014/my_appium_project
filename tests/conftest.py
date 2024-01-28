from appium_utils import initialize_appium_driver

import pytest


@pytest.fixture(scope="function")
def appium_driver(request):
    # platformName = request.param('platformName')
    # platformVersion = request.param.get("platformVersion")
    # deviceName = request.param.get("deviceName")
    # automationName = request.param.get("automationName")
    driver = initialize_appium_driver()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
