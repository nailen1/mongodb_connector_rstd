from pymongo import MongoClient
from .consts import RESTRICTED_MACRO_URI, DATABASE_MACRO

client_macro = MongoClient(RESTRICTED_MACRO_URI)
database_macro = client_macro[DATABASE_MACRO]
collection_global = database_macro['dataset-global']
collection_test = database_macro['dataset-test']