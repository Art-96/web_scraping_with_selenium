# import the required libraries
from selenium import webdriver
import time


# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# or
# options.headless == True


# initialization of the web driver
driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe", options=options)

# URL to the page
url = "https://www.avito.ru/moskva_i_mo/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1"

try:
    # requests
    driver.get(url=url)
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")
    # time.sleep(3)
    driver.implicitly_wait(5)

    items = driver.find_elements_by_xpath('//a[@data-marker="item-title"]')
    items[0].click()
    # print(driver.window_handles)
    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(3)
    driver.implicitly_wait(5)
    print(f"Currently URL is: {driver.current_url}")

    username = driver.find_element_by_xpath('//div[@data-marker="seller-info/name"]/a')
    print(f"User name is: {username.text}")
    # time.sleep(3)
    driver.implicitly_wait(5)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(2)
    driver.implicitly_wait(5)
    print(f"Currently URL is: {driver.current_url}")

    items[1].click()
    # time.sleep(3)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(3)
    driver.implicitly_wait(5)
    print(f"Currently URL is: {driver.current_url}")

    username = driver.find_element_by_xpath('//div[@data-marker="seller-info/name"]/a')
    print(f"User name is: {username.text}")
    ad_date = driver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")


except Exception as ex:
    # error processing
    print(ex)
finally:
    # close the web driver
    driver.close()
    driver.quit()
