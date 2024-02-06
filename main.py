import streamlit as st

st.title("Talk with database")

question = st.text_input("Question")

if(question):
    # chain = ..
    # answer = chain.run(question)
    answer = "Hello"
    st.header('Answer')
    st.write(answer)
