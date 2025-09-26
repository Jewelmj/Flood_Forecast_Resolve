CropProfit Predictor

Project Overview:

We are developing an agentic AI framework in the domain of agriculture to assist farmers in decision-making and risk management. 

The system addresses two primary challenges:

1)Crop Recommendation: Based on market demand, weather conditions, and soil characteristics, 
                        the system suggests which crops to cultivate in order to maximize profit.
2)Crop Loss Prediction: Using weather forecasts and historical data, the system predicts the expected percentage loss for crops, 
                        helping farmers plan mitigation strategies.

To achieve this, we implement a multi-agent architecture:

1) Data Scraper Agent: Collects and aggregates relevant market, soil, and weather data.
2) Demand Prediction Agent: Forecasts crop demand based on market trends.
3) Weather Forecast Agent: Predicts upcoming weather conditions affecting crop yield.
4) Notification/Decision Agent: Integrates insights from all agents and delivers actionable recommendations to the user interface.

This framework provides a data-driven, intelligent solution for optimizing crop selection and minimizing agricultural risk.


Technical Requirements:
1) use Python: 3.12
2) Environment Management: Conda
3) Dependencies: Listed in requirements.txt
4) get groq api key from https://console.groq.com/keys
