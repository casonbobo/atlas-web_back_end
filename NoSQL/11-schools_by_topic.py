#!/usr/env/bin python3
"""Write a function that returns the list of school having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """return a list of school"""
    return mongo_collection.find({"topics": topic})
