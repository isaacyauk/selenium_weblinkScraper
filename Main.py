from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ChromeDriverMethods import ChromeDriverMethods

search_term = input("Enter desired search term: ")

if __name__ == "__main__":

    # Get the Chrome Driver
    driver = webdriver.Chrome()

    # Pass it into the ChromeDriverMethods class
    chromeDriver = ChromeDriverMethods(driver)
    chromeDriver.getURL("https://google.com")



    # Search Query and "ENTER" keypress
    driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(search_term)
    driver.find_element(by=By.CSS_SELECTOR, value="#APjFqb").send_keys(Keys.ENTER)

    chromeDriver.scrollToResultsUntil(30)
    chromeDriver.scrapeAllVisibleLinks()




print("end of scrape")

