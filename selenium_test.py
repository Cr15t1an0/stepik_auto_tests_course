import os 
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id= 'price']"), '100'))


driver.find_element(By.XPATH,"//button[@id='book']").click()
# Resolve captcha

x = driver. find_element(By.XPATH, "//span[@id='input_value']").text

driver.find_element(By.XPATH, "//input[@type='text']").send_keys(calc(x))

driver.find_element(By.XPATH, "//button[@type='submit']").click()