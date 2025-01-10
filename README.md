# Rice Price Forecasting API

This API provides endpoints for rice price forecasting using both statistical and machine learning approaches.

## Local Development Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the development server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Get Forecast

Get both statistical and machine learning forecasts for rice prices.

```
GET /forecast
```

**Query Parameters:**
- `h` (integer, optional): Forecast horizon in months. Default: 12

**Response:**
```json
{
    "statistical_forecast": [
        {
            "date": "2025-01-01",
            "AutoARIMA": 503.089,
            "AutoARIMA-lo-90": 470.479,
            "AutoARIMA-hi-90": 535.698,
            "AutoETS": 496.524,
            "AutoETS-lo-90": 449.446,
            "AutoETS-hi-90": 543.602,
            "AutoTheta": 492.367,
            "AutoTheta-lo-90": 462.533,
            "AutoTheta-hi-90": 529.997,
            "CES": 494.386,
            "CES-lo-90": 447.228,
            "CES-hi-90": 543.096
        },
        {
            "date": "2025-02-01",
            "AutoARIMA": 511.703,
            // ... other model values
        }
    ],
    "ml_forecast": [
        {
            "date": "2025-01-01",
            "elasticnet": 484.423,
            "lightgbm": 484.711,
            "xgboost": 485.342,
            "catboost": 494.618
        },
        {
            "date": "2025-02-01",
            // ... predictions for other dates
        }
    ]
}
```

The forecast response includes:
- Statistical models (AutoARIMA, AutoETS, AutoTheta, CES) with their 90% confidence intervals (lo-90, hi-90)
- Machine learning models (ElasticNet, LightGBM, XGBoost, CatBoost) predictions

### 2. Get Statistical Metrics

Get performance metrics for statistical forecasting models.

```
GET /statistical_metrics
```

**Query Parameters:**
- `h` (integer, optional): Forecast horizon in months. Default: 12

**Response:**
```json
{
    "no_scaling": [
        {
            "Model": "AutoARIMA",
            "RMSE": 83.459,
            "Directional_Accuracy": 0.457,
            "Turning_Point_Accuracy": 0.639,
            "Weighted_Score": 28.120
        },
        {
            "Model": "AutoETS",
            "RMSE": 79.528,
            "Directional_Accuracy": 0.498,
            "Turning_Point_Accuracy": 0.688,
            "Weighted_Score": 26.780
        }
    ],
    "with_scaling": [
        // Same structure as no_scaling
    ]
}
```

The statistical metrics include:
- RMSE (Root Mean Square Error)
- Directional Accuracy (0-1, higher is better)
- Turning Point Accuracy (0-1, higher is better)
- Weighted Score (composite metric)

### 3. Get Machine Learning Metrics

Get performance metrics for machine learning forecasting models.

```
GET /ml_metrics
```

**Query Parameters:**
- `h` (integer, optional): Forecast horizon in months. Default: 12

**Response:**
```json
{
    "elasticnet": {
        "RMSE": 84.181,
        "Directional_Accuracy": 0.600,
        "Turning_Point_Accuracy": 0.562,
        "Weighted_Score": 28.339
    },
    "lightgbm": {
        "RMSE": 85.063,
        "Directional_Accuracy": 0.508,
        "Turning_Point_Accuracy": 0.607,
        "Weighted_Score": 28.649
    },
    "xgboost": {
        "RMSE": 80.738,
        "Directional_Accuracy": 0.559,
        "Turning_Point_Accuracy": 0.576,
        "Weighted_Score": 27.200
    },
    "catboost": {
        "RMSE": 74.421,
        "Directional_Accuracy": 0.635,
        "Turning_Point_Accuracy": 0.611,
        "Weighted_Score": 25.057
    }
}
```

The ML metrics include for each model:
- RMSE (Root Mean Square Error)
- Directional Accuracy (0-1, higher is better)
- Turning Point Accuracy (0-1, higher is better)
- Weighted Score (composite metric)

## API Documentation

For interactive API documentation, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
