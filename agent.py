class ResearchAgent:
    def __init__(self, query_tool, search_tool, scraper_tool, analyzer_tool, synth_tool):
        self.query_tool = query_tool
        self.search_tool = search_tool
        self.scraper_tool = scraper_tool
        self.analyzer_tool = analyzer_tool
        self.synth_tool = synth_tool

    def run(self, user_query: str) -> str:
        # print("Step 1: Analyzing query for keywords...")
        keywords = self.query_tool.func(user_query)
        # print(f"Extracted Keywords: {keywords}")

        # print("Step 2: Performing web search...")
        import re

        # Extract one usable search phrase from the LLM-generated keyword list
        phrases = re.findall(r"-\s+'([^']+)'", keywords)
        query_for_search = phrases[0] if phrases else user_query  # Fallback to the original question

        search_results = self.search_tool.func(query_for_search)
        # print(f"Search Results:\n{search_results}")

        # print("Step 3: Scraping web pages...")
        raw_text = self.scraper_tool.func(search_results)
        # print(f"Scraped Text (truncated):\n{raw_text[:500]}...")

        # print("Step 4: Analyzing content...")
        summarized = self.analyzer_tool.func(raw_text)
        # print(f"Summary:\n{summarized}")

        # print("Step 5: Synthesizing final answer...")
        final_answer = self.synth_tool.func(summarized)
        return final_answer

