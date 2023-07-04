#pip install pymongo

from pymongo import MongoClient
import csv
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')  #mongodb://localhost:27017
db = client['test_db']  # Replace with your database name
collection = db['test']  # Replace with your collection name

# Load CSV data into a pandas DataFrame
data = pd.read_csv('Test.csv')

# Convert DataFrame to a list of dictionaries
data_dict = data.to_dict(orient='records')
# Insert the data into the MongoDB collection
collection.insert_many(data_dict)

# Close the MongoDB connection
#client.close()

def insert_data():
    # Get input from user
    id = input("Enter id: ")
    Questions = input("Enter Questions: ")
   

    # Create document
    document = {
        'id': id,
        'Questions': Questions
    }

    # Insert document into collection
    collection.insert_one(document)
    print("Data inserted successfully.")

def delete_data():
    # Get input from user
    id = input("Enter id to delete: ")

    # Delete document(s) from collection
    result = collection.delete_many({'id': id})
    print(f"{result.deleted_count} document(s) deleted.")

def search_data():
    # Get input from user
    id = input("Enter id to search: ")

    # Search for document(s) in collection
    documents = collection.find({'id': id})

    # Display search results
    print("Search Results:")
    for document in documents:
        print(document)

def update_data():
    # Get input from user
    id = input("Enter id to update: ")
    Questions = input("Enter Question: ")

    # Update document(s) in collection
    result = collection.update_many({'id': id}, {'$set': {'Questions': Questions}})
    print(f"{result.modified_count} document(s) updated.")

# Main program loop
while True:
    print("Select an option:")
    print("1. Insert data")
    print("2. Delete data")
    print("3. Search data")
    print("4. Update data")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert_data()
    elif choice == '2':
        delete_data()
    elif choice == '3':
        search_data()
    elif choice == '4':
        update_data()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the MongoDB connection
client.close()
