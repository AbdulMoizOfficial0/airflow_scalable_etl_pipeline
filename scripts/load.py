import shutil
import yaml
import os

def load_data():
    with open('/opt/airflow/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    output_file = '/opt/airflow/data_output/transformed.csv'
    destination_folder = config['output_folder']
    destination_file = os.path.join(destination_folder, 'final_data.csv')

    shutil.move(output_file, destination_file)  # Rename transformed.csv to final_data.csv

if __name__ == "__main__":
    load_data()
