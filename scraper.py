import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("[ERROR] {}".format(e))
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    # Hacker News titles are stored inside: span class="titleline"
    items = soup.find_all("span", class_="titleline")

    for item in items:
        link = item.find("a")

        if link:
            title = link.get_text(strip=True)
            article_url = link.get("href")

            data.append({
                "title": title,
                "article_url": article_url,
                "source_url": url
            })

    return data


def save_to_csv(data, filename="output.csv"):
    if not data:
        print("[WARNING] No data to save.")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print("[SUCCESS] Saved {} rows to {}".format(len(data), filename))


if __name__ == "__main__":
    url = input("Enter a website URL: ").strip()

    if not url.startswith("http"):
        print("[ERROR] Enter a valid URL with http or https.")
    else:
        results = scrape(url)
        save_to_csv(results)