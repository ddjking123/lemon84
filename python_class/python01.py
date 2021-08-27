"""标识符：python里面自己取得名字==命名规则 变量 函数==取名
#只能包含字母、数字和下划线
不能以数字开头
不能使用关键字
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
 'raise', 'return', 'try', 'while', 'with', 'yield']
建议：不同数字和字母之间用下划线隔开
注释：
1）单行注释#--#之后的内容被注释
2）多行注释"""""" ''''''
3）快捷方式：Ctrl+/  也可以用来取消注释
基本语法：；
1）代码顶格编写
2）缩进敏感：除了父子关系的代码，都不能加缩进  ==循环，函数
常用数据类型：
整型--整数--int；
浮点型--小数--float；
布尔型--TRUE=1，FALSE=0  ==bool
字符串--str，用成对引号包括的部分，单引号、双引号(可以嵌套);三引号（保留原代码格式）
查看数据类型typle()输出这个类型
isinstance()：判断数据类型结果是bool值；print(isinstance(20.1,int))
变量--储存数据（任意数据）
1、定义变量==赋值--变量声明--初始化
变量要被使用前，必须要先声明--没有报错
名字最好是英文含义
字符串编号：左往右0开始，右向左-1开始---[]索引
取多个值：切片，开始、结束、步长索引[::]可以省略默认值
len()统计元素个数
print(len());print(str1[:len(str1):1])
获取索引
print(str1.index())：index元素不存在会报错终止运行;
find()元素不存在返回值-1不会中断报错
.count统计元素个数
.replace替换
.replace(old,new,第几个)"""
"""
#字符串格式化输出
name ='翅尖'
gender = 'female'
age = '20'
hobby = '喜欢男'
print('''---{}的基本信息---
性别：{}
年龄：{}
爱好：{}
'''.format(name,gender,age,hobby))
花括号中可以指定位置0，-1
"""
"""
# 占位符{}
# 占位符$;$s占位字符串(万能占位符)；$d--整数；$f--浮点型
"""
# 运算符
# +数字相加，字符串拼接
# 强制转换类型：int();str();float();bool();lst()
# z只能数字相减
# *数字想成；表示重复输出次数love*3000
# /只能表数字相除
# =右边内容赋值给左;
# +=等同于a=a+10;
# -=等同于a=a-10
# 比较运算符<;>;>=;>=结果是布尔值bool(Ture,False)
# ==等于;!=不等于
# 逻辑运算符 or 或；and和；not非，结果也是布尔值
# 成员运算符 in；not in ，结果也是布尔值
# 列表，元组，字典，集合
# 列表元素可以包含任何的内容；索引从0开始和字符串使用一样
# list1 = [1,1,2,3,[1,1,2,3,6]]
# 嵌套取值print(list1[2][3])
# 获取元素个数---len()
# 列表元素可以修改，可以增删改查
# list1.append()添加
# list1.insert(位置,内容)指定位置插入
# list1.extend（）；多个元素扩展到列表，列表的合并，添加在末尾
# 删除
# list1.pop(位置);默认删除最后一个元素,也可以指定位置
# lsit1.remove(元素)；指定删除元素本身
# clear清除列表
# 赋值修改
# list1[0] = ''
# 列表元素可以重复，count统计个数
# input()；控制台获取输入内容

