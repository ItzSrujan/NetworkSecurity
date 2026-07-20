import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
from pymongo.mongo_client import MongoClient
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = MongoClient(MONGO_DB_URL, tlsCAFile = ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == "__main__":
    FILE_PATH = r"D:\Data Science\ML Projects - 2\Network Security\Network_Data\phisingData.csv"
    DATABASE = "SrujanAI"
    Collection = "NetworkData"
    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json(file_path = FILE_PATH)
    print(records)
    no_of_records = network_obj.insert_data_to_mongodb(records=records, database = DATABASE, collection = Collection)
    print(no_of_records)