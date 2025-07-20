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
shopify-insight-scraper/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app
│   ├── scraper.py            # Scraping logic
│   ├── constants.py          # Headers, path constants
│   ├── models.py             # Pydantic schemas
│   ├── utils.py              # Helper functions
│   └── templates/
│       └── index.html        # Frontend UI
├── static/
│   └── script.js             # JavaScript for frontend
├── run.py                    # Entry point for Render
├── requirements.txt
├── README.md
└── .render.yaml              # Render deployment config
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/shopify-insight-scraper.git
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
* Ensure `run.py` is set as entry point

### Render Setup:

1. Go to [Render.com](https://render.com)
2. Create a new **Web Service**
3. Use the following settings:

   * **Runtime:** Python 3.x
   * **Start Command:** `python run.py`
   * **Build Command:** `pip install -r requirements.txt`
   * **Root Directory:** Leave blank or set to `.`

Render will automatically expose your service at a public URL.

---

## ❓ How to Use

1. Visit the hosted frontend UI
2. Enter a full Shopify website URL (e.g. `https://luxyskincare.in`)
3. Click **Fetch Insights**
4. Wait for 3-5 seconds for the results to appear

---

## ⚠️ Notes

* This app only works with **public Shopify stores**
* Some stores block scrapers or rate-limit aggressively
* You can try upgrading to use [Playwright](https://playwright.dev/python/) for JavaScript-heavy stores

---

## 🚧 Disclaimer

This project is for educational and personal use. Do not use it for scraping private or restricted content. Always check the target website’s `robots.txt` and terms of service.

---

## 🎉 Credits

Built with ❤️ by \[Your Name] for the GenAI Developer Internship Assignment.
