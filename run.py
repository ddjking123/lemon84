
from commen import method
from testdata import data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#读取数据
url = data.data_t.get("url")
name = data.data_t["name"]
passwd = data.data_t["passwd"]
key = data.data_t["key"]
print(driver,name,passwd,key,url)
result = method.serch_fun(driver=driver,name=name,passwd=passwd,key=key,url=url)
print(result)
if key in result:
    print("搜索成功")