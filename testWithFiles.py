from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("iii")
    browser.find_element(By.NAME, "lastname").send_keys("ooo")
    browser.find_element(By.NAME, "email").send_keys("ooo")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "запуск.txt"
    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
