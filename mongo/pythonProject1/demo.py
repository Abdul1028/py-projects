from pymongo import MongoClient

# Replace 'your_username', 'your_password', and 'your_cluster_url' with your MongoDB credentials
connection_string = "mongodb+srv://adwaitthakur100:Adwait%40100@cluster0.ybcyebv.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoClient object
client = MongoClient(connection_string)

name = "test"
new = client[name]
collection = new["adwait"]
collection.insert_one({'abdul':'1234'})
print("data ins")

# Now you can perform operations on the collection, such as inserting or querying data