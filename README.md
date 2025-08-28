# 🌟 MCP Multi-Agent Server

> **A sophisticated Model Context Protocol (MCP) server providing AI-powered tools through a unified interface with a modern Streamlit web application.**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-1.13.1+-green.svg)](https://modelcontextprotocol.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.48+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


## ✨ Features

### 🔧 Core Tools

- **🌤️ Weather Service** ⚡ Real-time weather information using OpenWeatherMap API
- **🧮 Advanced Math Engine** 🧮 Mathematical operations and percentage calculations
- **💱 Currency Converter** 💰 Real-time currency conversion using ExchangeRate API
- **📚 Research Summarizer** 🔬 Academic paper summaries from arXiv
- **📖 Dictionary Tool** 📖 Word definitions and meanings

## 🛠️ Installation

### Prerequisites

- 🐍 Python 3.12 or higher
- 🌤️ OpenWeatherMap API key (for weather service)
- 🤖 Groq API key (for LLM integration)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mcp-server
   ```

2. **Create and activate virtual environment**
   ```bash
   # Using uv (recommended)
   uv venv
   uv venv activate
   
   # Or using traditional venv
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "OPENWEATHER_API_KEY=your_api_key_here" > .env
   echo "GROQ_API_KEY=your_groq_api_key_here" >> .env
   ```

5. **Run the application**
   ```bash
   streamlit run client.py
   ```
## 📖 Usage

### 🌐 Web Interface

1. 🚀 **Launch the app**: `streamlit run client.py`
2. 🌐 **Open your browser** and navigate to the provided URL
3. 💬 **Start chatting** with the AI agent
4. ❓ **Ask questions** like:
   - 🌤️ "What's the weather in London?"
   - 🧮 "Calculate 25% of 200"
   - 💰 "Convert 100 USD to EUR"
   - 🔬 "Summarize research on machine learning"
   - 📖 "Define the word 'serendipity'"



## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ using modern AI technologies**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-1.13.1+-green.svg)](https://modelcontextprotocol.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.48+-red.svg)](https://streamlit.io)

</div>
