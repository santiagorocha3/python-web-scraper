import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    # Simple extraction example (titles)
    items = soup.find_all(["h2", "h3", "h4"])

    for item in items:
        title = item.get_text(strip=True)

        if title:
            data.append({
                "title": title,
                "price": "N/A",
                "url": url
            })

    return data


def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False)
    print(f"Saved {len(data)} rows to output.csv")


if __name__ == "__main__":
    url = input("Enter a website URL: ")
    result = scrape(url)
    save_to_csv(result)
    