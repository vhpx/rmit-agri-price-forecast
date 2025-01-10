#!/bin/bash

echo "=============================================="
echo "TESTING /forecast ENDPOINT WITH horizon=12 ..."
echo "=============================================="
curl -X GET "http://127.0.0.1:8000/forecast?h=12" > forecast_output.txt

echo ""
echo "=============================================="
echo "TESTING /statistical_metrics ENDPOINT WITH horizon=12 ..."
echo "=============================================="
curl -X GET "http://127.0.0.1:8000/statistical_metrics?h=12" > statistical_metrics_output.txt

echo ""
echo "=============================================="
echo "TESTING /ml_metrics ENDPOINT WITH horizon=12 ..."
echo "=============================================="
curl -X GET "http://127.0.0.1:8000/ml_metrics?h=12" > ml_metrics_output.txt

echo ""
echo "Done testing endpoints. Results saved to *_output.txt files."