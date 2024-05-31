from _datetime import datetime
import os

import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from _pytest.config import ExitCode


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        # Instantiate EdgeService with EdgeChromiumDriverManager
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("Edge driver invoked successfully......")

    elif browser == "firefox":
        # Instantiate FirefoxService with GeckoDriverManager
        service = FireFoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("Firefox driver invoked successfully......")

    else:
        # Instantiate ChromeService with ChromeDriverManager
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("By default chrome driver invoked successfully......")
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', help='Specify the browser for test execution')

# Add the '--num-workers' option for parallel testing
# parser.addoption('--num-workers', action='store', default=1, help='Number of worker processes for parallel testing')

# Override pytest_configure to configure parallel testing with xdist
# def pytest_configure(config):
#     # Check if xdist is enabled
#     if hasattr(config, 'workerinput'):
#         # Set the number of workers based on the '--num-workers' option
#         num_workers = config.getoption('--num-workers')
#         config.workerinput['numprocesses'] = num_workers

# This function will be executed after all tests have finished running
# def pytest_sessionfinish(session, exitstatus):
#     # Check if xdist was used
#     if hasattr(session.config, 'workerinput'):
#         # If any worker process failed, set the exit code to 1
#         if exitstatus == ExitCode.TESTS_FAILED or exitstatus == ExitCode.INTERRUPTED:
#             session.exitstatus = 1


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


#report generation

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["Tester"] = "Harshit"

    if exitstatus == ExitCode.TESTS_FAILED or exitstatus == ExitCode.INTERRUPTED:
        session.exitstatus = 1


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.abspath(os.curdir+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M_%S")+
                                              ".html"))