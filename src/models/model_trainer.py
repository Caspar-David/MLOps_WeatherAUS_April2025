import xgboost as xgb
import pandas as pd
import yaml
import joblib

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)["XGBoost"]

def train_model():
    X_train = pd.read_csv(config["model_trainer"]["X_train_path"])
    y_train = X_train.pop(config["schema"]["TARGET_COLUMN"]["name"])

    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)

    joblib.dump(model, config["model_trainer"]["model_name"])
    print("Model training completed.")

if __name__ == "__main__":
    train_model()

