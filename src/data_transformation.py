import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def transform_data():
    data_path = config["data_transformation"]["data_path"]
    df = pd.read_csv(data_path)

    # Split data
    train, test = train_test_split(df, test_size=0.2, random_state=1)

    # Save transformed data
    train.to_csv(config["model_trainer"]["X_train_path"], index=False)
    test.to_csv(config["model_trainer"]["X_test_path"], index=False)

    print("Data transformation completed.")

if __name__ == "__main__":
    transform_data()

