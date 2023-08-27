from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import logging

driver = webdriver.Chrome()
driver.set_window_size(640, 800)
driver.get('https://www.cathaybk.com.tw/cathaybk')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[1]/header/div/div[1]/a"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'產品介紹')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'信用卡')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'卡片介紹')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'停發卡')]"))).click()

cards = driver.find_elements(By.XPATH, "//section[contains(@data-anchor-block, 'blockname06')]//div[contains(@class, 'credit')]")
print(len(cards))

actions = ActionChains(driver)
i = 1
for card in cards:
    actions.move_to_element(card).perform()
    driver.save_screenshot('ss3' + str(i) + '.png')
    i += 1

driver.quit()
