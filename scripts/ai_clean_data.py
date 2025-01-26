import os
import pandas as pd
from transformers import pipeline
from pycaret.datasets import get_data
from pycaret.preprocessing import *

# Load raw data
raw_data = pd.read_csv('sales_raw.csv')
print("Raw data loaded successfully.")

# Initialize Hugging Face pipeline for text cleaning
cleaner = pipeline('text-classification', model='bert-base-uncased')
print("Hugging Face pipeline initialized.")

# Clean text data
raw_data['cleaned_text'] = raw_data['text_column'].apply(lambda x: cleaner(x)[0]['label'])
print("Text data cleaned using Hugging Face pipeline.")

# Additional cleaning with PyCaret
clean_data = clean_data(raw_data)
print("Data cleaned using PyCaret.")

# Save cleaned data to a temporary CSV
clean_data.to_csv('cleaned_sales.csv', index=False)
print("Cleaned data saved to 'cleaned_sales.csv'.")
