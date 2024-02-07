# for llm
from langchain_google_genai import GoogleGenerativeAI
# for api key security
import os
from dotenv import load_dotenv
# for databases
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from few_shots import few_shots
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate


# set of pre written suffix and prefix for our prompts
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt

# loading the environment variable
load_dotenv()
    
def get_dbs_chain():
    # using the api for loading the model
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ['GOOGLE_API_KEY'])

    # setting up the database
    db_user = "root"
    db_host = "localhost"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{os.environ['db_password']}@{db_host}/{db_name}",sample_rows_in_table_info=3)

    # Setting up the chain for the llm to answer according to the database using Langchain
    # Note that this chain is the default one where the llm is directly answering from the database 
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose = True)

    # Since the above chain is not good enough in accuracy because the llm is answering on the basis of its own capabilities without looking at the column names or other info
    # Hence we need few shot learning
    # Here, we create a set of question and answers made up of complex queries which the llm may find difficult to answer
    # these are stored in the file few_shots.py

    # Now we will convert these few shots into vector embeddings and store them in vector databases
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

    # creating a blob for our vector database since the few-shots were in the form of a dictionary
    to_vectorise = [" ".join(temp.values()) for temp in few_shots]

    # creating and storing the vector database in ChromaDB
    vector_db = Chroma.from_texts(to_vectorise, embeddings, metadatas=few_shots)

    # to be able to select similar vector from a given database we use the following from langchain
    example_selector = SemanticSimilarityExampleSelector(vectorstore=vector_db, k=2,)

    # Now creating a prompt template to be fed to our final answering chain
    # rather this is the one which the chain will feed to the llm
    prompt_skeleton = PromptTemplate(input_variables=["Question","SQLQuery","SQLResult","Answer"],
                                    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}")

    # setting up the few_shots template 
    few_shot_template = FewShotPromptTemplate(example_selector=example_selector, example_prompt=prompt_skeleton,
                                            prefix=_mysql_prompt,suffix=PROMPT_SUFFIX,
                                            input_variables=["input","table_info","top_k"])

    # Setting up the final Database answering chain which will return the answers
    new_db_chain = SQLDatabaseChain(llm=llm, database=db,prompt=few_shot_template)
    return new_db_chain