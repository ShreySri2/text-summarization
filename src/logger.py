import logging
import os
from datetime import datetime

TIME = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
print(TIME)
LOG_FILE = f"{TIME}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)

# Test for logging
# if __name__ == "__main__":
#     logging.info("logging has started")