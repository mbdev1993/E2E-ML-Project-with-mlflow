import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logger.warning(f"Column '{col}' not found in schema.")
                    break

            with open(self.config.STATUS_File, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.error(f"Error during file validation: {e}")
            return False
