import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
import os

# Load API key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 My Chatbot")

# Initialize model
llm = ChatOpenAI(model="gpt-4o-mini")

# Initialize memory in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Savolingizni kiriting:")

if st.button("Yuborish") and user_input.strip():
    messages = []
    for role, content in st.session_state.chat_history:
        messages.append(HumanMessage(content=content) if role == "user" else AIMessage(content=content))
    messages.append(HumanMessage(content=user_input))

    response = llm.invoke(messages)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response.content))

for role, content in st.session_state.chat_history:
    header = "### 🧑 Siz:" if role == "user" else "### 🤖 Bot:"
    st.write(header)
    st.write(content)

if st.checkbox("Show memory"):
    st.write(st.session_state.chat_history)
