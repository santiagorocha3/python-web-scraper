import requests


def check_website(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"[UP] {url}")
        else:
            print(f"[ISSUE] {url} returned status {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"[DOWN] {url}")


if __name__ == "__main__":
    websites = [
        "https://google.com",
        "https://github.com",
        "https://news.ycombinator.com",
        "https://example.com"
    ]

    for site in websites:
        check_website(site)