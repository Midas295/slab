# 文件名:inputset.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:本文件用于输入值是否在允许范围内的判断以及字符串的处理。

import parameter as para
import math

def strtofloat(vset,list1):
    '''
    :param vset: 字典
    :param lsit: 键值列表
    :return: 处理后的键值
    '''
    for i in range(len(list1)):
        if para.is_floatorint(vset[list1[i]])==True:
            vset[list1[i]] = float(vset[list1[i]])
    return vset


def inputslesct_1(vset,key1,value1,str1):
    '''
    :param vset: 输入字典
    :param key1: 字典的键值
    :param value1: 需要判断的值1，如none
    :param str: 提示文字
    :return:如果key1对应的键值等于value1，则提示str输入新的value1值
    '''
    if vset[key1] == value1:
        vset[key1] = input(str1)
    return vset


def inputslesct_3(vset,key1,value1,w1,w2,str1):
    '''
    :param vset:输入字典
    :param key1: 需判断的键值
    :param value1: 需要判断的值1，如none
    :param w1: 需要判断的值范围起始值，如1
    :param w2: 需要判断的值范围终值，如50
    :param str1: 需要判断的值范围终值，如50
    :return:输出一个在1~50之间的字典键值
    '''
    if (vset[key1] == value1) or (para.is_floatorint(vset[key1]) == False) or (float(vset[key1]) < float(w1)) or (float(vset[key1]) > float(w2)):
        while True:
            vset[key1] = input(str1)
            if (para.is_floatorint(vset[key1]) == True) and (float(vset[key1]) >= float(w1)) and (float(vset[key1]) <= float(w2)):
                break
    return vset

