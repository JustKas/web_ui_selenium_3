# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class HomePageLocators(BaseLocators):
    """
    This is the HomePageLocators class
    Please put here locators/methods for Home Page only
    """
    search_btn_xpath = (By.XPATH, '//button[@aria-label="Search"]')
