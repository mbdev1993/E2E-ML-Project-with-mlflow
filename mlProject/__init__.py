# importing
import os
import sys
import logging

# ASCII time | log label - information log or bug log | which module name | message

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# creating a log folder and a file name is running_log.log
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # Method1: execute all my log data in the folder and file 
        logging.StreamHandler(sys.stdout) # Method2: to display log on terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")
 

