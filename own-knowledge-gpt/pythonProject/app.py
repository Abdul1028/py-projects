import random
import re
import warnings

import streamlit as st
from utils.snowchat_ui import StreamlitUICallbackHandler, message_func



st.title("snowChat")
st.caption("Talk your way through data")
model = st.radio(
    "",
    options=["✨ GPT-3.5", "♾️ codellama", "👑 Mistral"],
    index=0,
    horizontal=True,
)
st.session_state["model"] = model

INITIAL_MESSAGE = [
    {"role": "user", "content": "Hi!"},
    {
        "role": "assistant",
        "content": "Hey there, Welcome to WIT-Reality ChatBot, your sidekick, ready to chat up with your whatsapp data and fetch answers faster than a snowball fight in summer! ❄️🔍",
    },
]


# Add a reset button
if st.sidebar.button("Reset Chat"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.session_state["messages"] = INITIAL_MESSAGE
    st.session_state["history"] = []



# Initialize the chat messages history
if "messages" not in st.session_state.keys():
    st.session_state["messages"] = INITIAL_MESSAGE

if "history" not in st.session_state:
    st.session_state["history"] = []

if "model" not in st.session_state:
    st.session_state["model"] = model

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    message_func(
        message["content"],
        True if message["role"] == "user" else False,
        True if message["role"] == "data" else False,
    )

callback_handler = StreamlitUICallbackHandler()

import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain_experimental.agents.agent_toolkits import create_csv_agent

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0.5)

agent = create_csv_agent(llm,"my_csv_data.csv",verbose=True)

def append_message(content, role="assistant"):
    """Appends a message to the session state messages."""
    if content.strip():
        st.session_state.messages.append({"role": role, "content": content})


if (
    "messages" in st.session_state
    and st.session_state["messages"][-1]["role"] != "assistant"
):
    user_input_content = st.session_state["messages"][-1]["content"]

    if isinstance(user_input_content, str):
        callback_handler.start_loading_message()

        # result = agent.invoke(
        #     {
        #         "question": user_input_content,
        #         "chat_history": [h for h in st.session_state["history"]],
        #     }
        # )
        print(user_input_content)

        result = agent.invoke(user_input_content)
        print("type is ",type(result))
        print(result["output"])
        append_message(result["output"])
        st.experimental_rerun()
