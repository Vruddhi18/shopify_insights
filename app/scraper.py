import httpx
from bs4 import BeautifulSoup
from .models import BrandData, FAQ, ContactInfo, SocialLinks, ImportantLinks
from .constants import HEADERS
from .utils import extract_emails, extract_phones, extract_faqs, find_social_links, find_important_links

async def fetch_html(client, url: str):
    try:
        res = await client.get(url, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            return res.text
    except Exception:
        return None

async def scrape_shopify_data(website_url: str) -> BrandData:
    async with httpx.AsyncClient() as client:
        home_html = await fetch_html(client, website_url)
        if not home_html:
            raise ValueError("Website not found or not reachable")

        soup = BeautifulSoup(home_html, 'html.parser')

        # Product Catalog
        product_catalog = []
        try:
            products_url = website_url.rstrip('/') + "/products.json"
            res = await client.get(products_url)
            if res.status_code == 200:
                product_catalog = res.json().get('products', [])
        except:
            pass

        # Hero Products
        hero_products = [h.get_text(strip=True) for h in soup.select('h2, h3')][:5]

        # Policies
        privacy_policy = refund_policy = None
        try:
            privacy_policy_html = await fetch_html(client, website_url + "/policies/privacy-policy")
            if privacy_policy_html:
                privacy_policy = BeautifulSoup(privacy_policy_html, 'html.parser').get_text()
        except:
            pass
        try:
            refund_policy_html = await fetch_html(client, website_url + "/policies/refund-policy")
            if refund_policy_html:
                refund_policy = BeautifulSoup(refund_policy_html, 'html.parser').get_text()
        except:
            pass

        # FAQs
        faqs = extract_faqs(soup)
        faqs_model = [FAQ(**faq) for faq in faqs]

        # Contact Info
        contact_info = ContactInfo(
            emails=extract_emails(home_html),
            phones=extract_phones(home_html)
        )

        # Social Links
        socials = find_social_links(soup)
        social_links = SocialLinks(**socials)

        # About Text
        about = None
        try:
            about_html = await fetch_html(client, website_url + "/pages/about-us")
            if about_html:
                about = BeautifulSoup(about_html, 'html.parser').get_text()
        except:
            pass

        # Important Links
        important_links = ImportantLinks(**find_important_links(soup))

        return BrandData(
            product_catalog=product_catalog,
            hero_products=hero_products,
            privacy_policy=privacy_policy,
            refund_policy=refund_policy,
            faqs=faqs_model,
            contact_info=contact_info,
            social_links=social_links,
            about=about,
            important_links=important_links
        )