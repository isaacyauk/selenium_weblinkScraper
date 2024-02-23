from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

search_term = input("Enter desired search term: ")

driver = webdriver.Chrome()


# driver = webdriver.Edge()

def scroll(times):
    # Define how many times to scroll (you can adjust this number)

    # Scroll to the bottom of the page
    for _ in range(times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def click(times):
    for _ in range(times):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div//span[contains(., 'More results')]")))
        driver.find_element(by=By.XPATH, value="//div//span[contains(., 'More results')]").click()


driver.get("https://google.com")

# Search Query and "ENTER" keypress
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(search_term)
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(Keys.ENTER)

#wait = WebDriverWait(driver, 10)
#wait.until(EC.visibility_of_element_located((By.XPATH, "//div//span[contains(., 'More results')]")))


wait = WebDriverWait(driver, 10)
searchResults = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div//cite")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//div//span[contains(., 'More results')]"))).click()

# location of weblink
# searchResults = driver.find_elements(by=By.XPATH, value="//div//cite")
click(7)
# this loop looks at all the "Cite" results on the DOM and checks for if it is a link or not.
for result in searchResults:
    link = result.text

    # This is the equivalent of "contains" in python.
    if "http" in link:
        print(link)
    # thing = driver.find_element(by=By.XPATH, value="//cite").text


moretest = driver.find_element(By.XPATH, value="//div//span[contains(., 'More results')]").click()

print("end of thing")

# thing = driver.find_element(by=By.XPATH, value=f"(//cite)[{i}]").text
