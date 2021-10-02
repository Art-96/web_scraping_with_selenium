# import the required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")



# initialization of the web driver
driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe", options=options)

# URL to the page
url = "https://www.instagram.com/?hl=ru"

try:
    # requests
    driver.get(url=url)
    time.sleep(5)

    # entering email address
    email_input = driver.find_element_by_name("username")
    email_input.clear()
    email_input.send_keys("your email or phone")
    time.sleep(2)

    # entering password
    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys("your password")
    time.sleep(2)

    # click the login button
    login_button = driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
    login_button.click()

    # or simulation of pressing the enter button
    #password_input.send_keys(Keys.ENTER)
except Exception as ex:
    # error processing
    print(ex)
finally:
    # close the web driver
    driver.close()
    driver.quit()
