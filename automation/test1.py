from selenium import webdriver
import time
import logging

driver = webdriver.Chrome()
driver.get('https://www.cathaybk.com.tw/cathaybk')

page_state = driver.execute_script('return document.readyState;')
while page_state != 'complete':
    time.sleep(3)
    page_state = driver.execute_script('return document.readyState;')

driver.save_screenshot('ss1.png')
driver.quit()