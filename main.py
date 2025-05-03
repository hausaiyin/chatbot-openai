import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()


## langsmih tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Chatbot With OpenAI"

## Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the user queries."),
        ("user", "Question:{question}"),
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    # Set the OpenAI API key
    openai.api_key = api_key

    # Create the LLM instance with the specified parameters
    llm=ChatOpenAI(model=llm)
    output_parser = StrOutputParser()
    chain= prompt |llm| output_parser
    answer = chain.invoke({"question": question})

    return answer


## Title of the app
st.title("Chatbot With OpenAI")

## Sidebar for Settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

## Dropdown for Model selection
llm = st.sidebar.selectbox("Select the Model",["gpt--4o","gpt-4-turbo", "gpt-4"])

## adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## main interface
st.write("Ask your question")
user_input = st.text_input("You:")

if user_input and api_key:
    response = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(response)

elif user_input:
    st.warning("Please enter a valid OpenAI API key in the sidebar.")
else:
    st.write("Please enter a query to get a response.")
