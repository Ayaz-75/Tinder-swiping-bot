from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

tinder_link = "https://tinder.com/"
chrome_diver_path = "D:\Development\chromedriver.exe"
s = Service(chrome_diver_path)


driver = webdriver.Chrome(service=s)
driver.get(tinder_link)

time.sleep(10)
login = driver.find_element(By.CLASS_NAME, "button")
login.click()


time.sleep(10)
fb_button = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_button.click()


base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


time.sleep(10)
fb_email = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_email.send_keys("your_email")

time.sleep(10)
fb_pass = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_pass.send_keys("your_password")
fb_pass.send_keys(Keys.ENTER)


driver.switch_to.window(base_window)
print(driver.title)










































# login_phone = driver.find_element(By.XPATH, "//*[@id='s369355022']/div/div/div[1]/div/div/div[3]/span/div[3]/button")
# login_phone.click()
#
# #
# time.sleep(5)
#
# phone = driver.find_element(By.CSS_SELECTOR, '#s369355022')
# if phone.text == "":
#     phone.send_keys("3408614246")
#     phone.send_keys(Keys.ENTER)

# print(phone.text)

# time.sleep(5)
# name = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div[1]/div/div[2]/div/input')
# name.send_keys("3408614246")
#












