import pandas as pd
import yaml


def transform_data():
    with open('/opt/airflow/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    input_file = '/opt/airflow/data_input/combined.csv'
    df = pd.read_csv(input_file)

    # Remove the last 2 columns
    df = df.iloc[:, :-2]

    df.to_csv('/opt/airflow/data_output/transformed.csv', index=False)


if __name__ == "__main__":
    transform_data()
