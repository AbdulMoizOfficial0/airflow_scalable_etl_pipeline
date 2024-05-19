import os
import pandas as pd
import yaml


def extract_data():
    with open('/opt/airflow/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    input_folder = config['input_folder']
    csv_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.csv')]

    data_frames = [pd.read_csv(csv_file) for csv_file in csv_files]
    combined_data = pd.concat(data_frames, ignore_index=True)

    combined_data.to_csv('/opt/airflow/data_input/combined.csv', index=False)


if __name__ == "__main__":
    extract_data()


