# E2E-ML-Project-with-mlflow
ML project with mlflow

## Workflows
1. Update config.yaml 
2. Update schema.yaml # data columns with their data types
3. Update params.yaml # parameters that'll be using in the project
4. Update the entity # folder entity
5. Update the configuration manager in project(mlProject) config
6. Update the components # Data ingestion/transformation , etc
7. Update the pipeline # Training pipeline and prediction pipeline
8. Update the main.py
9. Update the app.py # replaced it, earlier it was dvc.yaml 



# How to run?

### Steps:
Clone the repository

'''bash 
https://github.com/mbdev1993/E2E-ML-Project-with-mlflow


### step-1 : create a conda environment after opening the repository

''' bash
conda create -m venv python = 3.8 -y
....

'''bash
conda activate venv
...

###  step-2 install the requirements
''''bash
pip install -r requirements.txt
'''

'''bash
python app.py
...

Now,
'''bash
open up your local host and port
...

## ML flow
[Documentation] https://mlflow.org/docs/latest/

### cmd
- mlflow ui

### dagshub
[datshub] https://dagshub.com/

MLFLOW_TRACKING_URI = https://dagshub.com/mbdev1993/E2E-ML-Project-with-mlflow.mlflow
MLFLOW_TRACKING_USERNAME =
MLFLOW_TRACKING_PASSWORD =
python script.py

import dagshub
dagshub.init(repo_owner='mbdev1993', repo_name='E2E-ML-Project-with-mlflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

run this to export as env variables:

''' bash
export MLFLOW_TRACKING_URI=https://dagshub.com/mbdev1993/E2E-ML-Project-with-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=mbdev1993

export MLFLOW_TRACKING_PASSWORD=8244e1267a62c7dfa8cac5777c4b627e5fb48ea0

dvc remote modify origin --local auth basic
dvc remote modify origin --local user mbdev1993
dvc remote modify origin --local password 8244e1267a62c7dfa8cac5777c4b627e5fb48ea0



