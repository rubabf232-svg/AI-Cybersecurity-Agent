import os
from datetime import datetime
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.set_page_config(page_title='AI Cybersecurity Agent', page_icon='🛡️', layout='wide')

def rule_based_analyzer(query):
    q = query.lower(); findings = []
    checks = [
        (['phishing','suspicious email','fake login'], 'Phishing Risk', 'High', 'Check sender/domain mismatch, urgent requests, suspicious links, and credential requests.'),
        (['password','credential','login'], 'Authentication Risk', 'Medium', 'Use strong unique passwords, MFA, rate limiting, and secure password storage.'),
        (['api key','secret','token','password in code'], 'Secret Exposure', 'High', 'Do not hard-code secrets. Use environment variables and secret management.'),
        (['sql injection','sqli','database query'], 'Injection Risk', 'High', 'Use parameterized queries, input validation, and least-privilege database accounts.'),
        (['xss','cross-site scripting'], 'Web Injection Risk', 'High', 'Apply output encoding, input validation, and an appropriate Content Security Policy.'),
        (['port scan','open port','network'], 'Network Exposure', 'Medium', 'Review exposed services, firewall rules, segmentation, and unnecessary ports.'),
    ]
    for words,name,severity,detail in checks:
        if any(w in q for w in words): findings.append((name,severity,detail))
    if not findings: findings.append(('General Security Review','Info','Collect logs, identify assets, validate the reported behavior, and prioritize risks by impact and likelihood.'))
    return findings

def ai_analyze(query, api_key):
    if not api_key: return None
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        prompt = f'''You are a defensive cybersecurity analysis agent. Analyze this authorized security question:\n{query}\n\nReturn: 1. Situation summary 2. Key risks 3. Evidence to collect 4. Safe defensive actions 5. Priority. Do not provide instructions for unauthorized access, exploitation, credential theft, persistence, or evasion.'''
        r = client.responses.create(model=os.getenv('OPENAI_MODEL','gpt-4.1-mini'), input=prompt)
        return r.output_text
    except Exception as e:
        return f'AI provider error: {e}'

st.title('🛡️ AI Cybersecurity Agent')
st.caption('Agentic workflow demo: Plan → Analyze → Recommend → Report')
with st.sidebar:
    st.header('Agent Controls')
    use_ai = st.toggle('Use AI provider', value=False)
    api_key = st.text_input('OPENAI_API_KEY', type='password', value=os.getenv('OPENAI_API_KEY',''))
    st.info('Use only on systems, logs, domains, or data you are authorized to analyze.')
query = st.text_area('Security task', placeholder='Example: Our company received a suspicious login email. What should the security team investigate?', height=150)
if st.button('Run Security Agent', type='primary') and query.strip():
    st.subheader('1. Agent Plan')
    for item in ['Understand the security question','Identify relevant risk areas','Analyze available indicators','Produce defensive recommendations','Generate a concise security report']:
        st.write('• ' + item)
    st.subheader('2. Analysis')
    findings = rule_based_analyzer(query)
    for name,severity,detail in findings:
        st.markdown(f'**{name} — {severity}**'); st.write(detail)
    if use_ai:
        st.subheader('3. AI Analyst'); st.write(ai_analyze(query, api_key) or 'Add an API key to enable the AI provider.')
    st.subheader('4. Agent Report')
    report = f'AI Cybersecurity Agent Report\nGenerated: {datetime.now():%Y-%m-%d %H:%M}\nTask: {query}\n\nFindings:\n'
    report += '\n'.join(f'- {n} [{s}]: {d}' for n,s,d in findings)
    report += '\n\nScope: Defensive/authorized security analysis only.'
    st.download_button('Download Report', report, file_name='security_agent_report.txt')
