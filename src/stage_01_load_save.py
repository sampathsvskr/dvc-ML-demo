from src.utils.all_utils import read_yaml, create_dir, save_local_df
import argparse
import pandas as pd
import os


def get_data(config_path):
    config=read_yaml(config_path)
    
    df=pd.read_csv(config['data_source'],sep=";")
    
    artifacts_dir= config['artifacts']['artifacts_dir']
    raw_loacl_dir=config['artifacts']['raw_loacl_dir']
    raw_local_file=config['artifacts']['raw_local_file']

    raw_local_dir_path= os.path.join(artifacts_dir,raw_loacl_dir)    
    create_dir([raw_local_dir_path])
    
    raw_local_file_path= os.path.join(raw_local_dir_path,raw_local_file)

    save_local_df(df,raw_local_file_path, sep=",",index=False)




if __name__=="__main__":
    args=argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_args=args.parse_args()

    get_data(config_path=parsed_args.config)

