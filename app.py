from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

url = "https://www.google.com/"
number_prizedraw = 1715

driver.get(url)
driver.maximize_window()
time.sleep(5)

elem_search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
phrase_search = "Mega-Sena/Concurso " + str(number_prizedraw)
elem_search.send_keys(phrase_search)
elem_search.submit()
time.sleep(10)

elem_number_1 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[1]")
print(elem_number_1.text)
time.sleep(1)

elem_number_2 = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/span[2]")
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

phrase_search = "Mega-Sena/Concurso "
number_prizedraw = number_prizedraw + 1
driver.back()
time.sleep(5)
