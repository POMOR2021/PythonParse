import csv
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
print("Добро пожаловать в парсер цитат. Взгляните на операции")

while True:
    print("1. Увидеть запаршеные данные\n2. Сохранить запаршеные данные в ")
    a = int(input())

    match(a):
        case 1:
            soup = BeautifulSoup(response.text, "html.parser")
            quote_block = soup.find_all("div", class_="quote")
            for quote in quote_block:
                result_quote = quote.find("span", class_="text")
                result_author = quote.find("small", class_="author")
            if result_quote and result_author:
                print(result_quote.text.strip(),result_author.text.strip(), sep="\n")
        case 2:
            soup = BeautifulSoup(response.text, "html.parser")
            quote_block = soup.find_all("div", class_="quote")
            with open("users.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                for quote in quote_block:
                    result_quote = quote.find("span", class_="text")
                    result_author = quote.find("small", class_="author")
                    data = [result_quote.text.strip(), result_author.text.strip()]
                    writer.writerow(data)
        case _:
            print("Введена неправильная операция")
