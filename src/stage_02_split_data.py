import logging
import re
from src.utils.all_utils import read_yaml, create_dir, save_local_df,create_log_dir
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging


def split_and_save_data(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_loacl_dir = config['artifacts']['raw_loacl_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    file_path = os.path.join(artifacts_dir,raw_loacl_dir,raw_local_file)       

    # Reading the csv file stored in local
    df = pd.read_csv(file_path)

    # train and test data split
    train, test = train_test_split(df, test_size=params['base']['test_size'], random_state=params['base']['random_state'])

    split_data_dir = config['artifacts']['split_data']
    create_dir([os.path.join(artifacts_dir,split_data_dir)])

    # saving the train and test data 
    train_data_filename = config['artifacts']['train']
    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)

    test_data_filename = config['artifacts']['test']
    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_filename)

    for data,data_path in (train,train_data_path),(test,test_data_path):
        save_local_df(data,data_path)


   




if __name__=="__main__":
    args = argparse.ArgumentParser()

    create_log_dir()

    args.add_argument("--config","-c",default = "config/config.yaml")
    args.add_argument("--params","-p",default = "params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(" >>>>> Stage 02 started")
        split_and_save_data(config_path = parsed_args.config, params_path = parsed_args.params)
        logging.info(" >>>>> Stage 02 completed")
    except Exception as e:
        logging.exception(e)
        raise e

