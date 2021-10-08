from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get(r"D:/Python自动化测试/10.6的资料/练习的html/滑动验证/mousedrag.html")
driver.maximize_window()
f = driver.find_element_by_xpath("//*[@class = 'iconfont icon-double-right']")
action = ActionChains(driver)
#定义一个指针
action.click_and_hold(f)
#点击和抓按(长按)
action.move_by_offset(284, 0)

action.release()
#释放 鼠标松开
action.perform()
# perform，执行的意思
time.sleep(1)
driver.quit()
