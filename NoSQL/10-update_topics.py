#!/usr/bin/env python3
"""Write a Python function that inserts a new document in a collection based"""

def update_topics(mongo_collection, name, topics):
    """update"""
    return mongo_collection.update_many({"name": name}, {"$set":{"topics": topics}})
