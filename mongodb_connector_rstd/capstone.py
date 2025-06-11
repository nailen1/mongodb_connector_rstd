from pymongo import MongoClient
from .consts import RESTRICTED_CAPSTONE_URI, DATABASE_CAPSTONE

client_capstone = MongoClient(RESTRICTED_CAPSTONE_URI)
database_capstone = client_capstone[DATABASE_CAPSTONE]
collection_agent_01 = database_capstone['collection-agent-01']
collection_agent_02 = database_capstone['collection-agent-02']