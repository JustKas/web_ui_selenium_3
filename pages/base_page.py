# -*- coding: utf-8 -*-

class BasePage:
    """
    This is the base class for Pages
    Please put here common methods
    """
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
