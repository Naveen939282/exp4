from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
options=Options()
options.add_argument("--start-maximized")
service=Service("msedgedriver.exe")
driver=webdriver.Edge(service=service,options=options)
driver.get("https://facebook.com")
wait=WebDriverWait(driver,20)
email=wait.until(ec.visibility_of_element_located((By.NAME,"email")))
password=wait.until(ec.visibility_of_element_located((By.NAME,"pass")))
email.send_keys("naveen@gmail.com")
password.send_keys("Naveen@123456")
password.send_keys(Keys.RETURN)
print("success")
time.sleep(15)
driver.quit()
