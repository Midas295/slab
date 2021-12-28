# 文件名:parameter.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:本文件用于定义参数，如混凝土的强度，钢筋的强度，取整函数

def fc(C):
    '''
    :param C: 混凝土强度等级
    :return: 混凝土抗压设计值fc,单位N/mm^2
    '''
    if C.isdigit() == True:
        C = float(C)

    if (C == 'C15') or (C == 'c15') or (C == 15.0) :
        return 7.2
    elif (C == 'C20') or (C == 'c20') or (C == 20.0):
        return 9.6
    elif (C == 'C25') or (C == 'c25') or (C == 25.0):
        return 11.9
    elif (C == 'C30') or (C == 'c30') or (C == 30.0):
        return 14.3
    elif (C == 'C35') or (C == 'c35') or (C == 35.0):
        return 16.7
    elif (C == 'C40') or (C == 'c40') or (C == 40.0):
        return 19.1
    elif (C == 'C45') or (C == 'c45') or (C == 45.0):
        return 21.1
    elif (C == 'C50') or (C == 'c50') or (C == 50.0):
        return 23.1
    elif (C == 'C55') or (C == 'c55') or (C == 55.0):
        return 25.3
    elif (C == 'C60') or (C == 'c60') or (C == 60.0):
        return 27.5
    elif (C == 'C65') or (C == 'c65') or (C == 65.0):
        return 29.7
    elif (C == 'C70') or (C == 'c70') or (C == 70.0):
        return 31.8
    elif (C == 'C75') or (C == 'c75') or (C == 75.0):
        return 33.8
    elif (C == 'C80') or (C == 'c80') or (C == 80.0):
        return 35.9
    else:
        return 'error1'
def ft(C):
    '''
    :param C: 混凝土强度等级
    :return: 混凝土抗拉设计值ft,单位N/mm^2
    '''
    if C.isdigit() == True:
        C = float(C)

    if (C == 'C15') or (C == 'c15') or (C == 15.0):
        return 0.91
    elif (C == 'C20') or (C == 'c20') or (C == 20.0):
        return 1.10
    elif (C == 'C25') or (C == 'c25') or (C == 25.0):
        return 1.27
    elif (C == 'C30') or (C == 'c30') or (C == 30.0):
        return 1.43
    elif (C == 'C35') or (C == 'c35') or (C == 35.0):
        return 1.57
    elif (C == 'C40') or (C == 'c40') or (C == 40.0):
        return 1.71
    elif (C == 'C45') or (C == 'c45') or (C == 45.0):
        return 1.80
    elif (C == 'C50') or (C == 'c50') or (C == 50.0):
        return 1.89
    elif (C == 'C55') or (C == 'c55') or (C== 55.0):
        return 1.96
    elif (C == 'C60') or (C == 'c60') or (C == 60.0):
        return 2.04
    elif (C == 'C65') or (C == 'c65') or (C == 65.0):
        return 2.09
    elif (C == 'C70') or (C == 'c70') or (C == 70.0):
        return 2.14
    elif (C == 'C75') or (C == 'c75') or (C == 75.0):
        return 2.18
    elif (C == 'C80') or (C == 'c80') or (C == 80.0):
        return 2.22
    else:
        return 'error1'

def ftk(C):
    '''
    :param C: 混凝土强度等级
    :return: 混凝土抗拉标准值ftk,单位N/mm^2
    '''
    if C.isdigit() == True:
        C = float(C)

    if (C == 'C15') or (C == 'c15') or (C == 15.0):
        return 1.27
    elif (C == 'C20') or (C == 'c20') or (C == 20.0):
        return 1.54
    elif (C == 'C25') or (C == 'c25') or (C == 25.0):
        return 1.78
    elif (C == 'C30') or (C == 'c30') or (C == 30.0):
        return 2.01
    elif (C == 'C35') or (C == 'c35') or (C == 35.0):
        return 2.20
    elif (C == 'C40') or (C == 'c40') or (C == 40.0):
        return 2.39
    elif (C == 'C45') or (C == 'c45') or (C == 45.0):
        return 2.51
    elif (C == 'C50') or (C == 'c50') or (C == 50.0):
        return 2.64
    elif (C == 'C55') or (C == 'c55') or (C == 55.0):
        return 2.74
    elif (C == 'C60') or (C == 'c60') or (C == 60.0):
        return 2.85
    elif (C == 'C65') or (C == 'c65') or (C == 65.0):
        return 2.93
    elif (C == 'C70') or (C == 'c70') or (C == 70.0):
        return 2.99
    elif (C == 'C75') or (C == 'c75') or (C == 75.0):
        return 3.05
    elif (C == 'C80') or (C == 'c80') or (C == 80.0):
        return 3.11
    else:
        return 'error1'

