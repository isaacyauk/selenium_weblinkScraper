from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ChromeDriverMethods:
    def __init__(self, driver):
        self.driver = driver

    def getURL(self, url):
        self.driver.get(url)




    # Define how many times to scroll (you can adjust this number)
    def scrollToResultsUntil(self, duration):
        # Find the element you want to scroll to
        element = self.driver.find_element(by=By.XPATH, value="//span[text()='More results']")
        start_time = time.time()

        while time.time() - start_time < duration:
            # Execute JavaScript to scroll the page down to the element
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

            try:
                element.click()
            except:
                continue

    def scrapeAllVisibleLinks(self):
        links = self.driver.find_elements(by=By.XPATH, value="//span//a[@jsname]")
        # this loop looks at all the "Cite" results on the DOM and checks for if it is a link or not.
        for link in links:
            href = link.get_attribute('href')
            print(href)

