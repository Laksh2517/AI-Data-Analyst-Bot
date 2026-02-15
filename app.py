import streamlit as st
import requests

st.set_page_config(page_title="AI Data Analyst Assistant")

st.title("🤖 AI Data Analyst Assistant (Ollama - phi3)")
st.markdown("Ask SQL or data-related questions.")

user_input = st.text_area("Enter your question:")

if st.button("Generate Response") and user_input:

    with st.spinner("Thinking..."):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": f"You are a professional data analyst and SQL expert. {user_input}",
                "stream": False
            }
        )

        if response.status_code == 200:
            data = response.json()
            st.success("Response Generated")
            st.write(data["response"])
        else:
            st.error("Error connecting to Ollama. Make sure Ollama is running.")


