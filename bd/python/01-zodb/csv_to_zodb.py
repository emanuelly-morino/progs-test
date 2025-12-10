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

def fetch_csv_data():
    """Fetches the CSV file from the URL and returns a Pandas DataFrame."""
    print(f"1. Attempting to fetch CSV from: {CSV_URL}")
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()
        csv_data = io.StringIO(response.text)
        df = pd.read_csv(csv_data)
        # Clean up column names by stripping whitespace
        df.columns = df.columns.str.strip()
        print(f"   -> Successfully loaded {len(df)} records.")
        return df
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the CSV: {e}")
        return None

def csv_to_zodb(df):
    """
    Converts a DataFrame of fire records into a ZODB file.
    """
    print(f"2. Initializing ZODB File Storage: {ZODB_FILE}")
    
    # 2a. Setup Connection
    # Create or open the file storage
    storage = ZODB.FileStorage.FileStorage(ZODB_FILE)
    # Open the database connection
    db = ZODB.DB(storage)
    # Get the connection object
    conn = db.open()
    # The root object is where all other objects are attached
    root = conn.root
    
    # Check if the main storage list exists, otherwise create it.
    # Use PersistentList so ZODB notices in-place mutations like append/del.
    if not hasattr(root, 'fire_records') or not isinstance(root.fire_records, PersistentList):
        existing = getattr(root, 'fire_records', None)
        if existing is None:
            setattr(root, 'fire_records', PersistentList())
        else:
            # Convert any existing plain list into a PersistentList
            setattr(root, 'fire_records', PersistentList(existing))

    fire_records_list = root.fire_records
    
    print("3. Converting DataFrame rows to FireRecord objects and storing...")
    
    # 2b. Data Conversion and Insertion
    
    # Clear existing data for a fresh run
    del fire_records_list[:]
    
    inserted_count = 0
    
    # Iterate through the DataFrame rows
    for index, row in df.iterrows():
        # Create an instance of the Persistent class
        try:
            record = FireRecord(
                date=row['date'],
                year=row['year'],
                month=row['month'],
                state=row['state'],
                # Convert 'number' to float/int if needed, ZODB is flexible but good practice
                number=float(row['number'])
            )
            # Append the Persistent object to the list in the root object
            fire_records_list.append(record)
            inserted_count += 1
            
            # We commit frequently to manage memory/transaction size, though once 
            # outside the loop is also fine for smaller datasets.
            if inserted_count % 1000 == 0:
                transaction.commit()
                print(f"   -> Committed {inserted_count} records.")
        except Exception as e:
            print(f"   ! Error inserting record at index {index}: {e}")

    # Final commit to save all changes permanently to the .fs file
    transaction.commit()
    print("-" * 50)
    print(f"Success! Total {inserted_count} FireRecord objects inserted.")
    print(f"ZODB file created: {ZODB_FILE}")
    print("-" * 50)

    # 2c. Cleanup
    conn.close()
    db.close()


def read_data_from_zodb():
    """
    Demonstrates how to read and access the stored objects from the ZODB file.
    """
    print("\n--- Reading Data Demonstration ---")
    try:
        # Open the database connection
        storage = ZODB.FileStorage.FileStorage(ZODB_FILE)
        db = ZODB.DB(storage)
        conn = db.open()
        root = conn.root
        
        fire_records_list = root.fire_records
        
        print(f"Found {len(fire_records_list)} records in the database.")
        print("\nFirst 3 records:")
        for i in range(3):
            record = fire_records_list[i]
            # Accessing attributes directly like any Python object
            print(f"  > State: {record.state}, Date: {record.date}, Number: {record.number}")
            
        conn.close()
        db.close()
        
    except Exception as e:
        print(f"Could not read from ZODB: {e}")
        
        
if __name__ == "__main__":
    df_data = fetch_csv_data()
    if df_data is not None:
        csv_to_zodb(df_data)
        read_data_from_zodb()