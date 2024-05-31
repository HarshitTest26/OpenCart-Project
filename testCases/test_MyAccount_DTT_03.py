import pytest
import time
from pageObjects import HomePage
from pageObjects import LoginPage
from pageObjects import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils


class Test_DTT:
    baseURL = ReadConfig.getApplicationUrl()
    log = logGen.loggen()
    log.info("** Logging started **")

