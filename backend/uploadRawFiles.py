import os
from pymongo import MongoClient

# Step 1: Connect to MongoDB Cluster
def connect_to_mongo(uri):
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error: {e}")
    return client

# Step 2: Create a function to upload a file to its corresponding collection
def upload_file(file_path, collection):
    try:
        filename = os.path.basename(file_path)
        with open(file_path, "rb") as file:
            file_data = file.read()
            # Insert file into the corresponding collection
            document = {
                "filename": filename,
                "data": file_data
            }
            collection.insert_one(document)
        print(f"{filename} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload {filename}: {e}")

# Step 3: Function to process all files and upload them to their respective collections based on file extensions
def upload_files_by_extension(folder_path, db):
    try:
        # Loop through all files in the folder and subfolders
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Extract the file extension
                file_extension = file.split('.')[-1].lower()

                # Define collection name based on file extension
                collection_name = file_extension

                # Get the collection from MongoDB, dynamically named after the extension
                collection = db[collection_name]

                # Full path to the file
                file_path = os.path.join(root, file)

                # Upload the file to the corresponding collection
                upload_file(file_path, collection)

    except Exception as e:
        print(f"Error while processing files: {e}")

# Example usage
if __name__ == "__main__":
    # MongoDB connection URI
    uri = os.getenv("MONGODB_URI")  # Use the environment variable for the URI

    # Connect to MongoDB and select the 'Files' database
    client = connect_to_mongo(uri)
    db = client["Files"]

    # Specify the folder containing the files
    folder_to_upload = r"C:\Users\mahan\OneDrive\Desktop\GenaiusRemastered\Data"

    # Upload all files in the folder based on their file extensions
    upload_files_by_extension(folder_to_upload, db)
