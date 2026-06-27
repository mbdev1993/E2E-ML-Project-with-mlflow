# util is the place where we keep those programs which will be used frequently

# for example: to read yaml file in all the components, so inspite of writting 
# read yaml function in every component - we can simply create a common 
# program which we can call multiple times

import os
from box.exceptions import BoxValueError #exception handling for box
import yaml # to read yaml file
from mlProject import logger 
import json
import joblib
from ensure import ensure_annotations # annotation to check the type of input and output of function
from box import ConfigBox
from pathlib import Path
from typing import Any

# explain why we created real_yaml function? 
# Because we want to read yaml file in all the components, 
# so inspite of writting read yaml function in every component - 
# we can simply create a common program which we can call

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox: # to fetch data from an object by converting a list into object
    """reads a yaml file and returns a ConfigBox object"""
    # why using configbox? because it will give us 
    # the dictionary in the form of object so we can access it like 
    # object.property
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, "r") as f:
        content = json.load(f)
        logger.info(f"json file: {path} loaded successfully")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save any data type as binary file"""
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file: {path} saved successfully")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load any binary file"""
    data = joblib.load(filename=path)
    logger.info(f"binary file: {path} loaded successfully")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB"""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def get_files_from_directory(path: Path, extension: str) -> list:
    """get all files with a specific extension from a directory"""
    return [file for file in os.listdir(path) if file.endswith(extension)]

