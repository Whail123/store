from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("wanghailong")

time.sleep(3)

driver.find_element_by_xpath("//*[@id='password']").send_keys("12345678")

time.sleep(3)

driver.find_element_by_xpath("//*[@id='submit']").click()

time.sleep(5)

driver.quit()




























































