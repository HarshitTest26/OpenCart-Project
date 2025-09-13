from datetime import datetime
import os
import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from _pytest.config import ExitCode


@pytest.fixture()
def setup(browser):
    """
    Sets up the WebDriver for the specified browser, with headless mode for Chrome.
    """
    if browser == "edge":
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("Edge driver invoked successfully......")
    elif browser == "firefox":
        service = FireFoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("Firefox driver invoked successfully......")
    else:
        # Configure Chrome to run in headless mode for server environments like Jenkins
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("By default chrome driver invoked successfully in headless mode......")

    yield driver
    driver.quit()


def pytest_addoption(parser):
    """
    Adds a command-line option to specify the browser.
    """
    parser.addoption('--browser', action='store', default='chrome', help='Specify the browser for test execution')


@pytest.fixture()
def browser(request):
    """
    Fixture to get the browser option from the command line.
    """
    return request.config.getoption('--browser')


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Adds custom metadata and handles exit status.
    """
    session.config.stash[metadata_key]["Tester"] = "Harshit"
    if exitstatus == ExitCode.TESTS_FAILED or exitstatus == ExitCode.INTERRUPTED:
        session.exitstatus = 1


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Dynamically sets the path for the HTML report.
    """
    report_dir = os.path.join(os.curdir, "reports")
    os.makedirs(report_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    report_name = f"{timestamp}.html"
    report_path = os.path.abspath(os.path.join(report_dir, report_name))
    config.option.htmlpath = report_path

