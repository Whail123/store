from selenium import webdriver
import time

driver = webdriver.Chrome()
# 百度
# driver.get(r"https://www.baidu.com/")
# driver.find_element_by_xpath("//*[@id = 'kw' and @class = 's_ipt']").send_keys("https://www.jd.com/")
# driver.find_element_by_xpath("//*[@type = 'submit']").click()
# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_xpath("//*[@id='1']/h3/a").click()

# 京东
driver.find_element_by_xpath("//*[@id = 'key' and @type = 'text']").send_keys("电脑")
driver.find_element_by_xpath("//*[@class = 'button' and @aria-label='搜索']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a").click()
time.sleep(10)
driver.quit()
