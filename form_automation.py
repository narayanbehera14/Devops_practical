from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # ✅ fixed import
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.maximize_window()

time.sleep(2)

driver.execute_script("window.scrollTo(0,800)")
time.sleep(1)

fname = driver.find_element(By.ID, "fname")
lname = driver.find_element(By.ID, "lname")  # ✅ fixed incorrect 'lname.clear.find_element'

fname.clear()
lname.clear()

fname.send_keys("Narayan")
lname.send_keys("Behera")

submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_btn.click()

print("Form filled and submitted successfully!")

time.sleep(4)
print("Program success!")
driver.quit()
