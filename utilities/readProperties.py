import configparser   #pre-defined in python
import os

#we created config object for RawConfigParser class present in configparser module just like driver instance/object
config = configparser.RawConfigParser()
#To read config.ini we have specified the location
config.read(os.path.abspath(os.curdir) + '\\configurationFiles\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('CommonTestData', 'baseurl')
        return url

    @staticmethod
    def getEmail():
        email = config.get('CommonTestData', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('CommonTestData', 'password')
        return password

