# -*- coding: utf-8 -*-
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    This is the HomePage object class
    Please put here methods for Home Page only
    """

    def click_search_btn(self):
        self.logger.info('Click on Search button')
        self.driver.find_element(*HomePageLocators.search_btn_xpath).click()
