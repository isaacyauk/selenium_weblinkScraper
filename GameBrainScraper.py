from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ChromeDriverMethods import ChromeDriverMethods

if __name__ == "__main__":

    # Get the Chrome Driver
    driver = webdriver.Chrome()

    # Pass it into the ChromeDriverMehtods class
    chromeDriver = ChromeDriverMethods(driver)
    chromeDriver.getURL("https://store.steampowered.com/search/")

