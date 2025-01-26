import os
import pandas as pd
from supabase import create_client, Client

# Set environment variables
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

# Initialize Supabase client
supabase: Client = create_client(url, key)

# Load cleaned data
df = pd.read_csv('cleaned_sales.csv')

# Infer schema from cleaned data
columns = df.columns
data_types = df.dtypes

# Map pandas dtypes to SQL data types
dtype_mapping = {
    'int64': 'INTEGER',
    'float64': 'FLOAT',
    'object': 'TEXT',
    'bool': 'BOOLEAN',
    'datetime64[ns]': 'TIMESTAMP'
}

# Generate SQL command to create table
table_name = 'cleaned_sales'
create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for col, dtype in zip(columns, data_types):
    sql_type = dtype_mapping[str(dtype)]
    create_table_sql += f"{col} {sql_type},"
create_table_sql = create_table_sql.rstrip(',') + ');'

# Execute the SQL command to create table
supabase.rpc('execute_sql', {'sql': create_table_sql}).execute()

# Upload data to Supabase
for index, row in df.iterrows():
    data = row.to_dict()
    supabase.table(table_name).insert(data).execute()
