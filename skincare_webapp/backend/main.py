from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import math
import os

app = FastAPI(title="Skincare Recommendation API")

# Allow CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model at startup
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'skincare_recommendation_model.pkl')
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
    
    vectorizer = model.get('tfidf_vectorizer')
    matrix = model.get('tfidf_matrix')
    df_clean = model.get('df_clean')
    skin_type_dict = model.get('skin_type_ingredients', {})
    skin_concern_dict = model.get('skin_concern_ingredients', {})
    
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class RecommendationRequest(BaseModel):
    skin_type: str
    skin_concern: str

@app.get("/api/options")
def get_options():
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    return {
        "skin_types": list(skin_type_dict.keys()),
        "skin_concerns": list(skin_concern_dict.keys())
    }

@app.post("/api/recommend")
def recommend_products(req: RecommendationRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
        
    skin_type_ingredients = skin_type_dict.get(req.skin_type, [])
    skin_concern_ingredients = skin_concern_dict.get(req.skin_concern, [])
    
    # Combine the ingredients into a single space-separated string
    features = " ".join(skin_type_ingredients) + " " + " ".join(skin_concern_ingredients)
    
    if not features.strip():
        raise HTTPException(status_code=400, detail="Invalid skin type or concern")
        
    try:
        # Vectorize
        q_vec = vectorizer.transform([features])
        # Compute cosine similarity
        sim = cosine_similarity(q_vec, matrix).flatten()
        # Get top 6 matches
        top_indices = sim.argsort()[-6:][::-1]
        
        results = []
        for idx in top_indices:
            row = df_clean.iloc[idx]
            
            # Handle NaN values before sending to JSON
            price = row.get('price')
            if isinstance(price, float) and math.isnan(price):
                price = "N/A"
                
            results.append({
                "product_name": row.get('product_name', 'Unknown'),
                "product_type": row.get('product_type', 'Unknown'),
                "price": price,
                "product_url": row.get('product_url', '#'),
                "ingredients": row.get('ingredients_list', [])
            })
            
        return {"recommendations": results}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
