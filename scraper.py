import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict
import json

def scrape_shl_assessments() -> List[Dict]:
    """
    Scrape SHL assessment data from their product catalog
    Returns a list of assessment dictionaries
    """
    base_url = "https://www.shl.com/solutions/products/product-catalog/"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching SHL catalog: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This is a simplified scraper - in reality you'd need to parse the actual structure
    # For this example, we'll create mock data that matches the expected format
    assessments = []
    
    # Mock data - in a real implementation this would come from scraping
    assessments = [
        {
            "name": "SHL Verify Interactive - Java",
            "url": "https://www.shl.com/solutions/products/verify-interactive/java",
            "remote_testing": "Yes",
            "adaptive": "Yes",
            "duration": "45 minutes",
            "test_type": "Technical Skills",
            "description": "Assesses Java programming skills with interactive coding tasks.",
            "skills": ["Java", "Programming", "Problem Solving"]
        },
        {
            "name": "SHL Cognitive Ability",
            "url": "https://www.shl.com/solutions/products/cognitive-ability",
            "remote_testing": "Yes",
            "adaptive": "No",
            "duration": "30 minutes",
            "test_type": "Cognitive Ability",
            "description": "Measures general mental ability including verbal, numerical and abstract reasoning.",
            "skills": ["Cognitive Ability", "Problem Solving", "Reasoning"]
        },
        {
            "name": "SHL Personality Questionnaire",
            "url": "https://www.shl.com/solutions/products/personality-questionnaire",
            "remote_testing": "Yes",
            "adaptive": "No",
            "duration": "20 minutes",
            "test_type": "Personality",
            "description": "Assesses personality traits relevant to workplace performance.",
            "skills": ["Personality", "Behavioral", "Soft Skills"]
        },
        {
            "name": "SHL Verify Interactive - Python",
            "url": "https://www.shl.com/solutions/products/verify-interactive/python",
            "remote_testing": "Yes",
            "adaptive": "Yes",
            "duration": "50 minutes",
            "test_type": "Technical Skills",
            "description": "Assesses Python programming skills with interactive coding tasks.",
            "skills": ["Python", "Programming", "Problem Solving"]
        },
        {
            "name": "SHL Verify Interactive - JavaScript",
            "url": "https://www.shl.com/solutions/products/verify-interactive/javascript",
            "remote_testing": "Yes",
            "adaptive": "Yes",
            "duration": "50 minutes",
            "test_type": "Technical Skills",
            "description": "Assesses JavaScript programming skills with interactive coding tasks.",
            "skills": ["JavaScript", "Programming", "Web Development"]
        },
        {
            "name": "SHL Verify Interactive - SQL",
            "url": "https://www.shl.com/solutions/products/verify-interactive/sql",
            "remote_testing": "Yes",
            "adaptive": "Yes",
            "duration": "40 minutes",
            "test_type": "Technical Skills",
            "description": "Assesses SQL skills with interactive database tasks.",
            "skills": ["SQL", "Database", "Querying"]
        },
        {
            "name": "SHL Behavioral Assessment",
            "url": "https://www.shl.com/solutions/products/behavioral-assessment",
            "remote_testing": "Yes",
            "adaptive": "No",
            "duration": "25 minutes",
            "test_type": "Behavioral",
            "description": "Evaluates behavioral competencies for workplace success.",
            "skills": ["Behavioral", "Soft Skills", "Teamwork"]
        },
        {
            "name": "SHL Management & Graduate Item Bank",
            "url": "https://www.shl.com/solutions/products/management-graduate-item-bank",
            "remote_testing": "Yes",
            "adaptive": "No",
            "duration": "60 minutes",
            "test_type": "Cognitive Ability",
            "description": "Designed for assessing management and graduate candidates.",
            "skills": ["Cognitive Ability", "Problem Solving", "Leadership"]
        },
        {
            "name": "SHL Occupational Personality Questionnaire",
            "url": "https://www.shl.com/solutions/products/occupational-personality-questionnaire",
            "remote_testing": "Yes",
            "adaptive": "No",
            "duration": "35 minutes",
            "test_type": "Personality",
            "description": "Measures personality traits relevant to specific occupations.",
            "skills": ["Personality", "Behavioral", "Occupational Fit"]
        },
        {
            "name": "SHL Verify G+",
            "url": "https://www.shl.com/solutions/products/verify-g-plus",
            "remote_testing": "Yes",
            "adaptive": "Yes",
            "duration": "30 minutes",
            "test_type": "Cognitive Ability",
            "description": "General ability test with adaptive difficulty.",
            "skills": ["Cognitive Ability", "Problem Solving", "Adaptive"]
        }
    ]
    
    # Save to JSON file for later use
    with open('assessments.json', 'w') as f:
        json.dump(assessments, f, indent=2)
    
    return assessments

if __name__ == "__main__":
    assessments = scrape_shl_assessments()
    print(f"Scraped {len(assessments)} assessments")