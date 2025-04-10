import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

class AssessmentRecommender:
    def __init__(self):
        # Load assessment data
        with open('assessments.json', 'r') as f:
            self.assessments = json.load(f)
        
        # Initialize sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Generate embeddings for all assessments
        self.assessment_texts = [
            f"{a['name']} {a['description']} {' '.join(a['skills'])} {a['test_type']}"
            for a in self.assessments
        ]
        self.embeddings = self.model.encode(self.assessment_texts)
    
    def filter_by_duration(self, assessments: List[Dict], max_duration: int = None) -> List[Dict]:
        """
        Filter assessments by duration if specified
        """
        if not max_duration:
            return assessments
            
        filtered = []
        for a in assessments:
            # Extract numeric duration (assuming format like "45 minutes")
            duration_str = a['duration'].split()[0]
            try:
                duration = int(duration_str)
                if duration <= max_duration:
                    filtered.append(a)
            except ValueError:
                continue
        return filtered
    
    def recommend(self, query: str, max_results: int = 10, max_duration: int = None) -> List[Dict]:
        """
        Recommend assessments based on query
        """
        # Embed the query
        query_embedding = self.model.encode(query)
        
        # Calculate similarity scores
        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]
        
        # Get indices of top matches
        top_indices = np.argsort(similarities)[::-1][:max_results]
        
        # Get corresponding assessments
        recommendations = [self.assessments[i] for i in top_indices]
        
        # Filter by duration if specified
        if max_duration:
            recommendations = self.filter_by_duration(recommendations, max_duration)
        
        return recommendations[:max_results]

def extract_duration_from_query(query: str) -> int:
    """
    Try to extract duration limit from query text
    Returns duration in minutes or None if not specified
    """
    import re
    # Look for patterns like "30 minutes" or "less than 45 mins"
    matches = re.findall(r'(\d+)\s*min\w*', query.lower())
    if matches:
        return int(matches[-1])
    
    return None