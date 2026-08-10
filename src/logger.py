import logging
import os
from datetime import datetime
from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Logs Folder
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Log File Name
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

LOG_FILE_PATH = LOG_DIR / LOG_FILE

# Logger Configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)
