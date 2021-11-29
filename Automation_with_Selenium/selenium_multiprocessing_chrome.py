# import the required libraries
from selenium import webdriver
import time
from multiprocessing import Pool
import random


# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")

# URL to the page
# urls_list = ["https://stackoverflow.com/", "https://www.instagram.com/", "https://vk.com/"]

# def get_data(url):
#     try:
#         # initialization of the web driver
#         driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe", options=options)

#         driver.get(url=url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(f"media\{url.split('//')[1].strip('/')}.png")
        
#     except Exception as ex:
#         # error processing
#         print(ex)
#     finally:
#         # close the web driver
#         driver.close()
#         driver.quit()

# if __name__ == '__main__':
#     p = Pool(processes=3)
#     p.map(get_data, urls_list)



def get_data(url):
    try:
        # initialization of the web driver
        driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe", options=options)

        driver.get(url=url)
        time.sleep(5)
        
        driver.find_element_by_class_name('lazyload-wrapper').find_element_by_class_name('item-video-container').click()
        time.sleep(random.randrange(3, 10))

    except Exception as ex:
        # error processing
        print(ex)
    finally:
        # close the web driver
        driver.close()
        driver.quit()

if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)

    p = Pool(processes=process_count)
    p.map(get_data, urls_list)