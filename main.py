import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Set LangChain tracking settings (optional)
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Chatbot With OpenAI"

# Define prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the user queries."),
        ("user", "{question}"), 
    ]
)

def generate_response(question, api_key, model_name, temperature, max_tokens):
    # Set OpenAI API key
    openai.api_key = api_key

    # Create the ChatOpenAI instance with all parameters
    llm = ChatOpenAI(
        model=model_name,
        openai_api_key=api_key,  
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # Create the LangChain chain
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})

    return answer

# Streamlit UI
st.title("💬 Chatbot With OpenAI")

# Sidebar for API key and settings
st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Model selection
model_name = st.sidebar.selectbox("Select the Model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])

# Temperature and token limits
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Chat interface
st.write("Ask your question below:")
user_input = st.text_input("You:")

if user_input and api_key:
    try:
        response = generate_response(user_input, api_key, model_name, temperature, max_tokens)
        st.success(response)
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
elif user_input:
    st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
else:
    st.info("💡 Enter a query to get started.")
