from pipelines.data_ingestion_pipeline import DataIngestionTrainingPipeline

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

