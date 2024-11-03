# Rice Price Forecasting Project

## Overview
This project implements multiple forecasting approaches to predict Vietnamese rice prices using both statistical and machine learning models. It combines macro-economic indicators, news sentiment data, and historical price data to generate forecasts.

## Data Sources
- target_rice_data.xlsx: Vietnamese 5% broken rice prices (monthly)
- macro_data.xlsx: Macro-economic indicators from Vietnam  
- news_data_loaded.xlsx: News sentiment data
- Time period: 2009-2024

## Models Implemented
1. Statistical Models (statsforecast.ipynb):
   - AutoARIMA
   - AutoETS 
   - AutoTheta
   - AutoCES
   
2. Machine Learning Models (mlforecast.ipynb):
   - ElasticNet
   - XGBoost
   - LightGBM
   - CatBoost

## Key Features
- Data preprocessing and cleaning
- Automatic TS feature engineering & LLM-powered sentiment analysis 
- Cross-validation with rolling windows for most robustness checks
- Ray-powered parallel processing for efficient statistical model training
- Efficient automated ML & DL forecasting pipeline
- Multiple evaluation metrics:
  * RMSE (Root Mean Square Error)
  * Directional Accuracy
  * Turning Point Accuracy
  * Weighted Combined Score

## Project Structure
preprocessing.ipynb
- Data loading and cleaning
- Feature engineering
- Data merging and preparation

mlforecast.ipynb
- Machine learning model implementation
- Model training and evaluation
- Cross-validation
- Results visualization

statsforecast.ipynb
- Statistical model implementation
- Model training and evaluation
- Cross-validation
- Results comparison

## Requirements
Python 3.10+
Key packages:
- pandas
- numpy
- scikit-learn
- statsforecast
- mlforecast
- ray
- matplotlib
- xgboost
- lightgbm
- catboost

## Usage
1. Run preprocessing.ipynb first to prepare the data
2. Run either statsforecast.ipynb or mlforecast.ipynb for predictions
3. Results include performance metrics and visualizations

Note: The project uses parallel processing through Ray for efficient computation of statistical models.

## License
This project is for research purposes only. Please ensure you have the necessary rights to use the data sources mentioned above.