from selenium import webdriver
import rest_app
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(r"C:\Users\MY PC\OneDrive\Documents\chromedriver.exe")
driver.get('http://127.0.0.1:5000/users')
time.sleep(10)


