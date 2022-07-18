from venv import create
from src.utils.all_utils import read_yaml, create_dir, save_local_df, save_reports
import argparse
import pandas as pd
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import numpy as np


def evaluate_metrics(actual_values, predicted_values):
    rmse = np.sqrt(mean_squared_error(actual_values,predicted_values))
    mae = mean_absolute_error(actual_values,predicted_values)
    r2 = r2_score(actual_values,predicted_values)

    return rmse, mae, r2


def evaluate(config_path):
    config=read_yaml(config_path)
    
    artifacts_dir= config['artifacts']['artifacts_dir']
    split_data_dir= config['artifacts']['split_data']
    test_data_filename= config['artifacts']['test']

    test_data_path=os.path.join(artifacts_dir,split_data_dir,test_data_filename)

    test_data=pd.read_csv(test_data_path)
    
    test_y=test_data["quality"]
    test_x=test_data.drop("quality", axis=1)

    
    model_dir= config['artifacts']['model_dir']   
    model_filename= config['artifacts']['model_file']
    model_path= os.path.join(artifacts_dir,model_dir, model_filename)

    model= joblib.load(model_path)

    pred_values=model.predict(test_x)

    rmse, mae, r2 = evaluate_metrics(test_y,pred_values)

    scores_dir=config['artifacts']['reports_dir']
    scores_dir_path = os.path.join(artifacts_dir,scores_dir)
    create_dir([scores_dir_path])

    scores_filename = config['artifacts']['reports_file']

    scores_path = os.path.join(scores_dir_path, scores_filename)

    scores = {
        "rmse": rmse,
        "mae": mae,
        "r2": r2
    }
    save_reports(scores=scores,report_path=scores_path)

    

    
   




if __name__=="__main__":
    args=argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")   

    parsed_args=args.parse_args()

    evaluate(config_path=parsed_args.config)

