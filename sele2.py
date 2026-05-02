from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
service = Service("msedgedriver.exe")
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.google.com")
wait = WebDriverWait(driver, 20)
search_box = wait.until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
print("Search box is displayed:", search_box.is_displayed())
print("Search box is enabled:", search_box.is_enabled())
links = driver.find_elements(By.TAG_NAME, "a")
print("Total links on page:", len(links))
print("\nList of Links:")
for link in links:
    print(link.text)
inputs = driver.find_elements(By.TAG_NAME, "input")
print("\nTotal input fields:", len(inputs))
buttons = driver.find_elements(By.TAG_NAME, "button")
print("Total buttons:", len(buttons))
time.sleep(10)
driver.quit()
