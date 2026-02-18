# ✍️ Smart Writing Assistant

AI-powered writing assistant that rewrites your text in different styles.

## Features

- **Professional Mode**: Make text formal and business-appropriate
- **Friendly Mode**: Make text casual and warm
- **Fix Grammar**: Correct spelling and grammar errors
- **Make Shorter**: Condense text while keeping key points

## Tech Stack

- Streamlit (UI)
- Groq API (LLM)
- Llama 3.3 70B (Model)

## Live Demo

🔗 [Try it here](https://smart-writer-xyz.streamlit.app) _(coming soon)_

## Run Locally
```bash
# Clone repo
git clone https://github.com/mindelias/smart-writer.git
cd smart-writer

# Install dependencies
uv sync

# Add Groq API key
mkdir .streamlit
echo 'GROQ_API_KEY = "your-key-here"' > .streamlit/secrets.toml

# Run
uv run streamlit run app.py
```

## Project Structure
```
smart-writer/
├── app.py          # Main Streamlit app
├── prompts.py      # Rewriting mode prompts
└── requirements.txt
```

## Author

Built by Shotade as Week 1 project for LLM Engineering course.