from pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline
from pipelines.stage_04_model_trainer import ModelTrainerPipeline
from pipelines.stage_05_model_evaluation import ModelEvaluationPipeline

from mlProject import logger
from mlProject.components.data_ingestion import DataIngestion

logger.info("Welcome to our custom Logging")
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj =   DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


