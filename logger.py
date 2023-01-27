# -*- coding: utf-8 -*-
import os
import shutil
import sys
import loguru

from project import reports_path

LOG_FORMAT = '<level>{time: YYYY-MM-DD HH: mm: ss. SSS} | {level} | {module}/{function} |</level> {message}'


def set_logger(console_level: str):
    loguru.logger.remove()
    if os.path.exists(reports_path):
        shutil.rmtree(reports_path)
    test_logger = loguru.logger
    test_logger.add(sys.stdout, level=console_level, enqueue=True, format=LOG_FORMAT)
    test_logger.add(os.path.join('reports', 'full_tests.log'), level='TRACE', enqueue=True, format=LOG_FORMAT)
    test_logger.info(f'Logger is start with log-level: {console_level}')
    return test_logger
