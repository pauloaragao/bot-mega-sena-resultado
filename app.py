from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time

def open_url():
    try:
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5)
    except TimeoutException:
        print("Loading took too much time!")

def search_google():
    elem_search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    phrase_search = "Mega-Sena/Concurso " + str(number_prizedraw)
    elem_search.send_keys(phrase_search)
    elem_search.submit()
    time.sleep(10)

def get_numbers():
    elem_number = []
    elem_number_1 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[1]")
    elem_number.append(elem_number_1)
    print (elem_number)
    print(elem_number_1.text)
    time.sleep(1)
    elem_number_2 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[2]")
    elem_number.append(elem_number_1)
    print (elem_number)
    print(elem_number_2.text)
    time.sleep(1)
    elem_number_3 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[3]")
    print(elem_number_3.text)
    time.sleep(1)
    elem_number_4 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[4]")
    print(elem_number_4.text)
    time.sleep(1)
    elem_number_5 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[5]")
    print(elem_number_5.text)
    time.sleep(1)
    elem_number_6 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[6]")
    print(elem_number_6.text)
    time.sleep(1)

def back_page():
    driver.back()
    time.sleep(5)

driver = webdriver.Chrome()
url = "https://www.google.com/"
number_prizedraw = 1715

open_url()
search_google()
#get_numbers()

phrase_search = "Mega-Sena/Concurso "
number_prizedraw = number_prizedraw + 1

back_page()
