from dotenv import load_dotenv
import os

load_dotenv()

RESTRICTED_MACRO_URI = os.getenv("RESTRICTED_MACRO_URI")
DATABASE_MACRO = 'database-macro'