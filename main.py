from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def home():
    return "🧠 ALevelAPI Scraper Running"

@app.route("/scrape")
def scrape():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"})

    url = f"https://www.alevelapi.com/?s={query}"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="domcontentloaded")

            results = page.evaluate("""() => {
                const items = [];
                document.querySelectorAll("ul.post-items li.post-item").forEach(el => {
                    const title = el.querySelector("h2.entry-title a")?.innerText;
                    const link = el.querySelector("h2.entry-title a")?.href;
                    const thumbnail = el.querySelector(".post-thumbnail img")?.src || null;
                    if (title && link) {
                        items.push({ title, link, thumbnail });
                    }
                });
                return items;
            }""")

            browser.close()
    except Exception as e:
        return jsonify({"error": "Scrape failed", "details": str(e)}), 500

    return jsonify({
        "query": query,
        "results": results
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

