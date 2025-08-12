# Shopify Store Insights Scraper

This project is a full-stack web application built with **FastAPI** (backend) and **HTML/JavaScript** (frontend) to extract public insights from any Shopify-powered e-commerce website. It does **not** use the official Shopify API and relies on scraping publicly available data instead.

## 📈 Features

* Extracts:

  * Product catalog (from `/products.json`)
  * Hero section text (prominent headings)
  * Privacy & refund policies
  * About page content
  * Contact emails and phone numbers
  * Social media links
  * Blog & support-related links
  * FAQs (if structured)

* Simple HTML frontend UI

* Ready to deploy on **Render**

---

## 📁 Project Structure

```
shopify_insights/
├── app/
│ ├── constants.py 
│ ├── main.py 
│ ├── models.py 
│ ├── routes.py 
│ ├── scraper.py 
│ └── utils.py 
├── index.html 
├── run.py 
├── requirements.txt 
├── .gitignore 
└── README.md 
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Vruddhi18/shopify-insight-scraper.git
cd shopify-insight-scraper
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python run.py
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🚀 Deploy to Render

### Files to Upload to Render:

* All project files above
* Ensure `run.py` is set as an entry point



