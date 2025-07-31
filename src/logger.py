# This brings in Python’s built-in logging module
# which lets you log messages (like errors, warnings, or general info)
import logging
# This allows you to interact with the operating system
# for example, to make folders or join file paths.
import os
# This allows you to get the current date and time
# useful for naming log files uniquely.
from datetime import datetime

# This line creates a log file name based on the current date and time.
# very time program runs, it creates a new log file with a unique name.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# os.getcwd() gives the current directory
# os.path.join(...) builds a path like
# Put the log file inside a folder called logs in the current working directory
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
# This creates the full folder path 
# (including logs) if it doesn’t exist already.
os.makedirs(logs_path, exist_ok=True)
# This combines the folder path and the log file name into a full file path.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# This configures the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


