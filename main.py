# 文件名:main.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:本文件为主程序。。


import os
import VIDASSET as vidas
import positive as pot


while True:
    answer = input('''
----------板式楼梯计算器v1.0.0----------
开发时间：2021.10.20 02:01
本程序结果仅供参考，请自行核对计算结果，开发者不对结果承担任何责任！
#####################################
# 1.批量生成配筋计算书，输入1            #
# 2.查看VIDAS.SET文件，输入2             #
# 3.单次计算配筋，输入除1、2、e外任意值       #
# 4.退出，输入e                            #
#######################################
请输入:''')
    if answer == 'e':#退出程序
        break
    elif answer == '1':#批量生成配筋计算书
        pot.morefile(vset)
    elif answer == '2':
        if os.path.exists('VIDAS.SET'):
            print('配置文件存在，设置如下：')
            vidasset = open('VIDAS.SET')
            print(vidasset.read())
        else:
            print('配置文件不存在，改为默认设置：')
            vidasset = open('VIDAS.SET', 'w')
            vidasset.write(vidas.vset())
            vidasset.close()
            vidasset = open('VIDAS.SET')
            print(vidasset.read())
    if os.path.exists('VIDAS.SET'):
        vidasset = open('VIDAS.SET')
    else:
        vidasset = open('VIDAS.SET', 'w')
        vidasset.write(vidas.vset())
        vidasset.close()
        vidasset = open('VIDAS.SET')
    vset= vidas.vidasset(vidasset.read())
    pot.singlefile(vset)

# 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':

