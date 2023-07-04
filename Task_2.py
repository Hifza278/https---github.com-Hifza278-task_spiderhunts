#pip install numpy sqlalchemy mysql-connector-python
#pip install mysql-connector-python
import mysql.connector
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, Float, String, MetaData
# Read the CSV file using NumPy
data = np.genfromtxt('Test.csv', delimiter=',', skip_header=1, dtype=None, names=True)

df = pd.DataFrame(data)

#engine = create_engine('mysql+mysqlconnector://[user]:[pass]@[host]:[port]/[schema]', echo=False)

engine = create_engine('mysql+mysqlconnector://root:123456789@localhost:3306/testdb', echo=False)

# Create a cursor object
#cursor = engine.cursor()

df.to_sql('my_table',engine,if_exists='replace',index='Fasle')

print('done')
db = mysql.connector.connect(
host="localhost",
user="root",
password="123456789",
database="testDB"
)
# Create a cursor object
cursor = db.cursor()

# Function to insert data into the table
def insert_data():
    # Prepare the SQL query
    id = int(input("id "))
    question =input("Questions: ")
    sql = "INSERT INTO my_table (id, Questions) VALUES (%s, %s)"
    values = (id,question)
    #print(sql)
    # Execute the query
    cursor.execute(sql, values)
    # Commit the changes
    db.commit()
    # Print the number of rows affected
    print(cursor.rowcount, "record inserted.")

# Function to delete data from the table
def delete_data():
    #id = int(input("Enter ID of the data to delete: "))
    question = input("Enter name to search question: ")
    sql = "DELETE FROM my_table WHERE Questions = %s"
    adr = (question, )
    cursor.execute(sql, adr)
    db.commit()
    print(cursor.rowcount, "record(s) deleted")

# Function to search for data in the table
def search_data():
    question = input("Enter name to search question: ")
    sql ="SELECT * FROM my_table WHERE Questions = %s"
    val =(question,)
    search =cursor.execute(sql, val)
    rows = search.fetchall()
    if rows:
        for row in rows:
            print("ID:", row[0])
            print("Questions:", row[1])
    else:
        print("No data found.")

# Function to update data in the table
def update_data():
    question = input("Enter new question: ")
    sql = "UPDATE my_table SET question = %s WHERE question = %s"
    val =  (question,)
    cursor.execute(sql,val)
    db.commit()
    print(cursor.rowcount, "Data updated successfully.")

# Main program loop
while True:
    print("Menu:")
    print("1. Insert data")
    print("2. Delete data")
    print("3. Search data")
    print("4. Update data")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        insert_data()
    elif choice == "2":
        delete_data()
    elif choice == "3":
        search_data()
    elif choice == "4":
        update_data()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
