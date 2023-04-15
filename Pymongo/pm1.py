#!/usr/bin/env python3
##this function list all documents of a collection
import pymongo


def list_all(mongo_collection):
    """Return list of all docs in collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
