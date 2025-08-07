# 🏠 AI Real Estate Agent Team - Powered by OpenAI's First Open Source Model

> **Historic Moment**: This application showcases OpenAI's **first open-source model in ~5 years** - running locally with Ollama for complete privacy and control!

## 🎯 What Makes This Special?

### 🔓 **OpenAI Goes Open Source Again**
- **First time since GPT-2 (2019)**: OpenAI has released their models as truly open source
- **gpt-oss:20b**: A 20-billion parameter model that runs entirely on your hardware
- **No API calls**: Complete independence from OpenAI's servers
- **Full privacy**: Your data never leaves your machine
- **Zero costs**: No per-token charges or subscription fees

### 🏡 **Intelligent Real Estate Analysis**
Transform property hunting with AI agents that:
- 🔍 **Search multiple real estate websites** (Zillow, Realtor.com, Trulia, Homes.com)
- 📊 **Analyze market trends** and neighborhood insights
- 💰 **Evaluate investment potential** for each property
- 🤖 **Coordinate multiple AI agents** for comprehensive analysis
- 🆓 **Work completely offline** (Local Web Scraping mode)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed
- At least 16GB RAM (recommended for gpt-oss:20b)

### Installation

1. **Clone and setup**:
```bash
git clone <your-repo>
cd openai_oss
pip install -r requirements.txt
```

2. **Install Ollama and pull OpenAI's model**:
```bash
# Install Ollama from https://ollama.ai/
# Then pull OpenAI's open source model
ollama pull gpt-oss:20b
```

3. **Run the application**:
```bash
streamlit run main.py
```

---

## 🔧 Configuration Options

### 🤖 **AI Model Setup**

#### Local Setup (Single Machine)
```bash
ollama serve
# App will automatically connect to http://localhost:11434
```

#### Remote Setup (Powerful GPU Machine)
**On your powerful PC:**
```bash
export OLLAMA_HOST=0.0.0.0:11434  # Linux/Mac
# OR
set OLLAMA_HOST=0.0.0.0:11434     # Windows
ollama serve
```

**In the app:**
- Set Ollama Host URL to `http://YOUR_GPU_PC_IP:11434`
- Test connection using the built-in connection tester

### 🔍 **Search Methods**

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **Local Web Scraping** | 🆓 Free, Private | Rate limits | Privacy-focused users |
| **Firecrawl API** | 🎯 Reliable, Fast | Requires API key | Production use |

---

## 🏗️ Architecture

### Multi-Agent System
```
🔍 Property Search Agent
    ↓
📊 Market Analysis Agent  
    ↓
💰 Property Valuation Agent
    ↓
🤖 Final Synthesis & Recommendations
```

### Tech Stack
- **Frontend**: Streamlit (Interactive web interface)
- **AI Framework**: Agno (Multi-agent coordination)
- **LLM**: OpenAI's gpt-oss:20b via Ollama
- **Web Scraping**: BeautifulSoup4 + Google Search
- **API Integration**: Firecrawl (optional)

---

## 📊 Features

### 🏠 **Property Search**
- Multi-website search across top real estate platforms
- Customizable search criteria (location, budget, property type)
- Real-time property extraction and analysis

### 📈 **Market Analysis**
- Neighborhood trend analysis
- Buyer's vs seller's market insights
- Investment outlook predictions

### 💎 **Property Valuation**
- Individual property assessments
- Investment potential scoring
- Actionable recommendations

### 🎨 **Professional UI**
- Clean, responsive design
- Tabbed property views
- Downloadable analysis reports
- Real-time progress tracking

---

## 🌟 Why This Matters

### **The Open Source Revolution**
OpenAI's decision to release gpt-oss:20b as open source represents a significant shift:

1. **Democratizing AI**: Advanced language models accessible to everyone
2. **Privacy First**: No data sent to external servers
3. **Cost Effective**: No ongoing API fees
4. **Customizable**: Full control over model behavior
5. **Transparent**: Open weights and architecture

### **Real Estate Transformation**
This application demonstrates how open-source AI can:
- **Level the playing field** for individual property investors
- **Provide institutional-grade analysis** without institutional costs
- **Maintain complete privacy** of your property search data
- **Work offline** without internet dependencies

---

## 🔒 Privacy & Security

- ✅ **100% Local Processing**: All AI inference happens on your machine
- ✅ **No Data Transmission**: Property data never sent to external services
- ✅ **Open Source**: Full code transparency
- ✅ **Self-Hosted**: Complete control over your infrastructure

---

## 📋 Requirements

```txt
streamlit>=1.28.0
agno>=0.5.0
ollama>=0.1.0
beautifulsoup4>=4.12.0
requests>=2.31.0
googlesearch-python>=1.2.3
firecrawl-py>=0.0.8
pydantic>=2.0.0
python-dotenv>=1.0.0
```

---

## 🚀 Usage Examples

### Basic Property Search
```python
# Search for properties in San Francisco
city = "San Francisco"
state = "CA"
budget_range = "$800K - $1.2M"
property_type = "Condo"
```

### Remote AI Setup
```bash
# On powerful GPU machine (192.168.1.100)
export OLLAMA_HOST=0.0.0.0:11434
ollama serve

# In application
OLLAMA_HOST = "http://192.168.1.100:11434"
```

---

## 🤝 Contributing

This project showcases the potential of OpenAI's first open-source model in years. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- **OpenAI** for releasing their first open-source model in ~5 years
- **Ollama** for making local LLM deployment effortless
- **Streamlit** for the amazing web framework
- **Real Estate Community** for inspiring this application

---

## 📞 Support

Having issues? Check out:

1. **Connection Problems**: Use the built-in Ollama connection tester
2. **Model Issues**: Ensure `gpt-oss:20b` is properly downloaded
3. **Performance**: Consider using a GPU-enabled machine for faster inference

---

**🎉 Welcome to the new era of open-source AI - where powerful language models run on YOUR hardware, under YOUR control!**

---

*Last updated: August 2025 - Celebrating OpenAI's return to open source!*
