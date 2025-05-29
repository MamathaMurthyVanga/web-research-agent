from tools import query_tool, search_tool, scraper_tool, analyzer_tool, synth_tool
from agent import ResearchAgent
from tools import llm



# print("Testing LLM invoke with sample prompt...")
# res=llm.invoke("Ques")
# print("----------------",res)


if __name__ == "__main__":
    user_query = input("Enter your research question: ")

    agent = ResearchAgent(
        query_tool=query_tool,
        search_tool=search_tool,
        scraper_tool=scraper_tool,
        analyzer_tool=analyzer_tool,
        synth_tool=synth_tool
    )

    result = agent.run(user_query)
    print("\nFinal Answer:\n",result)

    