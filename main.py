import csv
import time

import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
current_page_url = "/page/1"

quote_list = []

while True:
    response = requests.get(base_url + current_page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        quote_block = soup.find_all("div", class_="quote")
        for quote in quote_block:
            result_text = (quote.find("span", class_="text")).text
            author = (quote.find("small", class_="author")).text
            tags = (quote.find_all("div", class_="tags"))

            result_tag = []
            for tag in tags:
                for t in tag.find_all("a", class_="tag"):
                    result_tag.append(t.text)
            quote_list.append({
                "text": result_text,
                "author": author,
                "tags": result_tag,
            })
        next_button = soup.find("li", class_="next")
        if next_button:
            current_page_url = next_button.find("a")["href"]
            time.sleep(1)
        else:
            break
    with open("quotes.csv", "a", newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file, ["text", "author", "tags"])
        writer.writerows(quote_list)

