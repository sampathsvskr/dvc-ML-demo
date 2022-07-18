import yaml
import os

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)

    return content


def create_dir(dires: list):
    for dir in dires:
        os.makedirs(dir,exist_ok=True)
        