# Siamo al minuto 48:13
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://live-tennis.eu/it/classifica-atp-live"
s = Service (r"/User/Mimmo/downloads/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get(url)
tables = driver.find_elements(By.TAG_NAME, "table")
for table in tables:
    print(table.text)