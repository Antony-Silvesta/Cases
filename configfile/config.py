from pymongo import MongoClient

def setup_db():
    mongo_uri = "mongodb://127.0.0.1:27017/sampleupload"
    client = MongoClient(mongo_uri)
    db = client['sampleupload']
    collection = db['users']  # Use the collection where you're storing users

    test_data = [
        {
            "_id": "673c3d642c394f61b7c8e5dc",
            "username": "demo",
            "password": "demo",
            "is_valid": True,
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/"
        },
        {
            "_id": "673c458090640cefa0757532",
            "username": "demo",
            "password": "demo",
            "is_valid": True,
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/"
        }
    ]

    # Remove any existing data to prevent duplicates
    collection.delete_many({})
    collection.insert_many(test_data)

    print("Database setup complete.")

if __name__ == "__main__":
    setup_db()
