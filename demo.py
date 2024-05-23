import streamlit as st

st.title("MoCk BoT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "mockbob":
        cm = st.chat_message(message["role"],  avatar="mockbob.jpg")
    else:
        cm = st.chat_message(message["role"])

    with cm:
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    if prompt.strip() == "/clear":
        st.session_state.messages = []
        st.rerun()
    else:
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = ''.join([c.lower(), c.upper()][i % 2 == 0] for c, i in zip(prompt, range(1, len(prompt) + 1)))
        # Display assistant response in chat message container
        with st.chat_message("mockbob", avatar="mockbob.jpg"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "mockbob", "content": response})
