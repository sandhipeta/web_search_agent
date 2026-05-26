# 🤖 AI Web Search Agent using MCP + Groq + Streamlit

An AI-powered real-time web search agent built using MCP (Model Context Protocol), BrightData MCP tools, LangChain, Groq LLM, and Streamlit.

This project demonstrates how Agentic AI systems can interact with external tools to fetch live information from the web and provide intelligent contextual responses.

---

# 🚀 Features

- 🌐 Real-time web search
- 🤖 AI Agent with tool calling
- ⚡ Async execution using AsyncIO
- 🔎 BrightData MCP integration
- 🧠 Groq LLM integration
- 🎨 Streamlit user interface
- 📈 Supports dynamic information retrieval
- 🛠 MCP-based tool orchestration

---

# 🧠 What This Project Can Do

The AI agent can search and retrieve:

- ✈️ Flight information
- 📈 Stock market updates
- 📰 Latest news
- 🌍 Live web data
- 💰 Cryptocurrency prices
- 🏏 Sports updates
- 🔍 General web search queries

Example Queries:

```text
Tell me available flights from Bangalore to Delhi on june 1 2026
```

```text
Top NSE stocks today
```

```text
Latest AI news today
```

```text
Current Bitcoin price
```

---

# 🏗 Architecture

```text
User Query
    ↓
Streamlit UI
    ↓
LangChain Agent
    ↓
Groq LLM
    ↓
BrightData MCP Tools
    ↓
Real-Time Web Data
    ↓
AI Generated Response
```

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- Python
- AsyncIO

## AI / LLM
- LangChain
- Groq LLM

## Tool Integration
- MCP (Model Context Protocol)
- BrightData MCP

---

# 📂 Project Structure

```text
ai-web-search-agent/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-url>
cd ai-web-search-agent
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create `requirements.txt`

```txt
streamlit
langchain
langchain-groq
langchain-mcp-adapters
python-dotenv
```

---

# 🔑 Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
BRIGHT_DATA_API_TOKEN=your_brightdata_api_token
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📸 UI Preview

The Streamlit interface allows users to:

✅ Enter queries  
✅ Trigger AI search agent  
✅ Retrieve real-time information  
✅ View AI-generated responses  

---

# 🧩 Core Concepts Used

This project demonstrates:

- Agentic AI
- Tool Calling
- MCP Architecture
- Async AI Workflows
- LLM Integration
- Real-Time AI Systems
- AI Tool Orchestration
- Web Automation

---

# ⚡ Async Workflow

This project uses asynchronous programming with AsyncIO because MCP tools operate asynchronously.

Key concepts:
- `async`
- `await`
- `ainvoke()`
- `astream()`

---

# 🧠 Why MCP?

MCP (Model Context Protocol) allows AI agents to:

- Use external tools
- Access live data
- Interact with APIs
- Perform browser automation
- Execute intelligent workflows

---

# 📈 Future Improvements

- Multi-agent architecture
- Chat history memory
- Authentication system
- Voice-based AI assistant
- AI travel assistant
- Financial analysis dashboard
- Advanced RAG integration
- Docker deployment
- Cloud hosting

---

# 💡 Key Learnings

Through this project, I learned:

- LangChain Agent Architecture
- MCP Tool Integration
- Async Python Programming
- Real-time AI Systems
- Tool Calling Workflows
- AI Agent Orchestration
- Streamlit Frontend Development

---

# 🧪 Challenges Faced

- Async tool execution
- Tool invocation handling
- Groq function-calling limitations
- MCP streaming workflows
- Agent orchestration debugging

---

# 🎯 Resume Value

This project showcases skills in:

- Generative AI
- Agentic AI
- Full Stack AI Development
- LangChain
- Streamlit
- Async Python
- Tool Calling
- Real-Time AI Applications

---

# 👨‍💻 Author

Siva Kumar

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and connect with me on LinkedIn.

---

# 📜 License

This project is open-source and available under the MIT License.
