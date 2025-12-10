import pandas as pd
import requests
import io
from persistent import Persistent
from persistent.list import PersistentList
import ZODB, ZODB.FileStorage
import transaction
import os

# --- Configuration ---
# 1. CSV Source
CSV_URL = "https://gitlab.com/hvescovi/prog23/-/raw/main/bd/datasets/fire/amazon_UTF8_CLEANED.csv"

# 2. ZODB Destination
ZODB_FILE = "amazon_fires.fs" # The name of the ZODB file storage
# ---------------------

## ZODB Model Definition (The Python Object)
# Inheriting from `Persistent` is mandatory for ZODB to track changes.
class FireRecord(Persistent):
    """
    A class to represent a single record (row) from the Amazon fire dataset.
    
    The attributes mirror the columns in the CSV file.
    """
    def __init__(self, date, year, month, state, number):
        self.date = date
        self.year = year
        self.month = month
        self.state = state
        self.number = number
        
    # Optional: A useful representation for debugging
    def __repr__(self):
        return (f"<FireRecord state='{self.state}', year={self.year}, "
                f"number={self.number}>")


print("\n--- Reading Data Demonstration ---")
try:
    # Open the database connection
    storage = ZODB.FileStorage.FileStorage(ZODB_FILE)
    db = ZODB.DB(storage)
    conn = db.open()
    root = conn.root
    
    fire_records_list = root.fire_records
    
    print(f"Found {len(fire_records_list)} records in the database.")
    n = 10
    print(f"\nFirst {n} records:")
    for i in range(n):
        record = fire_records_list[i]
        # Accessing attributes directly like any Python object
        print(f"  > State: {record.state}, Date: {record.date}, Number: {record.number}")
    
    # getting data of year 2010
    for rec in fire_records_list:
        if rec.year == 2010:
            print(f"\nRecord from 2010: State: {rec.state}, Date: {rec.date}, Number: {rec.number}")
    
    conn.close()
    db.close()
    
except Exception as e:
    print(f"Could not read from ZODB: {e}")
    
