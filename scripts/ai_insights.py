import pandas as pd
from openai import OpenAI
from config.settings import OPENAI_API_KEY
from config.logging_config import logger
from utils.helpers import load_csv_data

def generate_insights():
    if not OPENAI_API_KEY:
        return "OPENAI_API_KEY is not configured. Add it to your local .env file to enable AI insights."
    try:
        df = load_csv_data("processed_sales.csv", "processed")
    except FileNotFoundError:
        return "Processed sales data is missing. Run the ETL pipeline first."
    summary = df.groupby("Region")["Revenue"].agg(["sum", "mean", "count"]).round(2).to_string()
    prompt = "Analyze these sales metrics. Provide an executive summary, notable trends, and actionable recommendations. Do not invent data.\n\n" + summary
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a concise business data analyst."}, {"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content or "No insights were returned."
    except Exception as exc:
        logger.exception("AI insight generation failed")
        return f"Unable to generate insights: {exc}"
