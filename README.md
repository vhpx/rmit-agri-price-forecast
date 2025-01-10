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
    "statistical_forecast": {
        "ds": {
            "0": "2025-01-01",
            "1": "2025-02-01",
            ...
        },
        "AutoARIMA": {
            "0": 503.089,
            "1": 511.703,
            ...
        },
        "AutoARIMA-lo-90": {
            "0": 470.479,
            "1": 466.625,
            ...
        },
        "AutoARIMA-hi-90": {
            "0": 535.698,
            "1": 556.781,
            ...
        },
        "AutoETS": {...},
        "AutoETS-lo-90": {...},
        "AutoETS-hi-90": {...},
        "AutoTheta": {...},
        "AutoTheta-lo-90": {...},
        "AutoTheta-hi-90": {...},
        "CES": {...},
        "CES-lo-90": {...},
        "CES-hi-90": {...}
    },
    "ml_forecast": {
        "unique_id": {
            "0": "stats",
            "1": "stats",
            ...
        },
        "ds": {
            "0": "2025-01-01",
            "1": "2025-02-01",
            ...
        },
        "elasticnet": {
            "0": 484.423,
            "1": 475.038,
            ...
        },
        "lightgbm": {...},
        "xgboost": {...},
        "catboost": {...}
    }
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
    "no_scaling": {
        "Model": {
            "0": "AutoARIMA",
            "1": "AutoETS",
            "2": "AutoTheta",
            "3": "CES"
        },
        "RMSE": {
            "0": 83.459,
            "1": 79.528,
            "2": 76.848,
            "3": 81.624
        },
        "Directional_Accuracy": {
            "0": 0.457,
            "1": 0.498,
            "2": 0.635,
            "3": 0.475
        },
        "Turning_Point_Accuracy": {
            "0": 0.639,
            "1": 0.688,
            "2": 0.604,
            "3": 0.576
        },
        "Weighted_Score": {
            "0": 28.120,
            "1": 26.780,
            "2": 25.869,
            "3": 27.524
        }
    },
    "with_scaling": {
        // Same structure as no_scaling
    }
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
