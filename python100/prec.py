'''
在屏幕上显示跑马灯文字'''

# import os
# import time
#
# def main():
#     content = '上海欢迎您.....'
#     while True:
#         #清理屏幕上的输出
#         # os.system('cls') #os.system('clear')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:]+content[0]
#         # print(content,'---------')
# if __name__ == '__main__':
#     main()



'''设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。'''
# import random
#
# def generate_code(code_len=4):
#     '''
#     生成指定长度的验证码
#     :param code_len：验证码长度
#     ：:return：由大小写英文字母和数字构成随机验证码
#
#     '''
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     print('last_pos: ',last_pos)
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0,last_pos)
#         code += all_chars[index]
#     return code
#
# print(generate_code())


'''设计一个函数返回给定文件名的后缀名。'''
#
# def get_surffix(filename,has_dot=False):
#     '''
#     获取文件名后缀
#
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     '''
#     pos = filename.rfind('.')
#     print('pos: ',pos)
#     if 0<pos<len(filename)-1:
#         index = pos if has_dot else pos+1
#         print('index: ',index)
#         return filename[index:]
#     else:
#         return ''
# print(get_surffix('python.py'))


#
# content = 'abcderf12345'
# s = content.find('c')
# e = content.rfind('c')
#
# print('s: ',s)
# print('e: ',e)
#
#





# '''练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。'''
#
# def max2(x):
#     m1,m2 = (x[0],x[1] if x[0] > x[1] else(x[1],x[0]))
#     for index in range(2,len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1,m2
#
# print(max2([11,22,456,7777777,8,1,4444444444,6]))



'''练习5：计算指定的年月日是这一年的第几天'''
#
# def is_leap_year(year):
#     '''判断指定年份是不是闰年
#     :prarm year :年份
#     ：returm ： 闰年返回true  平年返回false
#
#     '''
#     return year % 4 == 0 and year %100!= 0 or year%400 == 0
# # print('---------',is_leap_year(1980))
# def which_day(year,month,date):
#     '''
#
#     :param year:
#     :param month:
#     :param date:
#     :return: 第几天
#     '''
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#
#     print('days_of_month: ',days_of_month)
#     total = 0
#     for index in range(month - 1):
#         total+= days_of_month[index]
#     return total+date
#
# def main():
#     print(which_day(1981,11,28))
# if __name__=='__main__':
#     main()
#

'''杨辉三角'''
#
# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     print('yh: ',yh)
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         print('yh[row]: ',yh[row])
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()
#
#
# if __name__ == '__main__':
#     main()
#



# '''双色球选号'''
# from random import randint,randrange,sample
#
# def display(balls):
#     '''
#     输出列表中的双色球号码
#     :param balls:
#     :return:
#     '''
#     for index,ball in enumerate(balls):
#         if index == len(balls) - 1:
#             # print('index: ',index)
#             print('|',end=' ')
#         print('%02d' %ball,end=' ')
#     print()
# def random_select():
#     '''
#     随机选择一组号码
#     :return:
#     '''
#     red_balls = [x for x in range(1,34)]
#     select_balls = []
#     select_balls = sample(red_balls,6)
#     select_balls.sort()
#     select_balls.append(randint(1,16))   #再加一个数进去，范围是（1，16）的数
#     return select_balls
#
#
# def main():
#     n = int(input('机选几注： '))
#     for _ in range(n):
#         display(random_select())
#
#
# if __name__=='__main__':
#     main()

'''约瑟夫环'''
# def main():
#     persons = [True] * 30
#     # print('persons: ',persons)
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1   #执行15次
#                 number = 0
#         index += 1
#         index %= 30
#         print('---------------------',index)
#         # print('---------------------',counter(index))
#
#     for person in persons:
#         print('1' if person else '0', end=' ')


# if __name__ == '__main__':
#     main()
#



'''井字棋'''

import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()


















