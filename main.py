from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

options = Options()
options.binary_location = chrome_path

print("Starting Chrome browser...")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print("Opened:", driver.title)

time.sleep(5)
print("Program success!")
driver.quit()
