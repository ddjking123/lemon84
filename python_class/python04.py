# 123
"""
list1=['贝贝','晶晶','欢欢','莹莹','妮妮']
list2 =[]  #空列表
for i in range (len(list1)):
    dict1 = dict(name=list1[i],age=18,gender='female',citu='北京')
    list2.append(dict1)
print(list2)

dict6 = {"name":"贝贝","gender":"male","age":18,"city":"深圳"}
for i in dict6:
    print(dict6.get(i))
"""
import jsonpath as jsonpath
import requests

"""
python的函数
函数使用：一段代码频繁使用，封装为函数--写一次就够，下次直接调用==提高代码的复用率
def 函数名()：
    函数体---具体实现功能的代码段
1、定义函数--def，不会执行，调用函数----只有被调用的时候才会执行
2、一些经常变化的内容不适合放在函数体内写死--最好参数化
函数参数定义：
1、定义--形参--变量
2、调用函数--传参--实参--值

定义的参数的类型
1、必备参数：定义了必须传入，不传报错
2、默认参数（缺省参数）：定义的时候给默认值，调用时不需要传入，如果传入选择传入值
注意：位置需要在非默认参数后面
3、不定长参数 ==不确定长度
*args：当前面的参数都被接受完成，剩下元素被他接受，并以元组格式保存,args名字可变，一般不做更改
*args在什么位置前面数据接受完到*args后数据都给他，位置看需求摆放
位置传参
**kwargs
名字一般不改
关键字传参，以字典形式保存，位置一定要放在最后
函数调用时传入参数方式
1、位置传参，位置不能乱
2、关键字传参：指定形参的变量名进行传参==位置无关==准确
3、混合传参：关键字参数必须要在位置参数的后面，否则报错，而且不能重复传
"""
# def good_job():
#     salary = 8000
#     bonus = 2000
#     subsidy =500
#     sum1 = salary + bonus +subsidy
#     print(sum1)
# good_job()  #调用函数
#
# def good_job(salary,bonus,subsidy=500,*args,**kwargs):
#     print("参数salary：{}".format(salary))
#     print("参数bonus：{}".format(bonus))
#     print("参数subsidy：{}".format(subsidy))
#     print("参数args：{}".format(args))
#     print("参数kwargs：{}".format(kwargs))
#     sum1 = salary + bonus + subsidy
#     for i in args:
#         sum1 +=i
#     for j in kwargs:
#         sum1 +=kwargs[j]
#     print('工资总和：{}'.format(sum1))
#     return sum1,salary

# result 这个变量接受 函数调用=返回值
# result = good_job(8000,2000,800,466,566,688,a=100,b=200,c=300)  #调用函数
# print(result)
# if result > 12000:
#     print('这是个好工作'.format(result))
# else:
#     print('不行')

# 函数返回值
# 函数需要给使用者抛出数据，后续使用==改数据，返回值
# 1、可以有，可以不用return,没有返回值返回==none
# 2、多个，逗号隔开进行返回，接受返回元组保存
# 3、定义之后如何使用--接受后续使用
# 4、返回值标志代码结束--后续代码不再执行--放在最后

"""
内置函数：
print
input
type
isinstance
len
range
str、int、floor、tuple、dict
字符串内置方法：format，index，find，replace
列表内置方法：append，insert，pop，remove，extend，clear，count，index
字典：get，update，pop，keys，value，items



代码测试
1、断点，点击行首前红点可以的点击绿色小瓢虫，debug模式step into
代码出错，使用调试功能
"""

# 作业
# 将字符串分割转换成列表
# str1= ‘hello python world’
# list1=list(str1)  #拆开每个元素
# # 字符串内置函数split：将一个字符串以一个指定符号截断，返回列表--num-截取次数，默认-1最后
# list2 = str1.split(' ')
# print(list2)

# 求任意整数和
# num1 = int(input('请输入整数'))
# sum1 = 0
# for i in range(num1):
#     sum1 += i
# print(sum1)

