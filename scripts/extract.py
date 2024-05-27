import os
import pandas as pd
import yaml


def extract_data():
    with open('/opt/airflow/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    input_folder = config['input_folder']
    csv_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.csv')]

    data_frames = [pd.read_csv(csv_file) for csv_file in csv_files]
    combine_data = pd.concat(data_frames, ignore_index=True)

    combine_data.to_csv('/opt/airflow/data_input/combined_data.csv', index=False)
