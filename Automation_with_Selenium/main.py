# import the required libraries
from selenium import webdriver
import time

# URL to the page
url = "https://www.instagram.com/?hl=ru"
# initialization of the web driver
driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe")

try:
    # requests
    driver.get(url=url)
    time.sleep(5)

    # refreshes the browser window
    driver.refresh()

    # takes a screenshot of the open window
    driver.get_screenshot_as_file("1.png")

except Exception as ex:
    # error processing
    print(ex)
finally:
    # close the web driver
    driver.close()
    driver.quit()
