import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Streamlit app layout
st.title("Chatbot Interface")
st.write("This is a simple chatbot using GPT-3 via the OpenAI API.")

# Initialize session state for conversation history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Input text box for user input
user_input = st.text_input("You:")

# Process the user's input when the form is submitted
if st.button("Send"):
    if user_input:
        # Display user message in chat
        st.session_state['messages'].append({"role": "user", "content": user_input})
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state['messages']
        )
        
        # Extract the response
        bot_response = response.choices[0].message['content']
        
        # Display bot response in chat
        st.session_state['messages'].append({"role": "assistant", "content": bot_response})
        st.text_area("Chatbot:", value=bot_response, height=200, max_chars=None)

# Display the conversation history
st.write("### Conversation History")
for message in st.session_state['messages']:
    role = "You" if message["role"] == "user" else "Chatbot"
    st.write(f"**{role}:** {message['content']}")

