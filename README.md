# Airline Price Prediction & Passenger Satisfaction Analysis
A complete end-to-end data science project that analyzes airline ticket pricing and passenger satisfaction using Machine Learning, Tableau, and an interactive web-based UI.


#Features
Machine Learning Models — XGBoost (Regression), Random Forest (Classification), K-Means (Clustering)
Data Visualization — Tableau dashboards for pricing and satisfaction analysis
Interactive UI — User input-based real-time price prediction system
End-to-End Pipeline — Data preprocessing, modeling, evaluation, and deployment
Model Explainability — Feature importance and SHAP-based insights

#airline-analysis/
│
├── app.py                      # Web application (Flask/Streamlit)
├── requirements.txt            # Dependencies
│
├── data/
│   ├── pricing_dataset.csv
│   └── satisfaction_dataset.csv
│
├── models/
│   ├── xgboost_model.pkl
│   ├── random_forest_model.pkl
│   └── kmeans_model.pkl
│
├── notebooks/
│   └── eda_and_training.ipynb
│
├── tableau/
│   └── dashboards.twbx
│
└── templates/
    └── index.html

 #Quick Start
1. Clone the repository
2. Install dependencies
pip install -r requirements.txt
3. Run the application
python app.py
Open in browser: http://localhost:5000

#Datasets
#Airline Ticket Price Dataset
-Airline
-Source & Destination
-Duration
-Days Left
-Class
-Price

#Passenger Satisfaction Dataset
-Online Boarding
-Seat Comfort
-Inflight WiFi
-Travel Type
-Satisfaction

Source: Kaggle

#How It Works
Step	Description
Preprocessing- Data cleaning, missing value handling, encoding
Feature Engineering-	Creation of Service Score, label encoding
Modeling-	XGBoost for price, Random Forest for satisfaction
Clustering-	K-Means segmentation (budget, mid, premium)
Visualization-	Tableau dashboards for insights
Deployment-	UI for real-time prediction

#Machine Learning Models
-XGBoost (Regression)
Used for ticket price prediction
Key features: Duration, Days Left
High accuracy with strong alignment between actual and predicted values

-Random Forest (Classification)
Used for passenger satisfaction prediction
Key features: Online Boarding, WiFi
AUC Score: 0.986

-K-Means Clustering
Segmentation into:
Budget
Mid-range
Premium


#User Interface
Input parameters: source, destination, duration, class, days left
Predicts ticket price using trained model
Displays insights and analytics
Simulates real-world airline pricing system

#Key Insights
Ticket prices increase with duration and last-minute booking
Airlines follow distinct pricing strategies (budget vs premium)
Digital services (boarding, WiFi) strongly influence satisfaction
Seat comfort significantly impacts passenger experience
Models achieved high accuracy and reliability

#Tech Stack
Backend: Python
Libraries: Pandas, NumPy, Scikit-learn, XGBoost
Visualization: Tableau
Frontend/UI: HTML, CSS, JavaScript / Flask / Streamlit
Notebook: Jupyter




