import pandas as pd
import joblib
import yaml
from sklearn.metrics import accuracy_score

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def evaluate_model():
    X_test = pd.read_csv(config["model_evaluation"]["X_test_path"])
    y_test = X_test.pop(config["schema"]["TARGET_COLUMN"]["name"])

    model = joblib.load(config["model_evaluation"]["model_path"])
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")

if __name__ == "__main__":
    evaluate_model()

