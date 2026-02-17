#!/usr/bin/env python3
"""Module that returns schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of school documents that have a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search

    Returns:
        list: list of matching school documents
    """
    return list(mongo_collection.find({"topics": topic}))
