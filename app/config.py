import os
import yaml
from pymongo import MongoClient


class Config:
    def __init__(self):
        env = os.getenv('FLASK_ENV', 'development')
        self.config_file = f'config_{env}.yml'  # Directly specifying the path
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_kafka_config(self):
        return self.config.get('kafka', {})

    def get_mongo_client(self):
        mongo_config = self.config['mongo']
        return MongoClient(mongo_config['uri'])[mongo_config['db']]

    def get(self, key, default=None):
        return self.config.get(key, default)
