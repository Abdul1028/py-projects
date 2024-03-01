import streamlit as st
from pymongo import MongoClient
from bson import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["your_collection_name"]

# Function to perform CRUD operations

def create_record(data):
    return collection.insert_one(data)

def read_records():
    return collection.find()

def update_record(record_id, new_data):
    collection.update_one({"_id": ObjectId(record_id)}, {"$set": new_data})

def delete_record(record_id):
    collection.delete_one({"_id": ObjectId(record_id)})

# Streamlit App

def main():
    st.title("MongoDB CRUD App")

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Add Record")
        name = st.text_input("Name")
        age = st.number_input("Age")
        if st.button("Add"):
            record = {"name": name, "age": age}
            create_record(record)
            st.success("Record added successfully!")

    elif choice == "Read":
        st.subheader("View Records")
        records = read_records()
        for record in records:
            st.write(f"Name: {record['name']}, Age: {record['age']}")

    elif choice == "Update":
        st.subheader("Update Record")
        records = read_records()
        record_id = st.selectbox("Select Record", [str(record["_id"]) for record in records])
        selected_record = collection.find_one({"_id": ObjectId(record_id)})
        if selected_record:
            new_name = st.text_input("New Name", value=selected_record["name"])
            new_age = st.number_input("New Age", value=selected_record["age"])
            if st.button("Update"):
                update_record(record_id, {"name": new_name, "age": new_age})
                st.success("Record updated successfully!")

    elif choice == "Delete":
        st.subheader("Delete Record")
        records = read_records()
        record_id = st.selectbox("Select Record", [str(record["_id"]) for record in records])
        if st.button("Delete"):
            delete_record(record_id)
            st.success("Record deleted successfully!")

if __name__ == "__main__":
    main()
