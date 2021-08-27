# 123

from selenium import webdriver  # 从selenium工具包里导入webdriver
import time

driver = webdriver.Chrome()      #webdriver 与chrome建立会话 ==赋值变量
driver.implicitly_wait(10)  #隐性等待--10秒
driver.get('http://erp.lemfix.com/login.html')
driver.maximize_window()
# 获取页面标题
title = driver.title   #赋值给title标题
if title == '柠檬ERP':
    print('这个页面的标题是：{}'.format(title))
else:
    print('这条测试不通过')

#第三条用例：登录
driver.find_element_by_name('username').send_keys('test123')  #代码找到元素，进行输入内容操作
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id('btnSubmit').click()

"""
元素的四大操作
1、点击--click
2、输入--send_keys
3、获取文本 --text
4、获取属性
问题：找到元素利用xpath定位输入位置运行报错？--进行点击操作之后，或者当前页面变化的时候为了避免未加载出来要添加等待--三种等待
1、强制等待time.sleep()---不灵活--time.sleep(2)
2、智能等待--等待元素出现/存在：
隐式等待；一般一个会话只执行一次，设置等待时间（10s）；只要元素出现、被找到，就会继续执行下去，如果一直未出现等待10s就会报错。
显式等待；
"""
# 判断是否登录成功
# time.sleep(2)
username = driver.find_element_by_xpath("/html/body/div[1]/aside/div/section/div[1]/div[2]/p").text  #获取这个元素文本信息
if username == '测试用户':
    print('登陆成功且用户名是：{}'.format(username))
else:
    print('测试不通过')

# 点开零售出库
driver.find_element_by_xpath('//span[contains(text(),"零售出库")]').click() # 获取id属性
"""
搜索编号-检索结果
问题，涉及到页面嵌套子页面，先找到子页面，切换到子页面再进行元素定位
如果元素标签路径中存在iframe说明页面肯定存在页面嵌套
如何浅灰子页面
1、通过id进行切换 ==  driver.switch_to.frame(id_iframe)  ==id
注意：id可以唯一，但是如果是变化的，就不能用来做元素定位！
2、通过webselement进行切换==driver.switch_to.frame (元素定位的表达式)
==//ifram[@id="tabpanel-dasdnjafa-fram"]
"""

id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute('id')  #获取id属性
id_iframe = id + "-frame"    #通过字符串的拼接得到iframe id
#通过id进行iframe切换
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
 # 通过webelement 来进行iframe切换
driver.find_element_by_id('searchNumber').send_keys('448')
driver.find_element_by_id('searchBtn').click()   #点击查询按钮
time.sleep(1) #隐性等待+强制等待
#获取编号文本
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
print(num)
if "448" in num:
    print('搜索成功')
else:
    print('用例不通过')
