import requests
from bs4 import BeautifulSoup
def currency(in_c, out_c):
    url = f"https://www.walutomat.pl/kursy-walut/{in_c}-{out_c}/"
    cont = requests.get(url).text
    soup = BeautifulSoup(cont, 'html.parser')
    el = soup.find('span', 'rate')
    print(el.text)


if __name__ == '__main__':
    currency('usd', 'pln')
