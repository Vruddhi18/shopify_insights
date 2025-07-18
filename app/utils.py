import re
from typing import List
from bs4 import BeautifulSoup

def extract_emails(text: str) -> List[str]:
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)

def extract_phones(text: str) -> List[str]:
    return re.findall(r"\+?\d[\d\-\s]{7,}\d", text)

def extract_faqs(soup: BeautifulSoup) -> List[dict]:
    faqs = []
    for q in soup.find_all(['h2', 'h3', 'h4']):
        next_sib = q.find_next_sibling()
        if next_sib and next_sib.name == 'p':
            faqs.append({"question": q.get_text(strip=True), "answer": next_sib.get_text(strip=True)})
    return faqs

def find_social_links(soup: BeautifulSoup) -> dict:
    links = {
        'instagram': None,
        'facebook': None,
        'twitter': None,
        'youtube': None,
        'linkedin': None
    }
    for a in soup.find_all('a', href=True):
        href = a['href']
        for key in links:
            if key in href:
                links[key] = href
    return links

def find_important_links(soup: BeautifulSoup) -> dict:
    result = {
        'contact_us': None,
        'order_tracking': None,
        'blogs': None
    }
    for a in soup.find_all('a', href=True):
        href = a['href'].lower()
        if 'contact' in href and not result['contact_us']:
            result['contact_us'] = href
        elif 'track' in href and not result['order_tracking']:
            result['order_tracking'] = href
        elif 'blog' in href and not result['blogs']:
            result['blogs'] = href
    return result