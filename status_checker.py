import requests


def check_website(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("[UP] {}".format(url))
        else:
            print("[ISSUE] {} returned status {}".format(url, response.status_code))

    except requests.exceptions.RequestException:
        print("[DOWN] {}".format(url))


def load_websites(filename="websites.txt"):
    try:
        with open(filename, "r") as file:
            websites = file.readlines()

        return [site.strip() for site in websites if site.strip()]

    except FileNotFoundError:
        print("[ERROR] websites.txt file not found.")
        return []


if __name__ == "__main__":
    websites = load_websites()

    if not websites:
        print("[WARNING] No websites to check.")
    else:
        for site in websites:
            check_website(site)