from fastapi import APIRouter, HTTPException
from .models import WebsiteRequest, BrandResponse
from .scraper import scrape_shopify_data

router = APIRouter()

@router.post("/fetch_insights", response_model=BrandResponse)
async def fetch_insights(payload: WebsiteRequest):
    try:
        brand_data = await scrape_shopify_data(payload.website_url)
        return BrandResponse(status="success", brand_data=brand_data)
    except ValueError as ve:
        raise HTTPException(status_code=401, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")