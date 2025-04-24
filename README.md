# web-research-agent


An AI-powered Web Research Agent that automatically searches the web, scrapes useful content, analyzes it, and provides comprehensive answers to user queries.

## 🚀 Features

- 🔎 Extracts keywords from user queries using LLM
- 🌐 Searches the web using DuckDuckGo
- 🕷️ Scrapes web pages with BeautifulSoup
- 🧠 Summarizes and synthesizes content with LLaMA-3 via Groq
- 🖥️ Offers both CLI and Streamlit Web Interface

## 🧱 Architecture Overview

flowchart TD
    A[User Query] --> B[Query Analyzer (LLM)]
    B --> C[Search Tool (DuckDuckGo)]
    C --> D[Web Scraper (BeautifulSoup)]
    D --> E[Content Analyzer (LLM)]
    E --> F[Information Synthesizer (LLM)]
    F --> G[Final Answer]


Project structure
├── main.py           # CLI app
├── app.py            # Streamlit app
├── agent.py          # Core agent logic
├── tools.py          # Tool definitions
├── .env              # API keys 
├── requirements.txt  # Python dependencies



⚙️ Setup
Clone the repository:

git clone https://github.com/yourusername/web-research-agent.git



Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows


Install dependencies:

pip install -r requirements.txt


Create a .env file and add your Groq API Key:

GROQ_API_KEY=your-groq-api-key


Run the CLI version:
python main.py


Or launch the Streamlit UI:
streamlit run app.py


Core Tools Used
Tool
Description
LLM (Groq LLaMA-3)
Keyword extraction, content summarization
DuckDuckGo Search
Fetches top web pages based on keywords
BeautifulSoup
Scrapes and extracts clean text from web pages
Streamlit
Web-based interface for research interaction




