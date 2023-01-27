# -*- coding: utf-8 -*-
import os
import shutil

import pytest
from browser import Browser
from logger import set_logger
from project import base_url, reports_path


def pytest_addoption(parser):
    parser.addoption('--console-log', type=str, choices=['TRACE', 'DEBUG', 'INFO'], default='DEBUG',
                     dest='console_log', help='Set console log level [TRACE, DEBUG, INFO]')


# Fixture for Chrome
@pytest.fixture
def chrome_driver_init(request, url=base_url):
    logger = set_logger(request.config.getoption('console_log'))
    logger.debug(f'Reports path: {reports_path}')
    logger.info('Setup chromedriver')
    chrome_driver = Browser.get_chrome_driver()
    logger.info(f'Open url: {url}')
    chrome_driver.get(url)
    request.cls.driver = chrome_driver
    request.cls.logger = logger
    yield
    chrome_driver.quit()
