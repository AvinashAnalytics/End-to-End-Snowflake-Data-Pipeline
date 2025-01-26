import pandas as pd
from transformers import pipeline
from pycaret.datasets import get_data
from pycaret.preprocessing import *

# Load raw data
raw_data = pd.read_csv('sales_raw.csv')

# Initialize Hugging Face pipeline for text cleaning
cleaner = pipeline('text-classification', model='bert-base-uncased')

# Clean data
raw_data['cleaned_text'] = raw_data['text_column'].apply(lambda x: cleaner(x)[0]['label'])

# Additional cleaning with PyCaret
clean_data = clean_data(raw_data)

# Save cleaned data
clean_data.to_csv('cleaned_sales.csv', index=False)
