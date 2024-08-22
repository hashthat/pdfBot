#!/usr/bin/bash
sudo python3 -m venv venv
sudo source venv/bin/activate

# installs for the virtual environment and chat_bot
sudo pip install streamlit
sudo pip install pypdf2
sudo pip install langchain
sudo pip install python-dotenv
sudo pip install faiss cpu
sudo pip install huggingface_hub
sudo pip install openai
