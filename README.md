# SHL-Assessment-Recommendation-System
 smart AI-powered tool that helps recruiters instantly find the most relevant SHL assessments for any job role—saving hours of manual searching with natural language queries.
Here’s a polished, engaging description of your SHL Assessment Recommendation System project that clearly communicates its purpose, value, and technical approach:


### Project Description: SHL Assessment Recommendation System

TL;DR: 
A smart AI-powered tool that helps recruiters instantly find the most relevant SHL assessments for any job role—saving hours of manual searching with natural language queries.  

#### **🔍 The Problem**  
Hiring managers struggle to navigate SHL’s vast assessment catalog. Traditional keyword searches are time-consuming and often miss the mark, especially for complex roles requiring multiple skills or specific testing constraints (e.g., *"Find a 45-minute Java test with teamwork evaluation"*).  

#### **✨ The Solution**  
This system leverages **generative AI** and **semantic search** to:  
 **Understand job descriptions** or free-text queries (e.g., *"Python developer test under 30 minutes"*).  
 **Recommend tailored SHL assessments** with key details:  
   Test name & direct SHL catalog link  
   Remote testing support (Yes/No)  
   Duration and test type (Cognitive, Technical, etc.)  
 **Prioritize accuracy** with Recall@3 and MAP@3 metrics to ensure top recommendations are relevant.  

#### **🛠️ How It Works**  
1. **Data Pipeline**:  
    Scrapes SHL’s product catalog (or uses mock data for prototyping).  
    Structures assessments with embeddings for AI search.  

2. **AI Matching**:  
    Uses 'sentence-transformers' to convert queries/job descriptions into semantic vectors.  
    Ranks assessments by cosine similarity to the query.  

3. **Smart Filters**:  
    Auto-detects time constraints (e.g., *"under 40 minutes"*).  
    Supports hybrid searches (skills + behavioral traits).  

4. **User-Friendly Interface**:  
    **Streamlit web app** for simple input/output.  
    **FastAPI backend** for scalable recommendations (JSON-ready).  

#### **🚀 Key Features**  
 **Natural Language Understanding**: No rigid syntax—works with plain English.  
 **Time-Saving**: Cuts search time from hours to seconds.  
 **Transparent Results**: Clear comparison of test attributes.  
 **Extensible**: Easy to integrate with SHL’s live catalog or other HR tools.  

#### **🌐 Real-World Impact**  
 **Recruiters**: Quickly find tests matching exact role requirements.  
 **Candidates**: Better-matched assessments improve hiring fairness.  
 **SHL**: Enhances product discoverability and user experience.  

#### **🖥️ Tech Stack**  
 **Backend**: Python, FastAPI, Sentence-Transformers ('all-MiniLM-L6-v2')  
 **Frontend**: Streamlit (low-code UI)  
 **Data**: Web scraping (BeautifulSoup), embeddings, cosine similarity  
 **Metrics**: Recall@3, MAP@3 for evaluation  

#### **📌 Example Use Case**  
> *Query*: *"I need a cognitive and personality test for analysts, max 45 minutes"*  
> *Output*:  
> 1. **SHL Cognitive Ability Test** (30 mins, Remote: Yes)  
> 2. **SHL Personality Questionnaire** (20 mins, Remote: Yes)  
> 3. **SHL Verify G+** (Adaptive, 30 mins)  



### **Why This Stands Out**  
Unlike static filters, this system **understands intent** and **context**, making it ideal for complex hiring scenarios. It’s designed for SHL’s catalog but can adapt to other assessment providers.  

**Ideal for**: HR teams, recruitment platforms, or as a demo for AI-powered HR tech.  



This description balances **technical depth** with **business value**, making it suitable for:  
- GitHub READMEs  
- Project presentations  
- LinkedIn/portfolio summaries  

Let me know if you'd like to emphasize any specific aspect (e.g., scalability, LLM integration)!
