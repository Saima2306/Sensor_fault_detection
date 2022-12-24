import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

# defining common constant variables for training pipeline(for constant, all capitals)
TARGET_COLUMN = "class"
PIPELINE_NAME:str= "sensor"
ARTIFACT_DIR:str = "artifact" #output stored 
FILE_NAME:str = "sensor.csv"

TRAIN_FILE_NAME: str = "train.csv" # training file
TEST_FILE_NAME:str = "test.csv" # testing file

PROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml") # schema information
SCHEMA_DROP_COLS ="drop_columns" # information about those columns that needs to be dropped in the project

#defining data ingestion related constants with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2