import streamlit as st
from utils import AssessmentRecommender, extract_duration_from_query
import pandas as pd
import requests

# Initialize recommender
recommender = AssessmentRecommender()

# Streamlit app
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

st.title("SHL Assessment Recommendation System")
st.markdown("""
Enter a job description or query to get recommended SHL assessments.
""")

# Input form
with st.form("recommendation_form"):
    query = st.text_area("Enter job description or query:", 
                        placeholder="e.g., 'I need an assessment for Java developers with 45 minute duration limit'")
    
    submitted = st.form_submit_button("Get Recommendations")
    
    if submitted and query:
        with st.spinner("Finding the best assessments..."):
            # Extract duration if specified
            max_duration = extract_duration_from_query(query)
            
            # Get recommendations
            recommendations = recommender.recommend(query, max_duration=max_duration)
            
            if recommendations:
                # Display results in a table
                st.subheader("Recommended Assessments")
                
                # Prepare data for display
                display_data = []
                for rec in recommendations:
                    display_data.append({
                        "Assessment Name": f"[{rec['name']}]({rec['url']})",
                        "Remote Testing": rec['remote_testing'],
                        "Adaptive/IRT": rec['adaptive'],
                        "Duration": rec['duration'],
                        "Test Type": rec['test_type']
                    })
                
                # Convert to DataFrame and display as markdown to preserve links
                df = pd.DataFrame(display_data)
                st.markdown(df.to_markdown(index=False))
            else:
                st.warning("No assessments found matching your criteria. Try broadening your search.")
    elif submitted:
        st.warning("Please enter a query first")

st.markdown("""
### Example Queries:
- I am hiring for Java developers who can also collaborate effectively with my business teams. Looking for an assessment(s) that can be completed in 40 minutes.
- Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript. Need an assessment package that can test all skills with max duration of 60 minutes.
- I need cognitive and personality tests for analyst candidates with 45 minute limit.
""")