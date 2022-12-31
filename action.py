from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time

from varibles import driver, url, number_prizedraw

def open_url():
    try:
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5)
    except TimeoutException:
        print("Loading took too much time!")

def get_numbers():
    path_numbers = "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span["
    i=1
    while i<=6:
        path_numbers_prizedraw = path_numbers+str(i)+"]"
        number_prizedraw = driver.find_element(By.XPATH,str(path_numbers_prizedraw))
        print(number_prizedraw.text)
        time.sleep(1)
        i = i + 1
        path_numbers_prizedraw = ""
    print("Catch numbers")

def search_google():
    elem_search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    phrase_search = "Mega-Sena/Concurso " + str(number_prizedraw)
    elem_search.send_keys(phrase_search)
    elem_search.submit()
    time.sleep(10)

def back_page():
    driver.back()
    time.sleep(5)

