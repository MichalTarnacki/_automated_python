from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

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


@app.route('/')
def home():
    return '<h1> Home page </h1> <p>Go to [ip]/api/<platform>-<number></p>'


@app.route('/api/<platform>-<number>')
def api(platform, number):
    driv = get_driver(
        f'https://www.metacritic.com/browse/games/score/metascore/year/{platform}/filtered?view=condensed')
    elements = driv.find_elements(By.CLASS_NAME, value="expand_collapse")
    list = []
    printed = 0
    for el in elements:
        if printed == int(number):
            break
        if el.tag_name != 'tr':
            continue
        printed += 1
        temp = el.find_element(By.CLASS_NAME, value='details')
        title = temp.find_element(By.CLASS_NAME, value='title').find_element(By.TAG_NAME, value='h3').text
        platform = temp.find_element(By.CLASS_NAME, value='platform').find_element(By.CLASS_NAME, value='data').text
        date = temp.find_elements(By.TAG_NAME, value='span')
        dict = {'title': title,
                'platform': platform,
                'release-date': date[3].text
                }
        list.append(dict)
    return jsonify(list)


app.run()
