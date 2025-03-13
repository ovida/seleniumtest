from selenium import webdriver

try:
    webdriver.Chrome()
    print("Selenium import successful!")
except Exception as e:
    print(f"Selenium import failed: {e}")
