# 文件名:calc.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:由已知条件计算配筋、挠度、裂缝结果。



import parameter as para

def calcslab_1(vset):
    '''
    :param vset:计算字典
    :return: 输出配筋结果
    '''
    b =  1000.0 #计算单位延米
    vset['h_0'] =vset['b_0']-vset['as'] #板有效高度，单位mm
    vset['ASb_steady'] = (vset['Mmax_steady'] * 1000000) / (1.0 * vset['f_c'] * b * (vset['h_0'] ** 2))
    if vset['ASb_steady'] <= 0.500:
        vset['x_steady'] = (1 - (1 - 2 * vset['ASb_steady']) ** (1 / 2)) * vset['h_0']
        S_1 = (1.0 * vset['f_c'] * b * vset['x_steady']) / vset['fy_1']
        S_2 = vset['rou_min']/ 100.0 * vset['h_0'] * b
        vset['S_steady'] = max(S_1, S_2)
    else:
        vset['S_steady'] ='error3'
    vset['ASb_span'] = (vset['Mmax_span'] * 1000000) / (1.0 * vset['f_c'] * b * (vset['h_0'] ** 2))
    if vset['ASb_span'] <= 0.500:
        vset['x_span'] = (1 - (1 - 2 * vset['ASb_span']) ** (1 / 2)) * vset['h_0']
        S_1 = (1.0 * vset['f_c'] * b * vset['x_span']) / vset['fy_1']
        S_2 = vset['rou_min']/ 100.0 * vset['h_0'] * b
        vset['S_span'] = max(S_1, S_2)
    else:
        vset['S_span'] ='error3'
    return vset

def calcslab_2(vset):

    '''
    :param vset: 计算字典
    :return: 输出承载力结果
    '''

    b = 1000.0 #计算单位延米
    h = float(vset['h_b'])#板厚，单位mm
    as_1 = float(vset['as']) # 计算受压区高度用的as，单位mm
    CON = vset['con'] # 混凝土强度等级
    HRB = vset['fy'] # 钢筋强度等级
    as_2 = float(vset['A_S']) * 100.0 # 配筋面积
    kexi = para.STEEL_1(HRB) * as_2 /(para.CON(CON) * b * (h - as_1)) #相对受压区高度
    if kexi >= 0.5: #暂时用0.5限制受压区高度，后面再更新
        kexi_2 = 0.5
    else:
        kexi_2 = kexi
    gamma = 1-0.5 * kexi_2 # 力臂系数
    L = float(vset['L0']) * 1000.0 # 计算跨度
    n_1 = float(vset['lamda_steady']) #支座弯矩系数
    n_2 = float(vset['lamda_span'])  # 跨中弯矩系数
    M = round(para.STEEL_1(HRB) * as_2 * gamma * (h-as_1) /1000000,t)
    q_steady = round(n_1 * M / ((L/1000)**2),2)
    q_span = round(n_2 * M / ((L/1000)**2),2)
    return [q_steady,q_span]

def calcw(vset):
    '''
    :param vset: 计算字典
    :return: 挠度计算值
    '''
    A_s = float(vset['A_s'])      # 受拉钢筋实配面积
    l_0 = float(vset['l_0'])      #跨度
    d_eq = float(vset['d_eq'])    #受拉钢筋等效直径
    c_s = float(vset['c'])        #受拉钢筋保护层厚度
    f_tk = float(vset['f_tk'])    #混凝土轴心抗拉强度标准值
    Es = float(vset['Es'])        #钢筋弹性模量
    Ec = float(vset['Ec'])
    h = float([vset['h']])        #板厚
    h_0 = h - c_s - d_eq/2        #截面有效高度
    rou_te= A_s / (0.5*1000.0*h)  #按有效受拉混凝土截面面积计算的纵向受拉钢筋配筋率
    Mq = float([vset['M']])       #弯矩值
    sigama_sq = Mq/(0.87*h_0*A_s) #σsq
    phi=1.1-0.65*f_tk/(rou_te*sigama_sq)
    alpha_E = Es/Ec
    rou = A_s /(1000.0*h_0)
    h_01 =float(vset['h_01']) # 考虑踏步刚度后的h_0
    gamma_f1 = 0
    Bs= Es *A_s * h_01^2 /(1.15*phi +0.2 +6*alpha_E*rou /(1+3.5*gamma_f1))
    theta =2.0
    B = Bs /theta
    l = 5 / 48 * Mq*l_0^2 /B
    return l

def calcl(vset):
    '''
    :param vset:计算字典
    :return: 裂缝计算值
    '''
    A_s = float(vset['A_s'])      # 受拉钢筋实配面积
    d_eq = float(vset['d_eq'])    #受拉钢筋等效直径
    c_s = float(vset['c'])        #受拉钢筋保护层厚度
    f_tk = float(vset['f_tk'])    #混凝土轴心抗拉强度标准值
    Es = float(vset['Es'])        #钢筋弹性模量
    h = float([vset['h']])        #板厚
    h_0 = h - c_s - d_eq/2        #截面有效高度
    rou_te= A_s / (0.5*1000.0*h)  #按有效受拉混凝土截面面积计算的纵向受拉钢筋配筋率
    Mq = float([vset['M']])       #弯矩值
    sigama_sq = Mq/(0.87*h_0*A_s) #σsq
    phi=1.1-0.65*f_tk/(rou_te*sigama_sq)
    if c_s <=20.0:
        c_s = 20.0
    elif c_s >=60.0:
        c_s = 60
    alpha_cr =1.9
    Lm = 1.9 * c_s +0.08 * d_eq/rou_te
    w = alpha_cr  * phi *sigama_sq * Lm / Es

    return w