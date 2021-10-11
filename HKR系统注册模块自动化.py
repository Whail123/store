from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")

driver.maximize_window()

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='loginname']").send_keys('123')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys('123')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='pwd']").send_keys('123456')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys('123456')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()

driver.find_element_by_xpath("//*[@id='valid_age']").send_keys('21')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys('女')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='classname']").send_keys('python自动化')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys('1234567895@qq.com')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys('17315238267')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys('北京市昌平区')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='btn_reg']").click()


time.sleep(5)

driver.quit()


