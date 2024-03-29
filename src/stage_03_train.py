from src.utils.all_utils import read_yaml, create_dir, save_local_df, create_log_dir
import argparse
import pandas as pd
import os
from sklearn.linear_model import ElasticNet
import joblib
import logging


def train_data(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    
    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data']
    train_data_filename = config['artifacts']['train']

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)

    # reading train data
    train_data = pd.read_csv(train_data_path)
    
    train_y = train_data["quality"]
    train_x = train_data.drop("quality", axis=1)

    # model creation
    lr=ElasticNet(
                  alpha = params["model_params"]["ElasticNet"]["alpha"],
                  l1_ratio = params["model_params"]["ElasticNet"]["l1_ratio"], 
                  random_state = params['base']['random_state']
                  )
    lr.fit(train_x,train_y)

    model_dir = config['artifacts']['model_dir']
    model_dir_path = os.path.join(artifacts_dir,model_dir)
    create_dir([model_dir_path])
    
    # saving the model 
    model_filename = config['artifacts']['model_file']
    model_path = os.path.join(model_dir_path, model_filename)

    joblib.dump(lr,model_path)

  


if __name__=="__main__":

    create_log_dir()

    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default = "config/config.yaml")
    args.add_argument("--params","-p",default = "params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(" >>>>> Stage 03 started")
        train_data(config_path = parsed_args.config, params_path = parsed_args.params)
        logging.info(" >>>>> Stage 03 completed")
    except Exception as e:
        logging.exception(e)
        raise e

