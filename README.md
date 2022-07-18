
## wokflow -
UCI ML Repository  ---> load and save ---> split data ---> train ---> evaluate

# STEPS:

## STEP 01: create and activate conda environment

```bash
conda create -n dvc-ml python=3.7 -y
source activate base
conda activate dvc-ml
```
## STEP 02: create a setup file
```bash
touch setup.py
```

paste the below content in the setup.py file and make the necessary changes as per your user ID-

```python
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Sampath",
    description="DVC practice",
    long_description=long_description,
    long_description_type="text/markdown",
    url="https://github.com/sampathsvskr/dvc-ML-demo",
    author_email="sampathkumarreddysvskr@gmail.com",
    packages=['src'],    
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]


)
```


## STEP 03: create requirement file and install dependencies
```bash
touch requirements.txt
pip install -r requirements.txt
```
content of requirements.txt - Refer the reference repository

## STEP 04: initialize dvc
```bash
dvc init
```

## STEP 05: create the basic directory structure

```bash
mkdir -p src/utils config
```
## STEP 06: create the config file 
```bash
touch config/config.yml
```
content of config.yml - 

```yaml

data_source: http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

artifacts: 
  artifacts_dir: artifacts
  raw_local_dir: raw_local_dir
  raw_local_file: data.csv


```


## STEP 07: create the stage 01 python file and all_utils file:
```bash
touch src/stage_01_load_save.py src/utils/all_utils.py
```
content of both these files can be refererd from the reference given


## STEP 8: create the dvc.yaml file and add the stage 01:
```bash
touch dvc.yaml
```

content of dvc.yaml file -
```yaml
stages:
  load_data:
    cmd: python src/stage_01_load_save.py --config=config/config.yaml
    deps:
      - src/stage_01_load_save.py
      - src/utils/all_utils.py
      - config/config.yaml
    outs:
      - artifacts/raw_local_dir/data.csv
```

## STEP 9: run the dvc repro command
```bash
dvc repo
```

## STEP 10: push the changes to remote repository
```bash
git add .
git commit -m "stage 01 added"
git push origin main
```