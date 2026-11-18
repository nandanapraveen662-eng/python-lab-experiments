
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

URL = "https://www.theguardian.com/international"
CSV_FILE = "news_headlines.csv"

# Sample news data
sample_news = [
    {
        "Headline": "India Announces New Technology Initiative",
        "Publication Date": "2026-11-18",
        "Category": "Technology"
    },
    {
        "Headline": "Kerala Introduces New Education Programme",
        "Publication Date": "2026-11-18",
        "Category": "Education"
    },
    {
        "Headline": "India Wins International Cricket Match",
        "Publication Date": "2026-11-17",
        "Category": "Sports"
    },
    {
        "Headline": "Global Markets Show Positive Growth",
        "Publication Date": "2026-11-17",
        "Category": "Business"
    },
    {
        "Headline": "Scientists Discover New Space Technology",
        "Publication Date": "2026-11-16",
        "Category": "Science"
    }
]

def get_category(article, link):
    tag = article.select_one(
        'a[href*="/world/"], a[href*="/business/"], '
        'a[href*="/technology/"], a[href*="/sport/"]'
    )

    if tag and tag.get_text(strip=True):
        return tag.get_text(" ", strip=True)

    if link and link.get("href"):
        parts = [
            p for p in urlparse(link["href"]).path.split("/") if p
        ]
        if parts:
            return parts[0].replace("-", " ").title()

    return "Not available"


def scrape_news():
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(
        URL, headers=headers, timeout=20
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    rows = []
    seen = set()

    for article in soup.find_all("article"):
        heading = article.select_one("h3, h2")

        if not heading:
            continue

        headline = heading.get_text(" ", strip=True)

        if not headline or headline in seen:
            continue

        link = heading.find_parent("a")

        if link is None:
            link = article.find("a", href=True)

        time_tag = article.find("time")

        date = "Not available"

        if time_tag:
            date = (
                time_tag.get("datetime")
                or time_tag.get_text(" ", strip=True)
            )

        rows.append({
            "Headline": headline,
            "Publication Date": date,
            "Category": get_category(article, link)
        })

        seen.add(headline)

    return rows


def save_csv(rows):
    fields = [
        "Headline",
        "Publication Date",
        "Category"
    ]

    with open(
        CSV_FILE, "w", newline="", encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file, fieldnames=fields
        )

        writer.writeheader()
        writer.writerows(rows)


def main():

    try:
        print("Fetching news headlines...")

        rows = scrape_news()

        # Use sample data if no live headlines are found
        if not rows:
            print("Using sample news data...")
            rows = sample_news

        save_csv(rows)

        print("\nNews Headlines:\n")

        for i, item in enumerate(rows, 1):

            print(i, item["Headline"])
            print("Date:", item["Publication Date"])
            print("Category:", item["Category"])
            print()

        print("Data successfully saved to CSV file.")

    except requests.RequestException as error:
        print("Website request failed:", error)
        print("Saving sample news data instead.")

        save_csv(sample_news)

    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    main()
