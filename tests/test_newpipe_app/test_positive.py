from itertools import count

import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        app_icon = device.find_element(by="xpath", value="//android.widget.TextView[@text=\"N MusicPlyaer\"]")

        app_icon.click()

        wait_system_window_allow = WebDriverWait(device, 90).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//android.widget.LinearLayout[@resource-id=\"com.android.permissioncontroller:id/grant_dialog\"]")))

        system_window_allow_button = device.find_element(by="xpath",
                                                         value="//android.widget.Button[@resource-id=\"com.android.permissioncontroller:id/permission_allow_button\"]")

        system_window_allow_button.click()

    def test_get_list(self):
        device = self.driver
        wait_component_list_application = False

        wait_component_list = WebDriverWait(device, 90).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//androidx.recyclerview.widget.RecyclerView[@resource-id=\"com.newpipemusic.downloader:id/items_list\"]")))

        if wait_component_list is not None:
            wait_component_list_application = True

        component_list = device.find_element(by="xpath",
                                             value="//androidx.recyclerview.widget.RecyclerView[@resource-id=\"com.newpipemusic.downloader:id/items_list\"]")

        component_list_items = component_list.find_elements(by="xpath", value=".//*")
        component_list_count = len(component_list_items)

        assert wait_component_list_application is True
        assert component_list_count == 49

    def test_quit(self):
        device = self.driver
        device.keyevent(3)

        device.terminate_app("com.newpipemusic.downloader")

        device.execute_script('mobile: shell', {'command': 'pm clear com.newpipemusic.downloader'})
