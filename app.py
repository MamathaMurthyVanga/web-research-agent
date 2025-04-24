import streamlit as st
from tools import query_tool, search_tool, scraper_tool, analyzer_tool, synth_tool
from agent import ResearchAgent

# Initialize the agent
agent = ResearchAgent(
    query_tool=query_tool,
    search_tool=search_tool,
    scraper_tool=scraper_tool,
    analyzer_tool=analyzer_tool,
    synth_tool=synth_tool
)

# Streamlit UI
st.set_page_config(page_title="AI Research Assistant", layout="wide")
st.title("Web Research Agent")

user_query = st.text_input("Enter your research question:", "")

if st.button("Run Research"):
    if user_query.strip() == "":
        st.warning("Please enter a research question.")
    else:
        with st.spinner("Researching... Please wait."):
            result = agent.run(user_query)
            st.success("Research Complete!")
            st.markdown("### Final Answer:")
            st.write(result)
