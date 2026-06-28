from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) 
# to define vairables, we use dataclass decorator. frozen=True means that 
# the values of the variables cannot be changed after initialization.

class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path