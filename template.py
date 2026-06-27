import os
from pathlib import Path
import logging

# I want to see log in my terminal | it will be information level log | with timestamp and message

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

# In the folder SRC, the below project and other components will be created
project_name = "mlProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    # Core Application Package
    f"{project_name}/__init__.py",
    # Components & Pipelines
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/pipelines/__init__.py",
    f"{project_name}/pipelines/training_pipeline.py",
    f"{project_name}/pipelines/prediction_pipeline.py",
    # Added core modules with constructors
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/training_pipeline/__init__.py",
    # System Modules
    f"{project_name}/logger.py",
    f"{project_name}/exception.py",
    "tests/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
# path is used to handle forward/backward slash
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
