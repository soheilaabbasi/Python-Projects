import streamlit as st
from utils import call_ollama


st.image('./images/ChatBot.jpg')
st.title(':zap: ChatBot')
st.caption("A streamlit chatbot powered by :llama: Ollama")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner('Generating response...'):
        msg = call_ollama('qwen3:1.7b', prompt)['response']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

