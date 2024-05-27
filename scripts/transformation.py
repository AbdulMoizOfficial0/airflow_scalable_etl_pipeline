import pandas as pd
import yaml

def transform_data():
    with open('/opt/airflow/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    input_file = '/opt/airflow/data_input/combined_data.csv'
    df = pd.read_csv(input_file)

    df = df.iloc[:, :-2]

    df.to_csv("/opt/airflow/data_output/transformed_data.csv", index=False)
