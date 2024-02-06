# for llm
from langchain.llms import GooglePalm
# for api key security
import os
from dotenv import load_dotenv
# for databases
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# loading the environment variable
load_dotenv()
# using the api for loading the model
llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.1)

# setting up the database
db_user = "root"
db_password = "sql#pass"
db_host = "localhost"
db_name = "atliq_tshirts"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)