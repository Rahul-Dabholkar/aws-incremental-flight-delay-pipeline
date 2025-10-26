import kagglehub
import shutil
import os
from create_env import create_env_file

def download_and_organize_airline_data(base_path):
    """
    Download and organize
    """
    os.makedirs(base_path, exist_ok=True)
    os.environ['KAGGLEHUB_CACHE'] = base_path
    path = kagglehub.dataset_download("tylerx/flights-and-airports-data")
    print("Downloaded Successfully :", path) 
    
    # Copy files to desired locations
    for file_name in os.listdir(path):
        src_path = os.path.join(path, file_name)
        
        if file_name.lower() == 'airports.csv':
            airports_dir = os.path.join(base_path, 'airports')
            os.makedirs(airports_dir, exist_ok=True)
            dst_path = os.path.join(airports_dir, 'airports.csv')
            shutil.copy2(src_path, dst_path)
            print(f"Copied {file_name} to {airports_dir}")
        
        elif file_name.lower() == 'flights.csv':
            flights_dir = os.path.join(base_path, 'flights')
            os.makedirs(flights_dir, exist_ok=True)
            dst_path = os.path.join(flights_dir, 'flights.csv')
            shutil.copy2(src_path, dst_path)
            print(f"Copied {file_name} to {flights_dir}")
        
        else:
            print(f"Unknown file: {file_name}")
    
    print("Files downloaded successfully!")
    
    return {
        'airports': os.path.join(airports_dir, 'airports.csv'),
        'flights': os.path.join(flights_dir, 'flights.csv')
    }

if __name__ == "__main__":
    base_path = "./s3_data"
    create_env_file()
    download_and_organize_airline_data(base_path)
    