from supabase import create_client, Client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# data from: https://www.kaggle.com/datasets/divu2001/coffee-shop-sales-analysis/data

url: str = "https://lgrlgjkibvhjbybbmcwb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxncmxnamtpYnZoamJ5YmJtY3diIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI2Mjc3NTYsImV4cCI6MjAyODIwMzc1Nn0.uX392Mdc1JCj0eeTQVcT5B3lVhnEJAtmWLngsd1yqrY"
supabase: Client = create_client(url, key)

app = FastAPI()
