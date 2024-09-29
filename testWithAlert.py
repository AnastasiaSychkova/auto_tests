from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    input_element = browser.find_element(By.ID, "input_value")
    input = input_element.text
    y = calc(input)

    browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
