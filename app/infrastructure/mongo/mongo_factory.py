from app.config import Config
from pymongo import MongoClient


class MongoFactory:
    @staticmethod
    def create():
        config = Config().get_mongo_client()
        return MongoClient(config['uri'])[config['dbname']]
