import os
import logging

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def load_env_variables():
    from dotenv import load_dotenv
    load_dotenv()

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_dataframe_to_csv(df, file_path):
    df.to_csv(file_path, index=False)
    logging.info(f'Saved DataFrame to {file_path}')