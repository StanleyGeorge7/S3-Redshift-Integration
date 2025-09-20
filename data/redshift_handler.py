import os
import boto3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_redshift_connection():
    redshift_endpoint = os.getenv('REDSHIFT_ENDPOINT')
    redshift_user = os.getenv('REDSHIFT_USER')
    redshift_password = os.getenv('REDSHIFT_PASSWORD')
    redshift_db = os.getenv('REDSHIFT_DB')

    conn = boto3.client('redshift-data', 
                        region_name=os.getenv('AWS_REGION'),
                        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    return conn

def query_redshift(query):
    conn = get_redshift_connection()
    response = conn.execute_statement(
        ClusterIdentifier=os.getenv('REDSHIFT_CLUSTER_ID'),
        Database=redshift_db,
        DbUser=redshift_user,
        Sql=query
    )
    return response

def fetch_data(query):
    response = query_redshift(query)
    data = response['Records']
    df = pd.DataFrame(data)
    return df