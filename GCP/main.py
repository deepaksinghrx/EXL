import os 
from google.cloud import bigquery
from matplotlib.table import table 

def run_etl(): 
    project_id = os.getenv("PROJECT_ID") 
    dataset = os.getenv("BQ_DATASET") 
    table = os.getenv("BQ_TABLE") 

client = bigquery.Client(project=project_id) 

query = f""" 
CREATE OR REPLACE TABLE `{project_id}.{dataset}.{table}` AS 
SELECT 
CURRENT_DATE() AS load_date, 
'cloud_run_etl_success' AS status 
""" 

client.query(query).result() 
print("ETL completed successfully") 

if __name__ == "__main__": 
    run_etl()