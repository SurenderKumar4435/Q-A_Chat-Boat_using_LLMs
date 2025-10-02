import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Load OpenAI API key
api_key = os.getenv("OPEN_API_KEY")

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key)

# Create prompt template
prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me about {topic}")
])

# Parser
output_parser = StrOutputParser()

# Chain
chain = prompt_template | llm | output_parser

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="AI Assistant", layout="centered")

st.title("AI Assistant Q&A Chat-Boat")
st.write("Ask me anything and I’ll try to help!")

# Input box
user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = chain.invoke({"topic": user_input})
        st.success("Answer:")
        st.write(response)
    else:
        st.warning(" Please enter a question first.")
