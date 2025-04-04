import os
import urllib.request
import zipfile
import yaml

# Load config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def download_and_extract():
    url = config["data_ingestion"]["source_URL"]
    local_path = config["data_ingestion"]["local_data_file"]
    unzip_path = config["data_ingestion"]["unzip_dir"]

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    if not os.path.exists(local_path):
        print("Downloading dataset...")
        urllib.request.urlretrieve(url, local_path)
    
    print("Extracting dataset...")
    with zipfile.ZipFile(local_path, "r") as zip_ref:
        zip_ref.extractall(unzip_path)

    print("Data ingestion completed.")

if __name__ == "__main__":
    download_and_extract()

