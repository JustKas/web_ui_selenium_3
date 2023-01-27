# -*- coding: utf-8 -*-
import pytest
from hamcrest import assert_that, equal_to

from pages.home_page import HomePage


@pytest.mark.usefixtures("chrome_driver_init")
class TestTitleChrome:

    def test_title(self):
        expected_title = 'Fast and reliable end-to-end testing for modern web apps | Playwright'
        self.logger.info('Verify title')
        assert_that(self.driver.title, equal_to(expected_title))
        # home_page = HomePage(self.driver, self.logger)
        # home_page.click_search_btn()
