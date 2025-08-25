#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 19:59:41 2025

@author: christopherod_snhu
"""

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='SNHU1234'):
        """
        Initialize connection to MongoDB.
        This class connects to the AAC database and the animals collection using the aacuser credentials.
        """
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32612
        DB = 'AAC'
        COL = 'animals'

        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
            self.database = self.client[DB]
            self.collection = self.database[COL]
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

# Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except PyMongoError as e:
                print(f"Insert failed: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Method to implement the R in CRUD.
    def read(self, query):
        if query is None:
            raise ValueError("Query is null.")
            
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read error: {e}")
            return []
        
# Method to implement the U in CRUD.
    def update(self, query, update_data):
        if query is None or update_data is None:
            raise ValueError("Query and update must not be null.")
        
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update failed: {e}")
            return 0
        

# Method to implement the D in CRUD.
    def delete(self, query):
        if query is None:
            raise ValueError("Query is null")
        
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete failed: {e}")
            return 0