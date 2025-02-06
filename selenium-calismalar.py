from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Create a function to open a website, wait for 2 seconds, then close it
def open_and_close(url):
    # Initialize WebDriver (ChromeDriver is assumed to be in system PATH)
    service = Service()  # No need to specify path if it's in PATH
    driver = webdriver.Chrome(service=service)

    # Open the given URL
    driver.get(url)
    
    # Wait for 2 seconds to simulate user viewing the page
    time.sleep(2)
    
    # Close the browser
    driver.quit()

# Open Google
open_and_close("https://www.google.com")

# Open YouTube
open_and_close("https://www.youtube.com")

# Open Facebook
open_and_close("https://www.facebook.com")
