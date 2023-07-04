# using numpy 
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file using NumPy
data = np.genfromtxt('Test.csv', delimiter=',', skip_header=1, dtype=None, names=True)

# Convert NumPy array to pandas DataFrame
df = pd.DataFrame(data)

# Create a SQLAlchemy engine
engine = create_engine('mysql://root:@localhost/database')

# Store the DataFrame in MySQL
df.to_sql('mytable', engine, if_exists='replace', index=False)