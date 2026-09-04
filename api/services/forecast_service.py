import joblib
import pandas as pd

from api.app.config import PROJECT_ROOT


MODEL_PATH = PROJECT_ROOT / "models" / "random_forest_demand_model.pkl"
FEATURE_DIR = PROJECT_ROOT / "models" / "features"
DATA_DIR = PROJECT_ROOT / "Data" / "raw"


class ForecastService:

    def __init__(self):
        self.model = None
        self.feature_columns = None

    def load_model(self):
        if self.model is None:
            self.model = joblib.load(MODEL_PATH)

        return self.model

    def load_features(self):
        if self.feature_columns is None:
            self.feature_columns = pd.read_csv(
                FEATURE_DIR / "feature_columns.csv"
            )["Feature"].tolist()

        return self.feature_columns

    def generate_forecast(self):
        model = self.load_model()
        feature_columns = self.load_features()

        X_test = pd.read_csv(
            FEATURE_DIR / "X_test.csv"
        )

        X_test = X_test[feature_columns]

        predictions = model.predict(X_test)

        forecast_df = pd.DataFrame({
            "Predicted_Demand": predictions
        })

        forecast_df["Predicted_Demand"] = (
            forecast_df["Predicted_Demand"]
            .clip(lower=0)
            .round(2)
        )

        sales_df = pd.read_csv(
            DATA_DIR / "sales.csv"
        )

        sales_df["Date"] = pd.to_datetime(
            sales_df["Date"]
        )

        sales_mapping = (
            sales_df
            .sort_values(["Date", "SKU"])
            .reset_index(drop=True)
        )

        test_rows = len(forecast_df)

        test_mapping = (
            sales_mapping
            .iloc[-test_rows:]
            [["Date", "SKU"]]
            .reset_index(drop=True)
        )

        forecast_output = pd.concat(
            [
                test_mapping,
                forecast_df.reset_index(drop=True)
            ],
            axis=1
        )

        return forecast_output


forecast_service = ForecastService()