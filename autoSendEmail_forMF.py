# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# 打开126
driver.get('https://www.126.com')
time.sleep(1)

# 输入用户名和密码
# 切换frame
driver.switch_to.frame(0)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").clear()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys("emilymengforMF")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys("123Mf456")

# 登陆
# 释放frame
driver.switch_to.default_content
driver.find_element_by_id('dologin').click()

time.sleep(1)

# 点击 写信 按钮
driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]").click()
time.sleep(1)

# 输入 收件人
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("suixin-computer@126.com")
time.sleep(1)

# 回车确认输入 邮箱收件人 完成
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys(Keys.ENTER)
time.sleep(1)

# 输入 邮件主题
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/section/header/div[2]/div[1]/div/div/input").send_keys("很想加入MF")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/section/header/div[2]/div[1]/div/div/input").send_keys(Keys.ENTER)
time.sleep(1)

# 输入 邮件内容
# 定位文本需要通过frame
f1 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/section/section/div/div[1]/div[1]/div[2]/iframe")
driver.switch_to.frame(f1)

driver.find_element_by_xpath("/html/body").clear()
driver.find_element_by_xpath("/html/body").send_keys("这是为应聘MF写的一个自动化脚本，自动发送邮件")

driver.find_element_by_xpath("/html/body").send_keys(Keys.ENTER)
time.sleep(1)

# 点击发送
# 释放 frame
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@class="jp0"]/div[@role="button"][1]').click()

# 退出
driver.quit()
