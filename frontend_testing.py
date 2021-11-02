
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.chrome(r"C:\Users\MY PC\OneDrive\Documents\WebDrivers\chromedriver")
driver.get('http://localhost:5000/users')


#searchBox = driver.findElement(By.name("USER_ID"))

#search_box.send_keys("webdriver")

