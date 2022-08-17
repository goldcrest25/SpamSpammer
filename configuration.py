from ast import parse
import configparser
from turtle import fd

# Configuration
class Configuration:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("config.ini")
        default = parser["DEFAULT"]
        print(default)
        self.endpoint = default["endpoint"]
        self.apikey = default["apikey"]
