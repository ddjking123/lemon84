# 123
# selenuim:UI自动化
"""
代码---翻译（浏览器驱动-driver）---浏览器
            chromedriver.exe  ---1、下载  2、解压exe 3、复制到Python安装目录中
Python/java
selenium-webdriver驱动 --发送指令（打开浏览器，网页） ---浏览器驱动接受-----驱动浏览器执行对应的操作
UI自动化发送指令和操作过程：
1、启动chromedriver之后，启动一个服务：ip端口 监听
2、Python的webdriver--chromedriver建立连接（http协议）
3、chromedriver收到webdriver指令之后，驱动浏览器执行操作
4、chromedriver把结果返回webdriver
5、继续发送后续的指令

selenium工具包，包括三个部分：--了解
1、ide--录制脚本
2、webdriver：库--提供了对网页操作的各种方法（点击、输入等操作）=各种语言版本，结合语言来使用
3、grid：分布式--多个浏览器执行开发
"""
from selenium import webdriver  # 从selenium工具包里导出webdriver
import time
driver = webdriver.Chrome()      #webdriver与chrome建立对话  ==赋值变量

"""
对浏览器的常用操作
1、打开某个网页
2、最大化窗口
3、页面回退、刷新、前进
4、关闭：quit()关闭窗口、浏览器、驱动
close关闭窗口
"""
# driver.get('https://baidu.com')
# driver.maximize_window()
# time.sleep(2)
#
# driver.get('https://taobao.com')
# time.sleep(2)
# driver.back()   #回退
# time.sleep(2)
# driver.forward()  #前进
# time.sleep(2)
# driver.refresh()  #刷新
# driver.close()   #关闭窗口

"""
web页面三部分
1、HTML：页面呈现的内容--标签语言
2、CSS：页面布局，字体颜色，字体大小
3、JavaScript：-js--控制页面

元素 = 标签+属性（id，name，class，type。。。）
id--开发遵循语法规定，id设置唯一，标准唯一
name--唯一

元素定位方法：八大元素定位=id，name，xpath，css，class，tag，link，partial_link===代码驱动操作
四大操作：
1、点击--click
2、输入--send_keys
3、获取文本text
4、获取属性：attribute --id属性
5、xpath：绝对路径--用的最多的定位方法--80%使用频率
绝对路径/html/body/div[2]/div/div[2]/div[2]/input==不能推荐方法，从根头开始/开头，逐级位置，继承关系--极易发生变化，大概率导致元素找不到
相对路径//*[@id="password"]---以//开头，某个标签+属性 ==相对稳定--推荐使用
开发中模式按住Ctrl+f最下变弹出搜索框
如果没有标签，往上级定位在找目标定位//
文本属性定位--文本唯一固定
//b[text()='']
6、包含定位contains
//标签名[contains(@属性名/text(),属性值)] --值/属性内容太长
--input[contains(@class,'username')]
--//span[contains(text(),'零售出库')]
轴定位
//input[@id='']/following-sibling::ins
"""
driver.get('http://erp.lemfix.com/login.html')
driver.maximize_window()
driver.find_element_by_id('username').send_keys('test123')  #代码找到元素，进行输入操作
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
# preceding-sibling向上寻找，following-sibling向后寻找

driver.find_element_by_id('btnSubmit').click()  #通过id找到按钮，进行点击操作，id换成name也可以