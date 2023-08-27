from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

driver = webdriver.Chrome()
driver.set_window_size(480, 800)
driver.get('https://www.cathaybk.com.tw/cathaybk')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[1]/header/div/div[1]/a"))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'產品介紹')]"))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'信用卡')]"))).click()
driver.save_screenshot('ss2.png')

e = driver.find_element(By.XPATH, "//div[contains(text(),'信用卡') and contains(@class, 'mbOnly')]")
siblings = e.find_elements(By.XPATH, "following-sibling::* | preceding-sibling::*")

print(len(siblings))

driver.quit()