import datetime
import uuid
from pymongo import MongoClient
from bson.objectid import ObjectId

# create client
client = MongoClient("localhost", 27017)

# get/create database
db = client.ktechhub
# db = client.ktech_hub ##this works
# db = client['ktech-hub'] ##this works
print(client.list_database_names())

# create/get collection
collection = db.posts
print(db.list_collection_names())

# # Insert one
post1 = {
    "title": "Post 1",
    "description": "This is post #1",
    "created_at": datetime.datetime.now(),
    "comments": [],
}
inserted_post1 = collection.insert_one(post1)
print(inserted_post1.inserted_id)

post2 = {
    "title": "Post 2",
    "description": "This is post #2",
    "created_at": datetime.datetime.now(),
    "comments": [
        {"name": "John", "message": "Nice post."},
        {"name": "Doe", "message": "I love this!"},
    ],
}
inserted_post2 = collection.insert_one(post2)
print(inserted_post2.inserted_id)

# Insert Many
posts = [
    {
        "title": "Post 3",
        "description": "This is post #3",
        "created_at": datetime.datetime.now(),
        "comments": [
            {"name": "John", "message": "Nice post."},
            {"name": "Doe", "message": "I love this!"},
        ],
    },
    {
        "title": "Post 4",
        "description": "This is post #4",
        "created_at": datetime.datetime.now(),
        "comments": [
            {"name": "John", "message": "Nice post."},
            {"name": "Doe", "message": "I love this!"},
            {"name": "Dan", "message": "I hate this!"},
        ],
    },
]
inserted_posts = collection.insert_many(posts)
print(inserted_posts.inserted_ids)

# find one
print(collection.find_one())

# find many
for post in collection.find():
    print(post)

query = {"title": "Post 1"}
for post in collection.find(query):
    print(post)

# Counting
print(collection.count_documents({}))
print(collection.count_documents(query))

# Update Post
query = {"_id": ObjectId("642fc3e21f31fa6d8b998d14")}
update_post = {"$set": {"title": "Post 1 Edited"}}
collection.update_one(query, update_post)
updated_post = collection.find_one(query)
print(updated_post)

## Delete Post
delete_item = {"_id": ObjectId("642fc46dfec31babedd78034")}
collection.delete_one(delete_item)

query = {"title": "Post 1"}
for post in collection.find(query):
    print(post)
