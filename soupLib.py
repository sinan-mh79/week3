import requests
import json
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_programming_languages"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.6613.86 Safari/537.36"
    )
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


example = soup.find("div", class_="mw-page-container")


if example:
    data = {
        "url": url,
        "content": example.get_text(strip=True)  
    }

    # Convert to JSON string
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_data[:1000])  
else:
    print(" Could not find the content div on the page.")


