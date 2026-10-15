import pandas as pd
from database.database import get_engine
from utils.helpers import load_csv_data
from config.logging_config import logger

def load_to_mysql():
    logger.info("Loading processed data to MySQL...")
    try:
        df = load_csv_data("processed_sales.csv", "processed")
    except FileNotFoundError:
        logger.error("Processed data not found. Run feature_engineering.py first.")
        return
    engine = get_engine()
    if engine is None:
        logger.error("Cannot connect to database. Check MySQL and .env credentials.")
        return
    try:
        df.to_sql("sales", con=engine, if_exists="replace", index=False)
        logger.info(f"Loaded {len(df)} rows into the sales table.")
    except Exception as exc:
        logger.exception(f"Failed to load data: {exc}")

if __name__ == "__main__":
    load_to_mysql()
