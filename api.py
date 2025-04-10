from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import AssessmentRecommender, extract_duration_from_query
import uvicorn

app = FastAPI()

# Allow CORS for demo purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

recommender = AssessmentRecommender()

class QueryRequest(BaseModel):
    text: str

@app.post("/recommend")
async def recommend_assessments(request: QueryRequest):
    """
    API endpoint for getting assessment recommendations
    """
    query = request.text
    max_duration = extract_duration_from_query(query)
    
    recommendations = recommender.recommend(query, max_duration=max_duration)
    
    # Format response
    formatted_recs = []
    for rec in recommendations:
        formatted_recs.append({
            "name": rec["name"],
            "url": rec["url"],
            "remote_testing": rec["remote_testing"],
            "adaptive": rec["adaptive"],
            "duration": rec["duration"],
            "test_type": rec["test_type"],
            "score": rec.get("score", 0)  # For ranking purposes
        })
    
    return {"recommendations": formatted_recs}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)