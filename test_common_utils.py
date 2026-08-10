import pandas as pd

from src.utils.common import CommonUtils

df = CommonUtils.load_csv(
    "data/raw/users.csv"
)

print(df.head())

CommonUtils.save_csv(
    df.head(),
    "artifacts/sample_users.csv"
)

print("CSV Saved Successfully")