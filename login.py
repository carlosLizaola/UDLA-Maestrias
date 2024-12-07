import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get ("https://aplatamqa.com/portal-alumno/login?schoolId=24")

driver.maximize_window()

selectCurrentTypeAccount = driver.find_element(By.CSS_SELECTOR, 'select[formcontrolname="currentTypeAccount"]')
currentTypeAccount = Select(selectCurrentTypeAccount)
currentTypeAccount.select_by_visible_text("UDLA MAESTRÍAS")

username = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="username"]')
username.send_keys("prueba_20241001_016@prueba.com")

password = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]')))
password.send_keys("Test.123")

driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block"]').click()

time.sleep(5)
