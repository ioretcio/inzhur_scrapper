import requests
from bs4 import BeautifulSoup
import json

class InzhurScraper:
    def __init__(self):
        self.data = {}
        self.urls = [
            "https://www.inzhur.reit/funds/Energy",
            "https://www.inzhur.reit/funds/ocean",
            "https://www.inzhur.reit/funds/Supermarket",
            "https://www.inzhur.reit/funds/Zhytniy",
            "https://www.inzhur.reit/funds/2001",
            "https://www.inzhur.reit/funds/1001",
            "https://www.inzhur.reit/funds/Bud"
        ]

    def scrape(self):
        for url in self.urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                summary_info_div = soup.find('div', class_='summary-info')
                if summary_info_div:
                    first_item_div = summary_info_div.find('div', class_='item')
                    if first_item_div:
                        value = first_item_div.find('span', class_='value')
                        if value:
                            value_text = value.get_text().replace('₴', '').replace(' ', '').replace(',', '')
                            self.data[url.split('/')[-1]] = float(value_text)
                    else:
                        print("Cant find 'summary_info'.")
                else:
                    print("Cant find 'summary_info_div'.")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while fetching the page: {e}")
        return json.dumps(self.data, indent=4)