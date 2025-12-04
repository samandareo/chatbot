import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# Load API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 My Streamlit Chatbot")

# LangChain LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Session-based memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=False
)

# Chat input
user_input = st.text_input("Savolingizni kiriting:", "")

if st.button("Yuborish") and user_input.strip() != "":
    response = conversation.predict(input=user_input)

    # Display chat history
    st.write("### 🧑 Siz:")
    st.write(user_input)

    st.write("### 🤖 Bot:")
    st.write(response)

# Optionally show conversation history
if st.checkbox("Show memory"):
    st.write(st.session_state.memory.buffer)
