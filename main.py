from supabase import create_client, Client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

# data from: https://www.kaggle.com/datasets/divu2001/coffee-shop-sales-analysis/data

url: str = "https://lgrlgjkibvhjbybbmcwb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxncmxnamtpYnZoamJ5YmJtY3diIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI2Mjc3NTYsImV4cCI6MjAyODIwMzc1Nn0.uX392Mdc1JCj0eeTQVcT5B3lVhnEJAtmWLngsd1yqrY"
supabase: Client = create_client(url, key)

app = FastAPI()

class Transaction(BaseModel):
    transaction_id: int
    transaction_date: datetime
    transaction_time: datetime
    store_id: int
    transaction_qty: int
    unit_price: float
    product_category: str
    product_type: str
    size: str
    
@app.get("/transactions/")
def read_items():
    data = supabase.table("df").select("*").order("created_at", ascending=False).limit(10).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Transactions not found")

@app.post("/{transaction_id}/")
def create_transaction(transaction: Transaction):
    transaction.total_bill = transaction.calculate_total_bill()
    transaction.transaction_date = datetime.now().strftime('%Y-%m-%d')
    transaction.transaction_time = datetime.now().strftime('%H:%M:%S')
    data = supabase_client.table("transactions").insert(transaction.dict()).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=400, detail="Transaction could not be created")