def Ec(C):
    '''
    :param C: 混凝土强度等级
    :return: 混凝土弹性模量Ec 单位10^4N/mm^2
    '''
    if C.isdigit() == True:
        C = float(C)

    if (C == 'C15') or (C == 'c15') or (C == 15.0):
        return 2.20
    elif (C == 'C20') or (C == 'c20') or (C == 20.0):
        return 2.55
    elif (C == 'C25') or (C == 'c25') or (C == 25.0):
        return 2.80
    elif (C == 'C30') or (C == 'c30') or (C == 30.0):
        return 3.00
    elif (C == 'C35') or (C == 'c35') or (C == 35.0):
        return 3.15
    elif (C == 'C40') or (C == 'c40') or (C == 40.0):
        return 3.25
    elif (C == 'C45') or (C == 'c45') or (C == 45.0):
        return 3.35
    elif (C == 'C50') or (C == 'c50') or (C == 50.0):
        return 3.45
    elif (C == 'C55') or (C == 'c55') or (C == 55.0):
        return 3.55
    elif (C == 'C60') or (C == 'c60') or (C == 60.0):
        return 3.60
    elif (C == 'C65') or (C == 'c65') or (C == 65.0):
        return 3.65
    elif (C == 'C70') or (C == 'c70') or (C == 70.0):
        return 3.70
    elif (C == 'C75') or (C == 'c75') or (C == 75.0):
        return 3.75
    elif (C == 'C80') or (C == 'c80') or (C == 80.0):
        return 3.80
    else:
        return 'error1'


def fy(Fy):
    '''
    :param Fy: 钢筋等级
    :return: 钢筋抗拉设计值
    '''
    if Fy.isdigit() == True:
        Fy = float(Fy)

    if (Fy == 'HPB300') or (Fy == 1.0):
        return 270.0
    elif (Fy == 'HRB335') or (Fy == 2.0):
        return 300.0
    elif (Fy == 'HRB400') or (Fy == 3.0):
        return 360.0
    elif (Fy == 'HRB500') or (Fy == 4.0):
        return 435.0
    else:
        return 'error2'

def fys(Fy):
    '''
    :param Fy:钢筋等级
    :return: 钢筋抗压设计值
    '''
    if Fy.isdigit() == True:
        Fy = float(Fy)

    if (Fy == 'HPB300') or (Fy == 1.0):
        return 270.0
    elif (Fy == 'HRB335') or (Fy == 2.0):
        return 300.0
    elif (Fy == 'HRB400') or (Fy == 3.0):
        return 360.0
    elif (Fy == 'HRB500') or (Fy == 4.0):
        return 410.0
    else:
        return 'error2'

def Es(Fy):
    '''
    :param Fy:钢筋等级
    :return: 钢筋弹性模量 ，单位10^5N/mm^2
    '''
    if Fy.isdigit() == True:
        Fy = float(Fy)

    if Fy == 'HPB300' or (Fy == 1.0):
        return 2.10
    elif Fy == 'HRB335' or (Fy == 2.0):
        return 2.00
    elif Fy == 'HRB400' or (Fy == 3.0):
        return 2.05
    elif Fy == 'HRB500' or (Fy == 4.0):
        return 1.95
    else:
        return 'error2'

def Area_1(n,s):
    '''

    :param n: 钢筋根数
    :param s: 钢筋直径
    :return: n根直径为s的钢筋配筋面积
    '''
    N = float(n)
    S = float(s)
    return N * (S ** 2) * 3.14 * 0.25

def Area_2(s,d):
    '''

    :param s:钢筋直径
    :param d: 钢筋间距
    :return: 1延米内直径为s，间距为d的钢筋配筋面积
    '''
    D = float(d)
    S = float(s)
    return 1000/D * (S ** 2) * 3.14 * 0.25

def round_up(a,b):
    '''

    :param a:跨度，单位毫米
    :param b:除数，如27
    :return: 取整商
    '''
    if float(a) % float(b) == 0.0:
        return float(a)/float(b)
    else:
        return (float(a) // (10.0 * float(b) ) +1) *10.0

def is_floatorint(s): #判断是否是小数或者整数
    s = str(s)
    if s.count('.') == 1:  # 判断小数点个数
        sl = s.split('.')  # 按照小数点进行分割
        left = sl[0]  # 小数点前面的
        right = sl[1]  # 小数点后面的
        if left.startswith('-') and left.count('-') == 1 and right.isdigit():
            lleft = left.split('-')[1]  # 按照-分割，然后取负号后面的数字
            if lleft.isdigit():
                return True
        elif left.isdigit() and right.isdigit():
            # 判断是否为正小数
            return True
    elif s.isdigit() == True:
        return True
    return False


if __name__ == '__main__':
    print(round_up(2700,27))
    print(round_up(2400, 27))
    print(round_up(2700.11, 27))