def input1(vset):
    '''
    :type vset: object
    :param vset: VIDAS.SET里的字典
    :return: 补充后的VIDAS字典
    '''
    vset=inputslesct_1(vset,'name','none','请输入标题，如LT1-AT3：')
    vset = inputslesct_1(vset, 'project_name_1', 'none', '请输入工程名：')
    vset = inputslesct_1(vset, 'project_name_2', 'none', '请输入项目名：')


    if (vset['con'] == 'none') or (para.CON_1(vset['con']) == 'error1'):
        while True:
            vset['con'] = input('请输入混凝土强度等级，如C30、c30、30：')
            if para.CON_1(vset['con']) != 'error1':
                break
    if (vset['fy'] == 'none') or (para.STEEL_1(vset['fy']) == 'error2'):
        while True:
            vset['fy'] = input('请输入钢筋强度等级，如HRB400、3：')
            if para.STEEL_1(vset['fy']) != 'error2':
                break

    vset = inputslesct_3(vset,'lamda_steady','none', 1,50,'请输入支座弯矩系数，如20代表1/20·q·L^2：')
    vset = inputslesct_3(vset,'lamda_span', 'none', 1,50,'请输入跨中弯矩系数，如10代表1/10·q·L^2：')
    vset = inputslesct_3(vset,'gamma_c', 'none', 0,50,'请输入混凝土容重,单位KN/m^3：')
    vset = inputslesct_3(vset,'l_1', 'none', 1,5000000,'请输入低端平台水平长度，单位mm：')
    vset = inputslesct_3(vset,'l_2', 'none', 1,5000000,'请输入斜梯板水平长度，单位mm：')
    vset = inputslesct_3(vset,'l_3', 'none', 1,5000000,'请输入高端平台水平长度，单位mm：')
    vset = inputslesct_3(vset,'h', 'none', 1,5000000,'请输入楼梯总高度，单位mm：')
    vset = inputslesct_3(vset,'n', 'none', 2,10000,'请输入楼梯踏步数量，注意是沿高度方向的，等于沿水平方向的踏步数＋1：')
    vset = inputslesct_3(vset, 'b_l', 'none', 1, 1000, '请输入低支座宽度，单位mm：')
    vset = inputslesct_3(vset, 'b_h', 'none', 1, 1000, '请输入高支座宽度，单位mm：')
    vset = inputslesct_3(vset, 'c', 'none', 1, 100, '请输入保护层厚度，单位mm：')
    vset = inputslesct_3(vset, 'as', 'none', 1, 1000, '请输入计算受压区高度时用的初始as，单位mm：')
    vset = inputslesct_3(vset, 'rou_min', 'none', 0.01, 100, '请输入最小配筋率，0.20的意思是0.20%：')
    vset = inputslesct_3(vset, 'gamma_g', 'none', 0.1, 10, '请输入恒荷载分项系数：')
    vset = inputslesct_3(vset, 'gamma_l', 'none', 0.1, 10, '请输入活荷载分项系数：')
    vset = inputslesct_3(vset, 'phi_c', 'none', 0.1, 10, '请输入组合值系数ψc，默认0.7：')
    vset = inputslesct_3(vset, 'phi_q', 'none', 0.1, 10, '请输入准永久值系数ψq，多层住宅0.4，其他0.3：')

    if (vset['b'] != 'none') :
        while True:
            if vset['b'].isdigit() == True:
                if (float(vset['b']) >= 0) and (float(vset['b']) <= 10000.0):
                    break
            elif (len(vset['b'].split('/'))) == 2 and (vset['b'].split('/')[0].isdigit() == True) and (vset['b'].split('/')[1].isdigit() == True) :
                a = float(vset['b'].split('/')[1])
                if ( a >= 1.0 ) and (a <= 50.0):
                    break
            vset['b'] = input('请输入梯板厚度，可填1/27或者120两种格式，分别代表梯板跨度的1/27和120mm：')
    if (vset['b'] == 'none') :
        while True:
            vset['b'] = input('请输入梯板厚度，可填1/27或者120两种格式，分别代表梯板跨度的1/27和120mm：')
            if vset['b'].isdigit() == True:
                if (float(vset['b']) >= 0) and (float(vset['b']) <= 10000.0):
                    break
            elif (len(vset['b'].split('/'))) == 2 and (vset['b'].split('/')[0].isdigit() == True) and (vset['b'].split('/')[1].isdigit() == True) :
                a = float(vset['b'].split('/')[1])
                if ( a >= 1.0 ) and (a <= 50.0):
                    break
    vset = inputslesct_3(vset,'g', 'none', 1,1000000,'请输入恒荷载，一般输入1.5，单位kN/m^2：')
    vset = inputslesct_3(vset,'l', 'none', 1,1000000,'请输入活荷载，一般输入3.5，单位kN/m^2：')

    vset['f_c'] = para.CON_1(vset['con']) #混凝土抗压强度设计值，单位N/mm^2
    vset['f_t'] = para.CON_2(vset['con']) #混凝土抗拉强度设计值，单位N/mm^2
    vset['f_tk'] = para.CON_3(vset['con']) #混凝土抗拉强度标准值，单位N/mm^2
    vset['E_c'] = para.CON_4(vset['con']) #混凝土弹性模量，单位10^4N/mm^2
    vset['fy_1'] = para.STEEL_1(vset['fy']) #钢筋抗拉强度设计值,单位N/mm^2
    vset['E_s'] = para.STEEL_3(vset['fy']) #钢筋弹性模量，单位10^5N/mm^2
    vset['n'] = int(float(vset['n']))# 台阶高度分段数

    vset= strtofloat(vset,['gamma_c','l_1','l_2','l_3','h','g','l','b_l','b_h','c','as','rou_min','gamma_g','gamma_l',
                           'phi_c','phi_q','lamda_steady','lamda_span','rou_min'])
    print(vset)
    vset['b_0']=0.00
    vset['l_0']=min((vset['l_2']+0.5*(vset['b_l']+vset['b_h'])),1.05*vset['l_2']) #计算跨度，单位mm
    if para.is_floatorint(vset['b']) == True:
        vset['b_0'] = float(vset['b']) #板厚，单位mm
    else:
        vset['b']='1/'+str(vset['b'].split('/')[1])
        vset['b_0'] = para.round_up(vset['l_0'],float(vset['b'].split('/')[1])) #板厚，单位mm
    vset['m'] = float(vset['n']-1)  # 楼梯踏步数量，注意是沿水平方向的
    vset['L']= float(vset['l']) / 1000.0 #活荷载，单位N/mm^2
    vset['G']=float(vset['g']) / 1000.0 #恒荷载，单位N/mm^2
    vset['GAMMA_C']= float(vset['gamma_c']) / 1000000.0 # 混凝土容重,单位N/mm^3
    vset['h_s']=vset['h']/vset['n'] #台阶高，单位mm
    vset['b_s']=vset['l_2']/vset['m'] #台阶宽，单位mm
    vset['a']= math.atan(vset['h_s']/vset['b_s']) #倾角，单位弧度
    vset['A'] = vset['a'] * 180.0 / math.pi #倾角，单位°
    vset['h_1'] = vset['b_0'] /math.cos(vset['a']) # 斜楼梯厚度转换为竖直厚度
    vset['T'] =  0.5 * vset['h_s'] +vset['h_1'] # 踏步板平均厚度，单位mm
    vset['g_k20'] = vset['GAMMA_C'] *vset['T'] # 斜梯板自重恒载，单位N/mm^2
    vset['g_k'] = (vset['g_k20'] *vset['l_2'] + vset['GAMMA_C']*vset['b_0']*(vset['l_1']+vset['l_3']))/(vset['l_1']+vset['l_2']+vset['l_3'])+vset['G'] #梯板恒载，单位N/mm^2
    vset['Q']= float(vset['gamma_g']) * vset['g_k'] + float(vset['gamma_l']) * vset['L'] #荷载基本组合值.单位N/mm^2
    vset['Q_q']= vset['g_k'] + vset['phi_q'] *  vset['L']#荷载准永久组合值.单位N/mm^2
    vset['Mmax_steady'] = vset['Q'] * vset['l_0']**2 / (float(vset['lamda_steady']) * 1000.0)#支座弯矩,单位KN*M/延米
    vset['Mmax_span'] =  vset['Q'] * vset['l_0'] ** 2 / (float(vset['lamda_span']) * 1000.0) #跨中弯矩，单位KN*M/延米
    return vset

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    vset={}
    vset['span']='none'
    inputslesct_3(vset,'span','none',1,2,'str1')