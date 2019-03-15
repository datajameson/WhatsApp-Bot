from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)

#group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))
group_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_1vDUw _1NrpZ']")))
time.sleep(5)
persons = driver.find_elements_by_class_name('_2wP_Y')
for person in persons:
    #title = person.find_element_by_class_name('_1wjpf').text
    title = person.find_element_by_xpath('div/div/div[2]/div[1]/div[1]/span').text
    #time.sleep(2)
    print(title)
