import logging

class Log_Class:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        file = logging.FileHandler('.\\Logs\\Bankapp_Revision2.log')
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")

        file.setFormatter(logformat)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger