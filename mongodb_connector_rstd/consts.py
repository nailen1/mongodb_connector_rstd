from dotenv import load_dotenv
import os

load_dotenv()

RESTRICTED_MACRO_URI = os.getenv("RESTRICTED_MACRO_URI")
RESTRICTED_CAPSTONE_URI = os.getenv("RESTRICTED_CAPSTONE_URI")
DATABASE_MACRO = 'database-macro'
DATABASE_CAPSTONE = 'database-capstone'