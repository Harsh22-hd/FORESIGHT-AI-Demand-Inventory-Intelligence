# FORESIGHT – AI Demand & Inventory Intelligence Platform

FORESIGHT is an AI-powered demand forecasting and inventory intelligence platform designed to help businesses predict SKU-level demand, identify stockout and overstock risks, and generate actionable inventory recommendations through an interactive dashboard.

## 🚀 Key Features

- 📈 SKU-level demand forecasting
- 📦 Inventory monitoring and analysis
- ⚠️ Stockout risk detection
- 📊 Overstock risk detection
- 💡 Automated inventory recommendations
- 🔎 SKU-based filtering and analysis
- 📅 Date-based forecast filtering
- 📊 Interactive Streamlit dashboard
- ⚡ FastAPI REST API
- 🤖 Machine Learning based demand prediction
- 📋 Business-ready recommendation tables
- 📚 Swagger API documentation

## 🧰 Tech Stack

### Programming Language
- Python

### Data Science & Machine Learning
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Statsmodels

### Visualization
- Plotly
- Matplotlib

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Frontend / Dashboard
- Streamlit

### Development & Testing
- Jupyter Notebook
- Pytest

## 📁 Project Structure

```text
FORESIGHT Project/
│
├── api/
│   ├── app/
│   │   ├── config.py
│   │   ├── main.py
│   │   └── __init__.py
│   ├── routes/
│   │   ├── forecast.py
│   │   ├── health.py
│   │   ├── inventory.py
│   │   ├── recommendations.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── forecast.py
│   │   ├── inventory.py
│   │   ├── recommendation.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── forecast_service.py
│   │   ├── inventory_service.py
│   │   ├── model_service.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
│
├── dashboard/
│   └── app.py
│
├── Data/
│   ├── external/
│   ├── processed/
│   └── raw/
│       ├── calendar.csv
│       ├── inventory.csv
│       ├── product_master.csv
│       └── sales.csv
│
├── models/
│   ├── features/
│   │   ├── feature_columns.csv
│   │   ├── X_train.csv
│   │   ├── X_test.csv
│   │   ├── y_train.csv
│   │   └── y_test.csv
│   ├── forecast_output/
│   │   └── foresight_inventory_intelligence.csv
│   ├── predictions/
│   │   └── random_forest_predictions.csv
│   ├── random_forest_demand_model.pkl
│   └── random_forest_model_metadata.json
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_experiments.ipynb
│   └── 05_demand_forecasting.ipynb
│
├── src/
│   ├── data/
│   ├── features/
│   ├── forecasting/
│   ├── inventory/
│   └── utils/
│
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## 📊 Dataset Description

FORESIGHT uses four primary datasets.

### 1. Sales Data – `sales.csv`

| Column | Description |
|---|---|
| `Date` | Sales date |
| `SKU` | Product identifier |
| `Units_Sold` | Number of units sold |
| `Revenue` | Revenue generated |
| `Price` | Selling price |
| `Promotion` | Promotion indicator |

### 2. Inventory Data – `inventory.csv`

| Column | Description |
|---|---|
| `Snapshot_Date` | Inventory snapshot date |
| `SKU` | Product identifier |
| `Current_Stock` | Current available stock |
| `On_Order` | Units already ordered |
| `Lead_Time_Days` | Supplier lead time |
| `Safety_Stock` | Required safety stock |
| `Reorder_Point` | Reorder threshold |
| `Inventory_Value` | Value of inventory |

### 3. Product Master – `product_master.csv`

| Column | Description |
|---|---|
| `SKU` | Product identifier |
| `Product_Name` | Product name |
| `Category` | Product category |
| `Subcategory` | Product subcategory |
| `Launch_Date` | Product launch date |
| `Cost_Price` | Product cost |
| `Selling_Price` | Selling price |
| `Gross_Margin_Per_Unit` | Gross margin per unit |

### 4. Calendar Data – `calendar.csv`

| Column | Description |
|---|---|
| `date` | Calendar date |
| `year` | Year |
| `month` | Month |
| `quarter` | Quarter |
| `week` | Week number |
| `day_of_week` | Day of week |
| `is_weekend` | Weekend indicator |
| `season` | Season |
| `holiday` | Holiday information |
| `is_holiday` | Holiday indicator |
| `promotion_event` | Promotion/event information |

## 🔄 Machine Learning Pipeline

```text
Raw Data
   │
   ▼
Data Loading
   │
   ▼
Data Validation
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Data Cleaning
   │
   ▼
Feature Engineering
   │
   ▼
Train/Test Split
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Demand Prediction
   │
   ▼
Inventory Risk Analysis
   │
   ▼
Inventory Recommendations
   │
   ▼
Dashboard
```

## 🤖 Demand Forecasting

FORESIGHT uses a **Random Forest Regressor** for demand prediction.

The model learns relationships between historical sales, product information, pricing, promotions, calendar features, and other engineered variables to estimate future SKU demand.

The trained model is stored in:

```text
models/random_forest_demand_model.pkl
```

Model metadata is stored in:

```text
models/random_forest_model_metadata.json
```

## ⚠️ Inventory Risk Intelligence

FORESIGHT evaluates inventory health using predicted demand and current inventory information.

### Stockout Risk

Stockout risk identifies products where available inventory may not be sufficient to satisfy expected demand.

Typical factors include:

- Predicted demand
- Current stock
- On-order quantity
- Safety stock
- Reorder point
- Lead time

### Overstock Risk

Overstock risk identifies products where inventory is significantly higher than expected demand.

This helps businesses:

- Reduce excess inventory
- Improve working capital
- Reduce holding costs
- Identify slow-moving products

## 💡 Recommendation Engine

The recommendation engine converts forecasting and inventory analysis into business actions.

```text
High Stockout Risk
        ↓
