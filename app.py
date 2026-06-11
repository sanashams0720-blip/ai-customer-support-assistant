import streamlit as st

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support Assistant")

question = st.text_input("Ask a question")

if question:
    st.success(f"You asked: {question}")