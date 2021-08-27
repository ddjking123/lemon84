# 123
# name = input('请输入你的名字')
# age = input('请输入你的年龄')
# gender = input('请输入你的性别')
#
# print('''************
# 姓名：{}
# 年龄：{}
# 性别：{}
# **********'''.format(name,age,gender))
# 取出字符串字段，切片[0:6:1]

# 元组tuple
# 嵌套列表取值print(tuple1[第一个列表位置][里面第二个列表元素位置])
# tuple的元素不能改变，转变成列表然后修改在转回元组；.count()统计个数
# 字典
# 元素是一对键值对key：value；
# key是表头不能重复，不能是列表字典这些可变数据类型
# value可以重复任意数据类型
# 字典是无序的，通过key取value；print(dict1['key']);print(dict1.get('key'))
# 取所有键print(dict.keys());取所有值print(dict1.values());
# 取所有键值对print(dict1.items())存在列表中
# dict1['key'] = 'value'  ,key不存在的时候增加键值对，存在修改原来的值
# dict1.update({key1:value1,key2:value2})合并字典，key相同修改原字典值
# 删除
# dict1.pop(key)指定删除
# clear清除
# 集合==使用比较少  set{}
# 元素不能重复，用来列表去重--把列表转换成集合,去重和在转换成列表lsit
# set1 = set(list1)
# 常用数据类型
# 控制流：判断 if
# if 条件:   --判断（逻辑运算符、成员运算符、比较运算符） ==成立（True）冒号--后面缩进
#     执行语句（子代码）  ==四个空格缩进tab
# elif 并列判断，可多个
"""
money = int(input('请输入您的存款')) #input输入为字符串不能比较要转化
if money >=200:
    print('我要买大房子')
elif money >=100:
    print('理财')
elif money >=50:
    print('付彩礼，娶媳妇')
else:
    print('继续搬砖！')
"""

# 循环while--死循环：for 循环
# 使用场景：遍历--全部元素：字符串、list、tuple、dict  ==冒号后面缩进，循环体
# for循环元素取完就结束
# str1 = '我爱学习'
# count = 0
# for i in str1:
#     print(i)
#     print('$' * 4)
#     count +=1
# print(count)
# print(len(str1))
# 终止循环break：跳出循环，后面的循环不执行
# continue跳出本次循环，后面的循环依然会再次执行
# 作为for循环一起使用的内置函数range：生成一个整数序列 ==编号
# 开始数字默认0
# 结束数字需要输入
# 步长默认1
# for i in range(10):
#     print(i)
