import logging
import os


class logGen:
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir + '\\logs\\automation.log')
        # path = "E:/PythonLearning/OpenCart_Project_V1/logs\\automation.log"
        logging.basicConfig(filename=path,
                            format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%m/%d/%y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger