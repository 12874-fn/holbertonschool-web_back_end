#!/usr/bin/env python3
"""Module to list all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return a list of all documents in the collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list: list of documents, or [] if collection is empty
    """
    return list(mongo_collection.find())
