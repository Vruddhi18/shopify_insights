from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Shopify Brand Insights API")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Shopify Insights API! Use /fetch_insights"}