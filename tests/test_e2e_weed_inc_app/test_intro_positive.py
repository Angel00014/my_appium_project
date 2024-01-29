import pytest
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from appium.webdriver.common.touch_action import TouchAction


class Test:

    @pytest.fixture(autouse=True)
    def driver_fixture(self, appium_driver):
        self.driver = appium_driver
        yield

    def test_start(self):
        device = self.driver

        device.keyevent(3)

        start_x = 400  # середина экрана по горизонтали
        start_y = 1000  # точка внизу экрана
        end_x = 400  # середина экрана по горизонтали
        end_y = 200  # точка вверху экрана
        duration = 500  # длительность свайпа

        device.swipe(start_x, start_y, end_x, end_y, duration)

        app_icon = device.find_element(by="xpath", value="//android.widget.TextView[@text=\"Weed Inc\"]")

        app_icon.click()

        system_window_agree = WebDriverWait(device, 90).until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.LinearLayout[@resource-id=\"android:id/parentPanel\"]")))

        system_window_agree = device.find_element(by="xpath",
                                                  value="//android.widget.LinearLayout[@resource-id=\"android:id/parentPanel\"]")

        system_window_agree_button = device.find_element(by="xpath",
                                                         value="//android.widget.Button[@resource-id=\"android:id/button1\"]")

        system_window_agree_button.click()

        system_window_allow = WebDriverWait(device, 90).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//android.widget.LinearLayout[@resource-id=\"com.android.permissioncontroller:id/grant_dialog\"]")))

        system_window_allow_button = device.find_element(by="xpath",
                                                         value="//android.widget.Button[@resource-id=\"com.android.permissioncontroller:id/permission_allow_button\"]")

        system_window_allow_button.click()

        # до open
        assert system_window_agree is not None
        assert system_window_allow is not None

    def test_introduction(self):
        device = self.driver

        game_window_intro = WebDriverWait(device, 90).until(EC.presence_of_element_located(
            (By.XPATH, "//android.view.View[@content-desc=\"Game view\"]")))

        # touch = ActionChains(device)
        # touch.move_by_offset(1315, 528).click().perform()

        touch = TouchAction(device)
        touch.tap(x=1315, y=528).perform()

        game_window_main = WebDriverWait(device, 90).until(EC.presence_of_element_located(
            (By.XPATH, "//android.view.View[@content-desc=\"Game view\"]")))

        game_window_main = device.find_element(by="xpath", value="//android.view.View[@content-desc=\"Game view\"]")

        assert game_window_main is not None

    def test_quit(self):
        device = self.driver
        device.keyevent(3)

        device.terminate_app("com.metamoki.weed")

        device.execute_script('mobile: shell', {'command': 'pm clear com.metamoki.weed'})
