from langchain.tools import Tool
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
import os

from dotenv import load_dotenv
load_dotenv()  # This loads environment variables from .env


# Set up LLM
llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"), model_name = "llama-3.3-70b-versatile")


# Tool 1: Query Analyzer
def analyze_query(query: str) -> str:
    prompt = f"Extract the best search keywords from this question:\n'{query}'\nKeywords:"
    return llm.invoke([HumanMessage(content=prompt)]).content.strip()
    

query_tool = Tool(
    name="Query Analyzer",
    func=analyze_query,
    description="Extracts effective search terms from the user's research question."
)


# Tool 2: DuckDuckGo Web Search
def search_duckduckgo(query: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query, region='wt-wt', safesearch='Moderate', max_results=3)
        return "\n".join([f"{r['title']} - {r['href']}" for r in results])

search_tool = Tool(
    name="Web Search",
    func=search_duckduckgo,
    description="Searches the web using DuckDuckGo and returns top URLs."
)

# Tool 3: Web Scraper
def scrape_url_list(result_text: str) -> str:
    urls = []
    for line in result_text.split("\n"):
        parts = line.split(" - ")
        if len(parts) == 2:
            urls.append(parts[1])
    scraped = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for url in urls:
        try:
            resp = requests.get(url, headers=headers, timeout=8)
            soup = BeautifulSoup(resp.text, "html.parser")
            text = soup.get_text(strip=True)
            scraped.append(text[:2000])
        except Exception as e:
            scraped.append(f"Error scraping {url}: {e}")
    return "\n\n".join(scraped)

scraper_tool = Tool(
    name="Web Scraper",
    func=scrape_url_list,
    description="Scrapes text from a list of URLs."
)


# Tool 4: Content Analyzer
def analyze_content(text: str) -> str:
    prompt = f"Summarize the following content clearly and concisely:\n\n{text}\n\nSummary:"
    return llm.invoke([HumanMessage(content=prompt)]).content.strip()

analyzer_tool = Tool(
    name="Content Analyzer",
    func=analyze_content,
    description="Summarizes raw web content into readable points."
)

# Tool 5: Information Synthesizer
def synthesize(summaries: str) -> str:
    prompt = f"Combine and clean up these multiple content summaries into a single informative answer:\n\n{summaries}\n\nAnswer:"
    return llm.invoke([HumanMessage(content=prompt)]).content.strip()

synth_tool = Tool(
    name="Information Synthesizer",
    func=synthesize,
    description="Synthesizes final research output."
)




