import time
from datetime import datetime

from Driver import get_driver

def weather():
    driv = get_driver("https://www.accuweather.com/en/pl/gda%C5%84sk/275174/minute-weather-forecast/275174")
    time.sleep(2)
    driv.find_element(by='xpath', value='/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[2]').click()
    while True:
        with open(f"{datetime.now().strftime('%Y-%d-%m-%H-%M-%S')}.txt", "w+") as f:
            f.write(driv.find_element(by='xpath', value='/html/body/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]').text)
        time.sleep(5)