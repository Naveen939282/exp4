from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
options=Options()
service=Service("msedgedriver.exe")
driver=webdriver.Edge(service=service,options=options)
driver.get("https://google.com")
driver.maximize_window()
time.sleep(2)
fine=driver.find_element(By.NAME,"q")
if fine:
    print("success")
else:
    print("fail")
time.sleep(5)
driver.quit()
