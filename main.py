import streamlit as st
from llm_helper import get_dbs_chain

st.title("Talk with database")

chain = get_dbs_chain()

question = st.text_input("Question")

if(question):
    answer = chain.run(question)
    st.header('Answer')
    st.write(answer)
