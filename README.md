# 
🛡️ AI Cybersecurity Agent

An educational **Agentic AI cybersecurity assistant** demonstrating a defensive workflow:

**User Task → Planning → Security Analysis → Recommendations → Report**

## Features
- Agent-style task planning
- Defensive security risk identification
- Phishing, authentication, secrets, injection, XSS, and network exposure checks
- Optional OpenAI-powered analysis
- Downloadable security report
- Streamlit interface
- `.env` configuration

## Installation
```bash
git clone https://github.com/rubabf232-svg/AI-Cybersecurity-Agent.git
cd AI-Cybersecurity-Agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## API Key
Copy `.env.example` to `.env` and add your key:
```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```
The project also works without an API key using its built-in defensive rules.

## Run
```bash
streamlit run app.py
```

## Example Tasks
- Analyze a suspicious phishing email
- Review possible exposed API keys
- Assess an authentication issue
- Review potential SQL injection indicators
- Analyze suspicious network exposure

## Agentic AI Concepts
- Task decomposition
- Agent planning
- Rule/tool selection
- Context-aware analysis
- AI reasoning layer
- Report generation
- Human-in-the-loop workflow

## Future Improvements
- Multi-agent architecture
- Security log ingestion
- MITRE ATT&CK mapping
- IOC enrichment tools
- RAG security knowledge base
- Agent memory
- Human approval checkpoints
- Structured JSON incident reports

## Security Notice
For **authorized defensive and educational use only**. Do not use this project to access, scan, exploit, monitor, or collect information from systems without permission.
