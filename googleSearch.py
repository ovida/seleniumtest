from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("amazon canada")
search_box.send_keys(Keys.RETURN)

try:
     first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h3")))

     print("first result found: ", first_result.text)
except Exception as e:
     print("Error: ", e)     

#assert "IBM Careers" in driver.title, "Test Failed: PAge not found"

driver.quit()