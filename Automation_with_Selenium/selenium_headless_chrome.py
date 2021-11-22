# import the required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import login, password
import time
import random
import pickle


# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
options.add_argument("--headless")
# or
# options.headless == True


# initialization of the web driver
driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe", options=options)

# URL to the page
url = "https://www.instagram.com/?hl=ru"

try:
    # requests
    driver.get(url=url)
    time.sleep(5)

    print("Passing authentication...")
    # entering email address
    email_input = driver.find_element_by_name("username")
    email_input.clear()
    email_input.send_keys(login)
    time.sleep(2)

    # entering password
    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(2)

    # click the login button
    login_button = driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
    login_button.click()

    # or simulation of pressing the enter button
    #password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    print("Going to the page...")

except Exception as ex:
    # error processing
    print(ex)
finally:
    # close the web driver
    driver.close()
    driver.quit()
    print("Close browser")
