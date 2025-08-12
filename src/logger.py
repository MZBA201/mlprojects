# This brings in Python’s built-in logging module
# which lets you log messages (like errors, warnings, or general info)
import logging
# This allows you to interact with the operating system
# for example, to make folders or join file paths.
import os
# This allows you to get the current date and time
# useful for naming log files uniquely.
from datetime import datetime

# Create a log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path to the logs folder (just the folder)
logs_folder = os.path.join(os.getcwd(), "logs")

# Make sure the logs folder exists
os.makedirs(logs_folder, exist_ok=True)

# Final path to the log file inside the logs folder
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# This configures the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)




