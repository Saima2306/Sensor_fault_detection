from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

df = pd.read_csv('/home/saima/Desktop/ineuron/Day07_sensor_fault_detection/Sensor_fault_detection/artifact/2022-12-24 12:28/data_ingestion/feature_store/sensor_data.csv')
train,test = train_test_split(df,test_size=0.2,train_size=0.8,shuffle=True)
# print(train.shape,test.shape)
train.to_csv("/home/saima/Desktop/ineuron/Day07_sensor_fault_detection/Sensor_fault_detection/artifact/2022-12-24 12:39/data_ingestion/ingested/train.csv",index= False,header=True)
test.to_csv("/home/saima/Desktop/ineuron/Day07_sensor_fault_detection/Sensor_fault_detection/artifact/2022-12-24 12:39/data_ingestion/ingested/test.csv",index= False,header=True)