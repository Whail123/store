from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"D:\Python自动化测试\10.6的资料\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()  # 窗口最大化

driver.find_element_by_xpath("//*[@id='accountID'  and  @name='account'  and  @type='text']").send_keys("liaison")
driver.find_element_by_xpath("//*[@id = 'passwordID' and @name = 'password' and @type = 'password']").send_keys('111')
driver.find_element_by_xpath("//*[@id = 'areaID']").send_keys("陕西省")
driver.find_element_by_xpath("//*[@id = 'sexID1']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@value = 'spring']").click()
driver.find_element_by_xpath("//*[@value = 'winter']").click()
driver.find_element_by_xpath("//*[@name = 'file' and @type = 'file']").send_keys(r"D:\专业课\1.jpg")
driver.find_element_by_xpath("//*[@id = 'buttonID' and @type = 'button']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(1)
driver.quit()
print("完成")
