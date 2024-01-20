from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://google.com")

# Search Query and "ENTER" keypress
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys("Dogs")
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(Keys.ENTER)

# location of weblink
driver.find_element(by=By.XPATH, value="//cite").text()
