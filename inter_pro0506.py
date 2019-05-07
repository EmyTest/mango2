# a=['1','2','3','4','5']
# print(a[0:3])
# print(a[-1:-3:-1])
# print(a[-1::-1])
# print(a[::2])

# list1='hello'
# list2='world'
# list3 = list1 + list2
# print(list3)
# print(list3.count('o'))
# print(list3.upper())

# b = 'i am a owesome geeker !'
# print(b.split())
# zoo = {'1':'cat','2':'dog','3':'monkey'}
# key = '4'
# value = 'panda'
# zoo[key] = value
# print(zoo)


# print([x**2 for x in range(1,11)])
# print([(lambda x:x**2) (x) for x in range(1,11)])




# print(list(map(lambda x:x*x,range(1,11))))



# #遍历
# import os
# dir = "D:\\"
# def aa():
#     for root,dirs,files in os.walk(dir):
#         for file in files:
#             print(os.path.join(root,file))
# print(aa())









# import os
#
# def all_path(dirname):
#
#     result = []#所有的文件
#
#     for maindir, subdir, file_name_list in os.walk(dirname):
#
#         print("1:",maindir) #当前主目录
#         print("2:",subdir) #当前主目录下的所有目录
#         print("3:",file_name_list)  #当前主目录下的所有文件
#
#         for filename in file_name_list:
#             apath = os.path.join(maindir, filename)#合并成一个完整路径
#             result.append(apath)
#
#     return result
#
# print(all_path("D:\CloudMusic"))



# import os
#
# filter=[".pdf"] #设置过滤后的文件类型 当然可以设置多个类型
#
# def all_path(dirname):
#
#     result = []#所有的文件
#
#     for maindir, subdir, file_name_list in os.walk(dirname):
#
#         # print("1:",maindir) #当前主目录
#         # print("2:",subdir) #当前主目录下的所有目录
#         # print("3:",file_name_list)  #当前主目录下的所有文件
#
#         for filename in file_name_list:
#             apath = os.path.join(maindir, filename)#合并成一个完整路径
#             ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
#
#             if ext in filter:
#                 result.append(apath)
#
#     return result
#
# print(all_path("D:\Python_PDF"))



"""map函数
map() 会根据提供的函数对指定序列做映射。
https://www.cnblogs.com/GatsbyNewton/p/4784049.html
python3里面的map函数的问题

"""
# def square(x):
#     return x**2
# print(list(map(square,[1,2,3,4,5])))
# print(list(map(lambda x:x**2,[1,2,3,4,5])))
# print(list(map(lambda x,y:x+y,[1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))






"""filter函数
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

"""

# def is_odd(n):
#     return n%2 == 1
# tmplist1 = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
# tmplist2 = map(is_odd,[1,2,3,4,5,6,7,8,9,10])   #???
# newlist1 = list(tmplist1)
# newlist2 = list(tmplist2)
# print(newlist1)
# print(newlist2)
"""filter 是通过生成 True 和 False 组成的迭代器将可
迭代对象中不符合条件的元素过滤掉；而 map 返回的则是 
True 和 False 组成的迭代器。"""



'''在 Python3 中，reduce() 函数已经被从全局名字空间里
移除了，它现在被放置在 functools 模块里，如果想要使用
它，则需要通过引入 functools 模块来调用 reduce() 函数：'''
# from functools import reduce
#
# def add(x,y):
#     return x+y
# print(reduce(add,range(1,101)))



"""
map()：【遍历】序列，对序列中每个元素进行操作，最终获取新的序列

reduce()：对于序列内所有元素进行【累计】操作，即是序列中后面的元素与前面的元素做累积计算（结果是所有元素共同作用的结果）

filter()：‘【筛选函数】’，filter()把传人的函数依次作用于序列的每个元素，然后根据返回值是True还是false决定保留还是丢弃该元素，返回符合条件的序列

"""


