from ast import parse
import configparser
from turtle import fd

# Configuration
class Configuration:
    def __init__(self):
        # Get default settings…
        parser = configparser.ConfigParser()
        parser.read("config.ini")
        default = parser["DEFAULT"]

        # …and configured settings
        self.endpoint = default["endpoint"]
        self.apikey = default["apikey"]
        self.spam_count = int(default["spam-count"])
