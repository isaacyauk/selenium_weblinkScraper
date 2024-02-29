from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

search_term = input("Enter desired search term: ")

driver = webdriver.Chrome()


# Define how many times to scroll (you can adjust this number)
def scrollToResultsUntil(duration, times):
    for i in range(times):

        try:
            # Find the element you want to scroll to
            element = driver.find_element(by=By.XPATH, value="//span[text()='More results']")
            start_time = time.time()

            while time.time() - start_time < duration:
                # Execute JavaScript to scroll the page down to the element
                driver.execute_script("arguments[0].scrollIntoView();", element)

            element.click()
        except:
            break


driver.get("https://google.com")

# Search Query and "ENTER" keypress
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(search_term)
driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
searchResults = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='main']//span//a[@jsname]"))) # USE THE .HREF javascript element here!!

# this loop looks at all the "Cite" results on the DOM and checks for if it is a link or not.

scrollToResultsUntil(2, 200)

for result in searchResults:
    link = result.text

    # This is the equivalent of "contains" in python.
    if "http" in link:
        print(link)
    # thing = driver.find_element(by=By.XPATH, value="//cite").text

print("end of scrape")

