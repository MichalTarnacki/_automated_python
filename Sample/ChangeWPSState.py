import time

from selenium.webdriver import Keys

from Sample.Driver import get_driver


def change_wps_state(username, password):

    new_driv = get_driver("http://192.168.1.100/Main_Login.asp")
    new_driv.find_element(by='xpath', value='//*[@id="login_username"]').send_keys(username)
    new_driv.find_element(by='xpath', value='//*[@id="login_filed"]/div[5]/input').send_keys(password)
    new_driv.find_element(by='xpath', value='//*[@id="login_filed"]/div[5]/input').send_keys(Keys.RETURN)
    time.sleep(1)
    new_driv.find_element(by='xpath', value='//*[@id="Advanced_Wireless_Content_menu"]').click()
    time.sleep(1)
    new_driv.find_element(by='xpath',
                          value='/html/body/form[2]/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td[2]/div').click()
    time.sleep(1)
    new_driv.find_element(by='xpath',
                          value='/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/div[2]/div/img').click()
    time.sleep(1)
