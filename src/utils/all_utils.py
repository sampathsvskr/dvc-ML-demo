import yaml
import os
import json

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)

    return content


def create_dir(dires: list):
    for dir in dires:
        os.makedirs(dir,exist_ok=True)

    print(f"directory created at {dir}")


def save_local_df(data, data_path, sep=",",index=False):
    data.to_csv(data_path,sep=sep, index=index )

    print(f"data saved at {data_path}")


def save_reports(scores: dict, report_path: str):
    with open(report_path, "w") as f:
        json.dump(scores,f,indent=4)

    print(f"reports are saved at {report_path}")
