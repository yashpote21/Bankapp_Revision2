import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def GetUsername():
        return config.get('login data', 'username')

    @staticmethod
    def GetPassword():
        return config.get('login data', 'password')

    @staticmethod
    def GetSearchUsername():
        return config.get('search user', 'username')