# 或者
# def add_hh(num2):
#     sum2 = 0
#     for i in range(num2):
#         sum2 +=i
#     return sum2
# result = add_hh(int(input('请输入一个整数')))
# print('这个整数序列的和为：{}'.format(result))
# 判断一个元素
# def object (items):
#     if isinstance(items,list) or isinstance(items,tuple) or isinstance(items,dict):
#     #if type(items) == list or type(items) ==dict or type(items) ==tuple:
#         length = len(items)
#         if length > 5:
#             print('TURE')
#         else:
#             print('FALSE')
#     else:
#         print('你输入的数据类型不能计算长度！')
#
# object([123456])
"""
http接口自动化：第三方库，---安装+导入==requests
pip： 安装Python的第三方库 pip install requests
pycharm里面也可以安装
request库传输参数必须是字典格式
"""
# import requests
# import pprint #pprint --prety prind
#
# #注册接口
# url_register ='http://47.115.15.198:7001/smarthome/user/register'  #定义接口位置
# data_register = {'phone':'13577444487','pwd':'lemon123',
# 'rePwd':'lemon123','userName':'ddj124','verificationCode':'lemon'}
# head = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}
# response = requests.post(url=url_register,json=data_register,headers=head)
# pprint.pprint((response.json()))
# #登录接口
#
# url_login = 'http://47.115.15.198:7001/smarthome/user/login'  #定义接口位置
# data_login = {'pwd':'lemon123','userName':'ddj124'}
# head_login = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}
# response = requests.post(url=url_login,json=data_login,headers=head_login)
# pprint.pprint((response.json()))
# login_resp = response.json()
#
"""
{'code': '0',
 'data': {'id': 2028,
          'phone': '13577444487',
          'token_info': {'expires_in': '2021-07-23 17:26:54',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiMjAyOCIsImV4cCI6MTYyNzAzMjQxNH0.
                         M0TEubCpWPGF-C6M8AuWx2ZvvKUCMPmXu-bDc3ByvOPr3pT0M2MEVug7gK1147kWGxVWQ7QU7-SJc1AW9zBNuQ',
                         'token_type': 'Bearer'},
          'type': False,
          'user_name': 'ddj124'},
 'msg': '操作成功'}

Process finished with exit code 0

完善信息
先获取登录返回信息中的id和token
id = login_resp['data']['id']
token = login_resp['data']['token_info']['token']
方法二：jsonpath--第三方库，安装dos命令：pip install jsonpath
id = jsonpath.jsonpath(login_resp,'$..id')[0]  #取出为列表的值，还要去列表中的值
token = jsonpath.jsonpath(login_resp,'$..token')[0]
"""

# id = login_resp['data']['id']
# token = login_resp['data']['token_info']['token']
# url_comp = 'http://47.115.15.198:7001/smarthome/merchant/complete'
# data_comp = {
#   "address": "湖南省长沙市岳麓区xx街道12345678901234567",
#   "establishDate": "2021-04-02",
#   "legalPerson": "韩",
#   "licenseCode": "xh430646464sdfa",
#   "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
#   "merchantName": "青海文梅科技有限公司1234567890",
#   "merchantType": 2,
#   "registerAuthority": "城中区派出所123456789012345678901234",
#   "tel": "18888888888",
#   "userId": id,
#   "validityDate": "2033-05-02"
# }
# head_comp = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer '+token}
# response = requests.put(url=url_comp,json=data_comp,headers=head_comp)
# print(response.json())
"""
# 扩展面试题
# 获取百度页面的请求get
#问题
# 有乱码
# 1、print(res_baidu.text）:text获取内容，自动解码，部分不能解码
# 2、print(res_baidu.content.decode('utf-8')):手动指定解码方式
#页面错误--百度服务器未返回正确页面
# 大型服务器：反爬虫机制
# User-Agent：Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
可整体定义为函数不用注释,封装为函数体；选中tab整体缩进
"""

def baidu_re():
  url_baidu = 'https://www.baidu.com/'
  head_baidu = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
  res_baidu = requests.get(url=url_baidu, headers=head_baidu)
  print(res_baidu.content.decode('utf-8'))

"""
向百度发起一个带参数的请求
https://www.baidu.com/s?wd=柠檬班   # /s为路径；？后面是参数，参数的名字等于参数的值；&后面是并列参数
"""

url_baidu = 'https://www.baidu.com/s'
head_baidu = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
para = {"wd":"海贼王"}
res_baidu = requests.get(url=url_baidu, headers=head_baidu,params=para)
print(res_baidu.content.decode('utf-8'))


