from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://shimo.im/desktop")
    time.sleep(1)
    name = browser.find_element_by_name('mobileOrEmail').send_keys('1234567@qq.com')
    passwd = browser.find_element_by_name('password').send_keys('xxxxx')

    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies=browser.get_cookies()
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()



