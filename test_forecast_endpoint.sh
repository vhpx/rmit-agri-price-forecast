#!/bin/bash

echo "Testing /forecast endpoint with horizon=12..."
curl -X GET "http://127.0.0.1:8000/forecast?h=12" > forecast_test.log