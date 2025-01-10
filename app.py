from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

# Import the modules used in main.py
from src.data.loader import DataLoader
from src.models.machine_learning import run_forecasting_pipeline, set_seeds
from src.models.statistical import run_statistical_pipeline
from src.utils.logger import setup_logger

import pandas as pd

app = FastAPI()

def prepare_data(price_df):
    """Prepare data for forecasting (mimics the function in main.py)."""
    stats_df = price_df.copy()
    stats_df = stats_df.rename(columns={'Rice, Viet Namese 5%': 'y', 'Date': 'ds'})
    stats_df['unique_id'] = 'stats'
    stats_df = stats_df[['ds', 'y', 'unique_id']]
    stats_df = stats_df.reset_index(drop=True)
    stats_df['y'] = stats_df['y'].fillna(method='ffill').fillna(method='bfill')
    return stats_df

@app.get("/forecast")
def forecast(h: int = Query(12, description="Forecast horizon")):
    """
    Returns date + future forecast (both statistical and ML).
    """
    logger = setup_logger()
    logger.info("Starting FastAPI forecast endpoint")

    set_seeds()
    loader = DataLoader()
    price_df = loader.load_price_data()
    stats_df = prepare_data(price_df)

    statistical_results = run_statistical_pipeline(
        stats_df,
        forecast_horizon=h,
        step_size=1,
        n_windows=36
    )
    ml_results = run_forecasting_pipeline(
        stats_df,
        horizon=h,
        step_size=1,
        n_windows=36
    )

    # Convert Timestamps to string for JSON serialization
    statistical_results['forecasts']['ds'] = statistical_results['forecasts']['ds'].astype(str)
    ml_results['future_predictions']['ds'] = ml_results['future_predictions']['ds'].astype(str)

    return JSONResponse(
        content={
            "statistical_forecast": statistical_results['forecasts'].to_dict(),
            "ml_forecast": ml_results['future_predictions'].to_dict()
        }
    )

@app.get("/statistical_metrics")
def get_statistical_metrics(h: int = Query(12, description="Forecast horizon")):
    """
    Returns only statistical metrics (no_scaling, with_scaling).
    """
    logger = setup_logger()
    logger.info("Starting statistical metrics endpoint")

    set_seeds()
    loader = DataLoader()
    price_df = loader.load_price_data()
    stats_df = prepare_data(price_df)

    statistical_results = run_statistical_pipeline(
        stats_df,
        forecast_horizon=h,
        step_size=1,
        n_windows=36
    )

    return JSONResponse(
        content={
            "no_scaling": statistical_results['no_scaling']['results'].to_dict(),
            "with_scaling": statistical_results['with_scaling']['results'].to_dict()
        }
    )

@app.get("/ml_metrics")
def get_ml_metrics(h: int = Query(12, description="Forecast horizon")):
    """
    Returns only ML metrics.
    """
    logger = setup_logger()
    logger.info("Starting ML metrics endpoint")

    set_seeds()
    loader = DataLoader()
    price_df = loader.load_price_data()
    stats_df = prepare_data(price_df)

    ml_results = run_forecasting_pipeline(
        stats_df,
        horizon=h,
        step_size=1,
        n_windows=36
    )

    return JSONResponse(content=ml_results['metrics'].to_dict()) 