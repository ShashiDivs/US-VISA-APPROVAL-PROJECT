import os
from us_visa.constants import DATABASE_NAME,MONGODB_URL_KEY
from exception import USvisaException
from logger import logging
import pymongo
import certifi


ca = certifi.where()


class MongoDBClient:
    client = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
                logging.info("MongoDb Connection Succesful")
        except Exception as e:
            raise USvisaException(e,sys) from e