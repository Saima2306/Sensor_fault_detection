from sensor.configuration.mongoDB_connection import MongoDBClient
import os
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    # mongo_db_client = MongoDBClient()
    # print("collection name:",mongo_db_client.database.list_collection_names()) # read all the collections from database
    # training_pipeline_config = TrainingPipelineConfig()
    # data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    # print(data_ingestion_config.__dict__)
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()