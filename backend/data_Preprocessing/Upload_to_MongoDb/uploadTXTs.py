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

# Step 2: Create a function to upload a PDF file
def upload_pdf(file_path, collection):
    try:
        filename = os.path.basename(file_path)
        with open(file_path, "rb") as file:
            file_data = file.read()
            # Insert file into the pdfs collection
            document = {
                "filename": filename,
                "data": file_data 
            }
            collection.insert_one(document)
        print(f"{filename} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload {filename}: {e}")

# Step 3: Function to loop through a folder and upload only PDF files
def upload_pdfs_from_folder(folder_path, collection):
    try:
        # Loop through all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('.txt'): 
                    file_path = os.path.join(root, file)  
                    upload_pdf(file_path, collection)  
    except Exception as e:
        print(f"Error while reading files from folder: {e}")

# Example usage
if __name__ == "__main__":
    # MongoDB connection URI
    uri = "mongodb+srv://dibyajyoti:Password123@atlascluster.fi2qsez.mongodb.net/PROJECT0?retryWrites=true&w=majority"

    # Connect to MongoDB and select the 'Files' database
    client = connect_to_mongo(uri)
    db = client["FIles"]

    # Create or get the 'pdfs' collection
    pdfs_collection = db["TXTs"]

    # Specify the folder containing the PDF files
    folder_to_upload = "C:/Users/mahan/OneDrive/Desktop/GenAIus/Files/TXTs"  

    # Upload all the PDF files in the folder
    upload_pdfs_from_folder(folder_to_upload, pdfs_collection)
