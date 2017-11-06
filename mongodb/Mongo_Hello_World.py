from pymongo import MongoClient
import datetime

marathon_public_url = "54.148.237.235"
mongo_port = 10109

client = MongoClient(marathon_public_url, mongo_port)

db = client.test_database

post1 = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

post2 = {"author": "Mark",
        "text": "It was the best of times it was the worst of times...",
        "tags": ["mongodb", "python", "pymongo","literature"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
print(posts)
post_id = posts.insert_one(post1).inserted_id
print(post_id)
post_id = posts.insert_one(post2).inserted_id

posts = db.posts


print (posts.find_one({"author":"Mark"}))