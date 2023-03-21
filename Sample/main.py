import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/michal/Documents/_automated_python/chromedriver')


def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver


def main():
    driver = get_driver('https://pl.wikipedia.org/wiki/')
    element = driver.find_element(by='xpath', value='//*[@id="main-page-featured-article"]/p/b/a')
    header = driver.find_element(by='xpath', value='//*[@id="Artykuł_na_medal"]')
    paragraph = driver.find_element(by='xpath',
                                    value='/html/body/div[3]/div[3]/div[5]/div[1]/div/div[2]/div/div[2]/div[1]/p/b/a')
    site = paragraph.get_property('href')
    newsite = get_driver(site)
    paragraph = newsite.find_element(by='xpath', value='//*[@id="mw-content-text"]/div[1]/p[2]')
    text = str(paragraph.text)
    text = re.sub(r"\[[0-9]+]", '', text)
    print(f'{header.text}:  {element.text}\n {text}')


main()
