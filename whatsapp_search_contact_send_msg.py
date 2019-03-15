from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer

friends_lists = ['Pb12', 'Rahul Ayan']

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)





#group_title = wait.until(EC.visibility_of_element_located(By.XPATH, "//span[@data-icon='search']"))
#group_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@class='_2MSJr']")))


#group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))
#search = driver.find_elements_by_xpath('//*[@id="side"]/div[2]/div/label/input')[0]
#search = driver.find_element_by_xpath("//input[@title='Search or start new chat']")
time.sleep(10)
search = driver.find_elements_by_xpath("//input[@title='Search or start new chat']")[0]
search.click()

for friend in friends_lists:
    search.clear()
    search.send_keys(friend)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._3Burg")))
    time.sleep(3)
    persons = driver.find_elements_by_class_name('_2wP_Y')
    print(len(persons))
    for person in persons:
        try:
            if person.text not in ['CHATS','MESSAGES']:
                person_title = person.find_element_by_class_name('_1wjpf')
                print(person_title.get_attribute("title"))
                person_contact = person.find_element_by_class_name('_2EXPL')
                person_contact.click()
                time.sleep(2)
                #message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                message = driver.find_elements_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']")[0]
                time.sleep(2)

                message.send_keys("Check!")
                time.sleep(2)

                #sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                sendbutton = driver.find_elements_by_xpath("//span[@data-icon='send']")[0]
                sendbutton.click()
        except:
            print("*")
            continue

driver.close()