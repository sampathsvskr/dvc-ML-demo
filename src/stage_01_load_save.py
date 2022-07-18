from src.utils.all_utils import read_yaml, create_dir, save_local_df,create_log_dir
import argparse
import pandas as pd
import os
import logging



def get_data(config_path):
    config = read_yaml(config_path)
    
    # reading data from the source
    df = pd.read_csv(config['data_source'],sep=";")
    
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_loacl_dir = config['artifacts']['raw_loacl_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    # directory creation to store the data in local
    raw_local_dir_path = os.path.join(artifacts_dir,raw_loacl_dir)    
    create_dir([raw_local_dir_path])
    
    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)

    # saving the data 
    save_local_df(df,raw_local_file_path, sep=",",index=False)




if __name__=="__main__":

    create_log_dir()

    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default = "config/config.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(" >>>>> Stage 01 started")
        get_data(config_path = parsed_args.config)
        logging.info(" >>>>> Stage 01 completed")
    except Exception as e:
        logging.exception(e)
        raise e

