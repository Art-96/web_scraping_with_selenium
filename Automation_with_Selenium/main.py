# import the required libraries
from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
# link to library fake user-agent https://github.com/hellysmile/fake-useragent

# URL to the page
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

user_agent_list =["Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
                  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"]
useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={random.choice(user_agent_list)}")
options.add_argument(f"user-agent={useragent.random}") # useragent.ie or useragent.chrome or useragent.opera

# initialization of the web driver
driver = webdriver.Chrome(
    executable_path="chromedriver\chromedriver.exe",
    options=options)

try:
    # requests
    driver.get(url=url)
    time.sleep(5)

    # refreshes the browser window
    # driver.refresh()

    # takes a screenshot of the open window
    # driver.get_screenshot_as_file("1.png")

except Exception as ex:
    # error processing
    print(ex)
finally:
    # close the web driver
    driver.close()
    driver.quit()
