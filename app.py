import os
import asyncio
import streamlit as st

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

load_dotenv()

st.set_page_config(
    page_title="AI Web Search Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Web Search Agent")
st.write("Search real-time information using MCP + BrightData + Groq")

# User Input
query = st.text_area(
    "Enter your query",
    placeholder="Example: Tell me available flights from Bangalore to Delhi on june 1 2026"
)

# Button
search_button = st.button("Search")


async def get_agent_response(user_query):

    client = MultiServerMCPClient(
        {
            "bright_data": {
                "command": "npx",
                "args": ["@brightdata/mcp"],
                "env": {
                    "API_TOKEN": os.getenv("BRIGHT_DATA_API_TOKEN"),
                    "BROWSER_ZONE": os.getenv(
                        "BROWSER_ZONE",
                        "scraping_browser"
                    )
                },
                "transport": "stdio",
            },
        }
    )

    tools = await client.get_tools()

    model = init_chat_model(
        model="groq:llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    agent = create_agent(
        model,
        tools,
        system_prompt="""
        You are a web search agent with access to BrightData MCP tools.
        Use tools to fetch latest and real-time information.
        """
    )

    response = await agent.ainvoke(
        {
            "messages": user_query
        }
    )

    return response["messages"][-1].content


# Run Agent
if search_button:

    if query.strip() == "":
        st.warning("Please enter a query")
    else:

        with st.spinner("Searching latest information..."):

            try:
                result = asyncio.run(
                    get_agent_response(query)
                )

                st.subheader("Agent Response")
                st.write(result)

            except Exception as e:
                st.error(f"Error: {str(e)}")