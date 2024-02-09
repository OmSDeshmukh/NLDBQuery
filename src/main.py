import streamlit as st
from llm_helper import llm_infer

st.title("Talk with database")

# llm_infer = llm_infer()

question = st.text_input("Question")

if(question):
    answer = llm_infer(question)
    st.header('Answer')
    st.write(answer)