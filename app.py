# import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage, AIMessage
# from langchain.store
# import os

# # Page configuration
# st.set_page_config(
#     page_title="AI Chatbot", 
#     page_icon="🤖", 
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Load API key
# try:
#     os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# except:
#     st.error("❌ OpenAI API key not found in secrets. Please add it to continue.")
#     st.stop()

# # Custom ConversationBufferMemory class
# class ConversationBufferMemory:
#     def __init__(self):
#         self.messages = []
    
#     def add_user_message(self, message):
#         self.messages.append(HumanMessage(content=message))
    
#     def add_ai_message(self, message):
#         self.messages.append(AIMessage(content=message))
    
#     def get_messages(self):
#         return self.messages
    
#     def clear(self):
#         self.messages = []
    
#     def get_buffer(self):
#         return "\n".join([f"Human: {msg.content}" if isinstance(msg, HumanMessage) 
#                          else f"AI: {msg.content}" for msg in self.messages])

# # Sidebar for controls
# with st.sidebar:
#     st.title("🎛️ Controls")
    
#     # Model selection
#     model_name = st.selectbox(
#         "Select Model:",
#         ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
#         index=0
#     )
    
#     # Temperature control
#     temperature = st.slider(
#         "Temperature:",
#         min_value=0.0,
#         max_value=2.0,
#         value=0.7,
#         step=0.1,
#         help="Higher values make output more random"
#     )
    
#     # Max tokens
#     max_tokens = st.slider(
#         "Max Tokens:",
#         min_value=50,
#         max_value=4000,
#         value=1000,
#         step=50
#     )
    
#     # Clear chat button
#     if st.button("🗑️ Clear Chat", use_container_width=True):
#         st.session_state.memory.clear()
#         st.session_state.messages = []
#         st.rerun()
    
#     # Show memory toggle
#     show_memory = st.checkbox("🧠 Show Memory Details")

# # Initialize LLM with selected parameters
# @st.cache_resource
# def get_llm(model, temp, max_tok):
#     return ChatOpenAI(
#         model=model,
#         temperature=temp,
#         max_tokens=max_tok
#     )

# llm = get_llm(model_name, temperature, max_tokens)

# # Initialize memory and messages in session state
# if "memory" not in st.session_state:
#     st.session_state.memory = ConversationBufferMemory()

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Main chat interface
# st.title("🤖 AI Chatbot")
# st.markdown("---")

# # Display chat messages
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# # Chat input
# user_input = st.chat_input("Savolingizni kiriting...")

# if user_input:
#     # Add user message to chat
#     st.session_state.messages.append({"role": "user", "content": user_input})
    
#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(user_input)
    
#     # Generate AI response
#     with st.chat_message("assistant"):
#         with st.spinner("Javob tayyorlanmoqda..."):
#             try:
#                 # Add user message to memory
#                 st.session_state.memory.add_user_message(user_input)
                
#                 # Get all messages from memory for context
#                 context_messages = st.session_state.memory.get_messages()
                
#                 # Get response from LLM
#                 response = llm.invoke(context_messages)
                
#                 # Extract content from response
#                 response_content = response.content
                
#                 # Display response
#                 st.markdown(response_content)
                
#                 # Add AI response to memory
#                 st.session_state.memory.add_ai_message(response_content)
                
#                 # Add to session messages for display
#                 st.session_state.messages.append({
#                     "role": "assistant", 
#                     "content": response_content
#                 })
                
#             except Exception as e:
#                 st.error(f"❌ Error generating response: {str(e)}")

# # Show memory details if enabled
# if show_memory:
#     st.markdown("---")
#     st.subheader("🧠 Memory Details")
    
#     with st.expander("Conversation Buffer Memory"):
#         st.text(st.session_state.memory.get_buffer())
    
#     with st.expander("Session Messages"):
#         st.json(st.session_state.messages, expanded=False)
    
#     with st.expander("LangChain Messages"):
#         messages_data = []
#         for msg in st.session_state.memory.get_messages():
#             messages_data.append({
#                 "type": type(msg).__name__,
#                 "content": msg.content
#             })
#         st.json(messages_data, expanded=False)

# # Footer
# st.markdown("---")
# st.markdown(
#     """
#     <div style='text-align: center; color: #666; font-size: 0.8em;'>
#         🤖 Powered by OpenAI & LangChain | Built with Streamlit
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# # Add some custom CSS for better styling
# st.markdown("""
# <style>
#     .stChatMessage {
#         border-radius: 15px;
#         padding: 1rem;
#         margin: 0.5rem 0;
#     }
    
#     .stChatMessage[data-testid="user-message"] {
#         background-color: #e3f2fd;
#     }
    
#     .stChatMessage[data-testid="assistant-message"] {
#         background-color: #f5f5f5;
#     }
    
#     .stButton > button {
#         border-radius: 10px;
#         border: none;
#         background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         font-weight: bold;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
# </style>
# """, unsafe_allow_html=True)


from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

llm = ChatOpenAI(model="gpt-4o")

memory = ConversationBufferWindowMemory(k=2)  # only last 2 turns

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

conversation.predict(input="My favorite food is pizza.")
conversation.predict(input="I live in Tashkent.")
conversation.predict(input="What is my favorite food?")
