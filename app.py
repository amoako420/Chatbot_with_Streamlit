import streamlit as st
from env import api_key
from google import genai 

# Initialize the Gemini client
api_key = api_key()
client = genai.Client(api_key=api_key)

# Set up the Streamlit app
st.title("Gemini 2.0 Flash")

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate text using the Gemini model
def generate_text(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", contents=prompt
        )
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Enter your message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate a response from the model
    with st.spinner("Gemini is thinking..."):
        response = generate_text(prompt)
    
    # Add model response to chat history
    if response:
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display model response in chat
        with st.chat_message("assistant"):
            st.markdown(response)
    else:
        st.warning("No response received from the model. Try again.")
        
        

st.write("Made by Amoako")