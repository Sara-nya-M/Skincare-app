import uvicorn
import sys
import os

if __name__ == "__main__":
    print("Starting Skincare Web App backend...")
    # Run the FastAPI app from backend.main
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