Prioritize Replenishment

Low Stock + High Demand
        ↓
Increase Order Quantity

High Stock + Low Demand
        ↓
Reduce / Delay Replenishment

Healthy Inventory
        ↓
Maintain Current Stock
```

Recommendations are displayed with priority and inventory health information.

## ⚡ FastAPI Backend

FORESIGHT provides REST API endpoints for the dashboard.

| Endpoint | Purpose |
|---|---|
| `/health` | API health check |
| `/forecast` | Demand forecast data |
| `/inventory` | Inventory intelligence |
| `/recommendations` | Inventory recommendations |

### Swagger Documentation

After starting FastAPI:

```text
http://127.0.0.1:8000/docs
```

## 📊 Streamlit Dashboard

The FORESIGHT dashboard provides an interactive business interface.

### Dashboard Modules

#### 1. Overview
- Total SKUs
- Forecast information
- Inventory status
- Stockout risk
- Overstock risk
- Demand trends
- Risk visualizations

#### 2. Demand Forecast
- SKU filtering
- Date filtering
- Predicted demand
- Demand trend visualization
- Forecast data table

#### 3. Inventory
- SKU filtering
- Current stock
- On-order inventory
- Inventory visualizations
- Inventory data table

#### 4. Recommendations
- SKU search
- Stockout risk filter
- Overstock risk filter
- Risk visualizations
- Priority levels
- Inventory health
- Recommended actions

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd "FORESIGHT Project"
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

FORESIGHT uses FastAPI as the backend and Streamlit as the dashboard.

### Step 1 – Start FastAPI

Open a terminal:

```bash
cd "D:\Zidio project\FORESIGHT Project\api"
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 2 – Start Streamlit

Open a second terminal:

```bash
cd "D:\Zidio project\FORESIGHT Project\dashboard"
streamlit run app.py
```

Streamlit will provide the local dashboard URL in the terminal.

## 🧪 Testing

Run tests using:

```bash
pytest
```

For detailed output:

```bash
pytest -v
```

## 📓 Notebook Workflow

### `01_data_exploration.ipynb`
Initial dataset loading, inspection, validation, and basic exploration.

### `02_eda.ipynb`
Exploratory data analysis and visualization of sales, products, inventory, and calendar information.

### `03_feature_engineering.ipynb`
Creation of machine learning features required for demand prediction.

### `04_model_experiments.ipynb`
Model experimentation, training, and evaluation.

### `05_demand_forecasting.ipynb`
Demand prediction and generation of forecast outputs.

## 💼 Business Value

FORESIGHT is designed to support inventory decision-making by transforming raw business data into actionable insights.

### Business Benefits

- Reduce stockout situations
- Reduce excess inventory
- Improve inventory turnover
- Support better purchasing decisions
- Improve demand visibility
- Prioritize high-risk SKUs
- Reduce manual inventory analysis
- Improve working capital utilization
- Enable data-driven replenishment decisions

## 🎯 Project Objectives

1. Predict future product demand.
2. Identify SKU-level inventory risks.
3. Detect potential stockout situations.
4. Detect potential overstock situations.
5. Generate actionable inventory recommendations.
6. Provide an easy-to-use business dashboard.
7. Expose forecasting and inventory intelligence through APIs.

## 🔮 Future Improvements

- Time-series models such as Prophet and ARIMA
- XGBoost / LightGBM model comparison
- Automated model retraining
- Real-time sales data integration
- External data integration
- Supplier performance analytics
- Automated purchase order generation
- Advanced anomaly detection
- Explainable AI for demand predictions
- User authentication and role-based access
- Cloud deployment
- Database integration
- Forecast accuracy monitoring
- Automated alerts for high-risk SKUs

## 🔐 Data & Configuration

Raw datasets are stored under:

```text
Data/raw/
```

Generated model artifacts are stored under:

```text
models/
```

Environment-specific configuration can be managed using environment variables and `.env` files.

Sensitive configuration files and local development files are excluded through `.gitignore`.

## 📌 Project Status

- ✅ Data exploration
- ✅ EDA
- ✅ Feature engineering
- ✅ Machine learning demand forecasting
- ✅ Inventory intelligence
- ✅ Stockout risk analysis
- ✅ Overstock risk analysis
- ✅ Recommendation engine
- ✅ FastAPI backend
- ✅ Swagger API documentation
- ✅ Streamlit dashboard
- ✅ Forecast filters
- ✅ Inventory filters
- ✅ Recommendation SKU search
- ✅ Risk visualizations
- ✅ Large inventory result support

## 👨‍💻 Author

**Harsh Darji**

MSc Data Science  
BCA Graduate  
Data Science / Machine Learning Enthusiast

## ⭐ Summary

**FORESIGHT** combines Machine Learning, Data Science, FastAPI, and Streamlit to create an end-to-end demand forecasting and inventory intelligence solution.

```text
Data
  ↓
Insights
  ↓
Demand Forecast
  ↓
Inventory Risk
  ↓
Actionable Recommendation
```

FORESIGHT demonstrates a complete real-world Data Science project workflow — from raw data and exploratory analysis to machine learning, API development, and an interactive business dashboard.
