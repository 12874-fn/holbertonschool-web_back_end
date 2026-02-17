#!/usr/bin/env python3
"""Module that inserts a document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in mongo_collection using kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: fields to insert

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
