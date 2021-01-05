# -*- coding: utf-8 -*-
# conftest.py
#
#-----------------------------------------------------------------
# pytest - conftest.py
# tests
#   ratings/*.csv
#   io/
#       test_xxx.py
#   conftest.py
#-----------------------------------------------------------------
# pip install pytest-html
# pytest --html=report.html
import os
import datetime
import pytest
import logging

class SystemLoggerFactory:

    @staticmethod 
    def create_stream_logger(logger_name):
        # Create Logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
     
        formatter = logging.Formatter('[%(name)s|%(filename)s:%(lineno)s] %(asctime)s] - %(levelname)s - %(message)s')

        # Create Handlers
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamHandler.setFormatter(formatter)
     
        logger.addHandler(streamHandler)
        return logger

def pytest_configure(config):
    # core is the htmlpath passed in each test change parameter
    if config.getoption('--html'):
        path_list = list(os.path.split(config.option.htmlpath))
        #path_list.insert(-1, datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        path_list.insert(-2, 'reports')
        #path_list.insert(-1, datetime.datetime.now().strftime('%Y%m%d_%H%M'))
        config.option.htmlpath = os.path.join(*tuple(path_list))

def pytest_html_report_title(report):
    report.title = "Team10x TDD Reports"

def pytest_addoption(parser):
    parser.addoption("--logname", action="store", default="test_logger")

@pytest.fixture
def logger(pytestconfig):
    name = pytestconfig.getoption("logname")
    test_logger = SystemLoggerFactory.create_stream_logger(name)
    return test_logger


