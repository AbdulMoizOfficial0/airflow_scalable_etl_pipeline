import shutil
import yaml
import os


def load_data():
    with open('/opt/airflow/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    output_folder = '/opt/airflow/data_output/transformed_data.csv'
    destination_folder = config['output_folder']
    destination_file = os.path.join(destination_folder, 'final_data.csv')

    shutil.move(output_folder, destination_file)
    