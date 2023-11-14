from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
path="E:/chromedriver.exe"
s=Service(path)
driver=webdriver.Chrome(service=s)
# driver.implicitly_wait(60)
driver.get("https://www.google.com/")
time.sleep(10)
box=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[5]/div/div/div/div/div/div[1]/div/div/span/a/h3""").click()
time.sleep(2)
# time.sleep(30)