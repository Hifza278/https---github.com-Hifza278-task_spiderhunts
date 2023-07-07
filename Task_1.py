import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file using NumPy
data = np.genfromtxt('Test.csv', delimiter=',', skip_header=1, dtype=None, names=True)

# Convert NumPy array to pandas DataFrame
df = pd.DataFrame(data)

try:
    # Create a SQLAlchemy engine
    engine = create_engine('mysql://root:@localhost/test_database')
except: 
    print("database not connected")

# Store the DataFrame in MySQL
df.to_sql('mytable', engine, if_exists='replace', index=False)

