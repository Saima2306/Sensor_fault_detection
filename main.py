from sensor.configuration.mongoDB_connection import MongoDBClient

if __name__ == "__main__":
    mongo_db_client = MongoDBClient()
    print(mongo_db_client.database.list_collection_names()) # read all the collections from database