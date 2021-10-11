from selenium  import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys('wanghailong')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='password']").send_keys('12345678')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='submit']").click()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys('9(上晚自习)')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='tea_td']/select").send_keys('曹士明')

time.sleep(3)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='textarea']").send_keys('无')

time.sleep(2)

driver.find_element_by_xpath("//*[@id='subtn']").click()

time.sleep(4)

driver.quit()





