import pandas as pd
from utils.helpers import load_csv_data, save_csv_data
from config.logging_config import logger

def clean_sales_data():
    logger.info("Starting data cleaning...")
    try:
        df = load_csv_data("raw_sales.csv", "raw")
    except FileNotFoundError:
        logger.error("Raw data not found. Run generate_data.py first.")
        return
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)
    df = df.dropna(subset=["OrderID", "OrderDate", "Quantity", "UnitPrice"])
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    df["Quantity"] = df["Quantity"].astype(int)
    save_csv_data(df, "cleaned_sales.csv", "cleaned")
    logger.info("Data cleaning complete.")

if __name__ == "__main__":
    clean_sales_data()
