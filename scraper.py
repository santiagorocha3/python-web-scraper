import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape(url, pages=3):
    headers = {"User-Agent": "Mozilla/5.0"}
    all_data = []
    current_url = url

    for page in range(pages):
        print("[INFO] Scraping {}".format(current_url))

        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("[ERROR] {}".format(e))
            break

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("span", class_="titleline")

        for item in items:
            link = item.find("a")

            if link:
                all_data.append({
                    "title": link.get_text(strip=True),
                    "article_url": link.get("href"),
                    "source_url": current_url
                })

        more_link = soup.find("a", class_="morelink")

        if more_link:
            next_href = more_link.get("href")
            current_url = "https://news.ycombinator.com/" + next_href
        else:
            break

    return all_data


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
        results = scrape(url, pages=3)
        save_to_csv(results)
