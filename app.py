from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/scrape")
def scrape():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Missing query"})

    search_url = f"https://www.alevelapi.com/?s={query}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(search_url)

        results = page.evaluate("""() => {
            const items = [];
            document.querySelectorAll("ul.post-items li.post-item").forEach(el => {
                const title = el.querySelector("h2.entry-title a")?.innerText;
                const link = el.querySelector("h2.entry-title a")?.href;
                const thumbnail = el.querySelector(".post-thumbnail img")?.src;
                if (title && link) items.push({ title, link, thumbnail });
            });
            return items;
        }""")

        browser.close()

    return jsonify({
        "query": query,
        "results": results
    })

@app.route("/")
def home():
    return "🧠 ALevel API Scraper is running."
