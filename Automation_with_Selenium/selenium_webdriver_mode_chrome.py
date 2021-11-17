# import the required libraries
from selenium import webdriver
import time


# options
options = webdriver.ChromeOptions()
# user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")

# disable webdriver mode
# # for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or over
# options.add_experimental_option('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-blink-features=AutomationControlled")


# initialization of the web driver
driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe", options=options)

# URL to the page
url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

try:
    # requests
    driver.get(url=url)
    time.sleep(5)

except Exception as ex:
    # error processing
    print(ex)
finally:
    # close the web driver
    driver.close()
    driver.quit()
