from pathlib import Path

# ==============================
# Project Root Directory
# ==============================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==============================
# Data Directories
# ==============================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ==============================
# Models
# ==============================

MODELS_DIR = PROJECT_ROOT / "models"

# ==============================
# Artifacts
# ==============================

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

# ==============================
# Logs
# ==============================

LOGS_DIR = PROJECT_ROOT / "logs"

# ==============================
# MLflow
# ==============================

MLRUNS_DIR = PROJECT_ROOT / "mlruns"

# ==============================
# Create folders automatically
# ==============================

for folder in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    ARTIFACTS_DIR,
    LOGS_DIR,
    MLRUNS_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)