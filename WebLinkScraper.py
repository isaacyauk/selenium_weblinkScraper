from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://google.com")

# Search Query and "ENTER" keypress
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys("Dogs")
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
searchResults = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div//cite")))
# location of weblink
#searchResults = driver.find_elements(by=By.XPATH, value="//div//cite")

# this loop looks at all the "Cite" results on the DOM and checks for if it is a link or not.
for result in searchResults:
    link = result.text

    # This is the equivalent of "contains" in python.
    if "http" in link:
        print(link)
    # thing = driver.find_element(by=By.XPATH, value="//cite").text


#thing = driver.find_element(by=By.XPATH, value=f"(//cite)[{i}]").text

