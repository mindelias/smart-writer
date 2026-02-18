# app.py

import streamlit as st
from openai import OpenAI
from prompts import MODES

# Configure Ollama client
# client = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="not-needed"
# )

# Using Groq API for deployment (replace with your actual API key)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=st.secrets["GROQ_API_KEY"]  # Stored in Streamlit Cloud
)

# Page config
st.set_page_config(
    page_title="Smart Writing Assistant",
    page_icon="✍️",
    layout="wide"
)

# Title
st.title("✍️ Smart Writing Assistant")
st.markdown("Paste your text and choose how you want to rewrite it")

# Layout: Two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Text")
    user_text = st.text_area(
        "Paste your text here:",
        height=300,
        placeholder="Type or paste your text here..."
    )
    
    # Mode selector
    mode = st.selectbox(
        "Rewriting Mode:",
        options=list(MODES.keys()),
        format_func=lambda x: f"{x} - {MODES[x]['description']}"
    )
    
    # Rewrite button
    rewrite_btn = st.button("✨ Rewrite", type="primary", use_container_width=True)

with col2:
    st.subheader("Rewritten Text")
    
    # Placeholder for output
    output_container = st.empty()

# Process when button clicked
if rewrite_btn:
    if not user_text.strip():
        st.error("Please enter some text to rewrite")
    else:
        with st.spinner("Rewriting..."):
            try:
                # Get system prompt for selected mode
                system_prompt = MODES[mode]["system_prompt"]
                
                # Create messages
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text}
                ]
                
                # Call Ollama
                response = client.chat.completions.create(
                    # model="llama2",
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.7
                )
                
                # Extract rewritten text
                rewritten_text = response.choices[0].message.content
                
                # Display in right column
                with col2:
                    st.text_area(
                        "Result:",
                        value=rewritten_text,
                        height=300,
                        disabled=True
                    )
                    
                    # Copy button
                    st.code(rewritten_text, language=None)
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Make sure Ollama is running: `ollama serve`")

# Footer
st.markdown("---")
st.markdown("Powered by Ollama (llama2) running locally")