import re

from Sample.Driver import get_driver


def artykul_na_medal():
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
