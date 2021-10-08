from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Python自动化测试\10.6的资料\练习的html\弹框的验证\dialogs.html')
driver.maximize_window()
driver.find_element_by_id("alert").click()
time.sleep(2)
driver.switch_to.alert.accept()
#点击确定
time.sleep(1)
driver.find_element_by_id("confirm").click()
time.sleep(1)
driver.switch_to.alert.dismiss()
#点击取消
time.sleep(2)
driver.quit()
