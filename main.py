import streamlit as st
from llm_helper import get_dbs_chain

st.title("Talk with database")

question = st.text_input("Question")

if(question):
    chain = get_dbs_chain()
    answer = chain.run(question)
    st.header('Answer')
    st.write(answer)
    
