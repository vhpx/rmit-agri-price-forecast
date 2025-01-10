#!/bin/bash

# Create a logs directory if it doesn't exist
mkdir -p logs

# Get current timestamp
timestamp=$(date +%Y%m%d_%H%M%S)

# Function to format JSON output
format_json() {
    python3 -c "import json; import sys; print(json.dumps(json.load(sys.stdin), indent=2))"
}

echo "=============================================="
echo "TESTING /forecast ENDPOINT WITH horizon=12 ..."
echo "=============================================="
curl -X GET "http://127.0.0.1:8000/forecast?h=12" | format_json | tee "logs/forecast_${timestamp}.txt"

echo ""
echo "=============================================="
echo "TESTING /statistical_metrics ENDPOINT WITH horizon=12 ..."
echo "=============================================="
curl -X GET "http://127.0.0.1:8000/statistical_metrics?h=12" | format_json | tee "logs/statistical_metrics_${timestamp}.txt"

echo ""
echo "=============================================="
echo "TESTING /ml_metrics ENDPOINT WITH horizon=12 ..."
echo "=============================================="
curl -X GET "http://127.0.0.1:8000/ml_metrics?h=12" | format_json | tee "logs/ml_metrics_${timestamp}.txt"

echo ""
echo "Done testing endpoints. Results saved to logs/[endpoint]_${timestamp}.txt files."