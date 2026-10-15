import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config.settings import REPORTS_DIR
from utils.helpers import load_csv_data
from config.logging_config import logger

def run_eda():
    try:
        df = load_csv_data("processed_sales.csv", "processed")
    except FileNotFoundError:
        logger.error("Processed data not found. Run feature_engineering.py first.")
        return
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="Region", y="Revenue", estimator=sum, errorbar=None)
    plt.title("Total Revenue by Region")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "revenue_by_region.png")
    plt.close()
    monthly = df.groupby(["Year", "Month"])["Revenue"].sum().reset_index()
    monthly["Date"] = pd.to_datetime(monthly["Year"].astype(str) + "-" + monthly["Month"].astype(str) + "-01")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly, x="Date", y="Revenue", marker="o")
    plt.xticks(rotation=45)
    plt.title("Monthly Revenue Trend")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "monthly_revenue_trend.png")
    plt.close()
    numeric = df.select_dtypes(include="number")
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "correlation_heatmap.png")
    plt.close()
    logger.info(f"EDA complete. Visualizations saved to {REPORTS_DIR}")

if __name__ == "__main__":
    run_eda()
