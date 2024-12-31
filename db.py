from astrapy import DataAPIClient
from dotenv import load_dotenv
import os


load_dotenv()


astra_db_token = os.getenv('ASTRA_DB_TOKEN')
astra_db_endpoint = os.getenv('ASTRA_DB_ENDPOINT')


if not astra_db_token or not astra_db_endpoint:
    raise ValueError("Environment variables ASTRA_DB_TOKEN or ASTRA_DB_ENDPOINT are missing")


client = DataAPIClient(astra_db_token)


db = client.get_database_by_api_endpoint(astra_db_endpoint)


print(f"Connected to Astra DB: {db.list_collection_names()}")