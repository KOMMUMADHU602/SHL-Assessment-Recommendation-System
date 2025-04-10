
### 🧠 SHL Assessment Recommendation System

*A smart tool that helps hiring managers find the perfect SHL assessments for their job openings*

<img width="539" alt="result" src="https://github.com/user-attachments/assets/3af039be-38b7-4bd3-b5fb-c00cb0c2afb4" />

## 🌟 What Does This Do?

Tired of manually searching through SHL's assessment catalog? This system:

 Takes a **natural language query** (e.g., "Java developer test under 45 minutes")
 Or a **full job description**
 Recommends the **most relevant SHL assessments** with all key details
 Shows results in a clean, clickable format

## 🚀 Quick Start

### Prerequisites
 Python 3.8+
 pip package manager

### Installation
1. Clone this repository:

   git clone https://github.com/KOMMUMADHU602/shl-Assessment-recommendation-system
   cd shl-recommender


2. Set up the environment:
   
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   

### Running the System
1. **First, start the API** (in one terminal):
   
   python api.py
   
   *API will run at `http://localhost:8000`*

2. **Then launch the web app** (in another terminal):
   
   streamlit run app.py
   
   *App will open in your browser at `http://localhost:8501`*

## 🛠️ How It Works

### Behind the Scenes
1. **Data Collection**: Our scraper gathers SHL assessment details
2. **Smart Matching**: Uses AI embeddings to understand your query
3. **Precision Filtering**: Automatically detects time constraints
4. **Clean Presentation**: Shows only the most relevant assessments

### Try These Example Queries
 "I need a Java test under 40 minutes"
 "Cognitive and personality tests for analysts"
 "Python and SQL assessment package for mid-level hires"

## 📂 Project Structure

shl-recommender/
├── app.py                # Web interface (Streamlit)
├── api.py                # Recommendation API (FastAPI)
├── scraper.py            # SHL data collector
├── utils.py              # Core recommendation logic
├── assessments.json      # Assessment database
├── requirements.txt      # Dependencies
└── README.md             # This file



## 💡 Why This Matters
 Saves recruiters **hours of manual searching**
 Understands **real job requirements** (not just keywords)
 **Adapts to time constraints** automatically
 Presents results in a **hiring-manager-friendly format**

## 🛠️ Built With
 **Python** - Core programming language
 **Streamlit** - Simple web interface
 **FastAPI** - Robust backend API
 **Sentence Transformers** - AI-powered semantic search
 **BeautifulSoup** - Web scraping

## 🤝 How to Contribute
Found a bug or have an improvement? 
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📜 License
This project is licensed under the MIT License.

