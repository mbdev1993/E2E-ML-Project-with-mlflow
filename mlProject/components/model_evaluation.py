from utils.common import save_json
import pandas as pd
import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from pathlib import Path
import mlflow
from urllib.parse import urlparse
import numpy as np
from mlProject.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, predicted):
        r2 = r2_score(actual, predicted)
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        return r2, rmse, mae
    
    def log_into_mlflow(self):
        Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_data)

        test_x = test_data.drop(self.config.target_column, axis=1) 
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (r2, rmse, mae) = self.eval_metrics(test_y, predicted_qualities)

            scores = {"r2_score": r2,"rmse": rmse,
                "mae": mae
            }
            
            Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("r2_score", r2)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetWineModel")
            else:
                mlflow.sklearn.log_model(model, "model")