from pymongo import MongoClient
from .consts import RESTRICTED_MACRO_URI, DATABASE_MACRO

client = MongoClient(RESTRICTED_MACRO_URI)
collection_global = client[DATABASE_MACRO]['dataset-global']
collection_test = client[DATABASE_MACRO]['dataset-test']