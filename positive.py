# 文件名:positive.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:本文件用于执行主操作

import os
import VIDASSET as vidas
import inputset
import calc
import write

def singlefile(vset):
    '''
    执行单个文件用的vset
    :param vset:
    :return:
    '''
    vset = inputset.input1(vset)  # 处理输入的字典
    vset = calc.calcslab_1(vset)  # 计算得到需要的配筋值
    rset = vidas.rein_lib(vset['s'], vset['d'], vset['r'])
    vset['Rein_steady'] = vidas.rein_select(vset['S_steady'], rset)
    vset['Rein_span'] = vidas.rein_select(vset['S_span'], rset)
    print(vset['S_steady'])
    print(vset['Rein_steady'])
    print(vset['S_span'])
    print(vset['Rein_span'])
    # vset = vset.calcl(vset)
    # vset = vset.calcw(vset)
    # write.single(vset)

def morefile(vset):
    '''
    执行多个文件用的vset
    :param vset:
    :return:
    '''
    vset = inputset.input1(vset)  # 处理输入的字典
    vset = calc.calcslab_1(vset)  # 计算得到需要的配筋值
    rset = vset.rein_lib(vset['s'], vset['d'], vset['r'])
    vset = vset.rein_select(vset, rset)
    vset = vset.calcl(vset)
    vset = vset.calcw(vset)
    write.single(vset)