# 一键隐藏电话号码和学号
import re

import openpyxl

def is_studentId(v1):
    '''
    判断是否为学号,这里是判断规则
    :param v1:
    :return:
    '''
    id = str(v1)
    ret = re.match(r"^[2sSbB]\d{9}$", id)
    if ret:
        return True
    else:
        return False

def hide_studentId(v1):
    '''
    学号隐藏规则
    :param v1:
    :return:
    '''
    return v1[:-2] + '*' * 2

def is_phonenumber(v1):
    '''
    :param v1:
    :return:
    '''
    tel = str(v1)
    ret = re.match(r"^1[35789]\d{9}$", tel)
    if ret:
        return True
    else:
        return False

def hide_phonenumber(v1):
    '''
    学号隐藏规则
    :param v1:
    :return:
    '''
    return v1[:3]+'*'*4+v1[-4:]

is_hide_studentId = True
is_hide_phonenumber = True

path = './6th创客.xlsx'
wb = openpyxl.load_workbook(path)
sh = wb['Sheet1']

for row in list(sh.rows):
    for i in row:
        v = i.value
        if is_hide_phonenumber and is_studentId(v):
            i.value = hide_studentId(v)

        if is_hide_phonenumber and is_phonenumber(v):
            i.value = hide_phonenumber(v)

        print(i.value,end=' ')
    print()

wb.save(path)
wb.close()