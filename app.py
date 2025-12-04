import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# Load API key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 My Chatbot")

# Initialize model
llm = ChatOpenAI(model="gpt-4o-mini")

# Initialize memory in session_state
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory
)

user_input = st.text_input("Savolingizni kiriting:")

if st.button("Yuborish") and user_input.strip():
    response = conversation.predict(input=user_input)
    st.write("### 🧑 Siz:")
    st.write(user_input)

    st.write("### 🤖 Bot:")
    st.write(response)

if st.checkbox("Show memory"):
    st.write(st.session_state.memory.buffer)
