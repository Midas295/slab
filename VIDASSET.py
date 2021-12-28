# 文件名:VIDASSET.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:本文件用于处理与VIDAS.SET有关的函数

import parameter as para


def vset():
    '''
    :param VI:是否存在VIDAS.SET文件，如果不存在则使用以下默认值。VI=0则不存在，VI=任意数则存在。
    :return: 默认值的参数
    '''
    s ='''#################################################
格式说明：
*参数=参数值 ##注释 

参数值为none时会在程序中有输入选项
参数值不为none且值无误时按此值取值

注意本文件中参数名称和等号全部为英文小写
选筋库只能在SET文件里设置，不提供输入窗口
#################################################
*name=none;                                 ##标题,如果为1则同文件名，其他则同本参数
*project_name_1=工程一;                ##工程名
*project_name_2=项目一;                ##项目名
*lamda_steady=20;                        ##支座弯矩系数，如20代表1/20·q·L^2，限制值在1~50之间
*lamda_span=10;                          ##跨中弯矩系数，如10代表1/10·q·L^2，限制值在1~50之间
*con=C30;                                    ##混凝土强度等级，可取C15~C80间实际存在的标号
*fy=HRB400;                                ##钢筋强度等级，可取HPB300、HRB335、HRB400、HRB500或1、2、3、4
*gamma_c=25;                            ##混凝土容重,单位KN/m^3,0表示不考虑自重，限制在0~50之间
*l_1=none;                                  ##低端平台水平长度，单位mm。限制在0~50000之间
*l_2=none;                                  ##斜梯板水平长度，单位mm。限制在0~50000之间
*l_3=none;                                  ##高端平台水平长度，单位mm。限制在0~50000之间
*h=none;                                    ##楼梯总高度，单位mm。限制在0~50000之间
*n=none;                                    ##楼梯踏步数量，注意是沿高度方向的，等于沿水平方向的踏步数＋1,限制为2~10000之间的整数
*b=none;                                    ##梯板厚度，可填1/27或者120两种格式，分别代表梯板跨度的1/27和120mm。分子只能取1,分母取值在1~50之间的整数。mm值限制在0~10000。
*g=none;                                    ##恒荷载，一般输入1.5，单位kN/m^2。限制大于0。
*l=none;                                     ##活荷载，一般输入3.5，单位kN/m^2。限制大于0
*b_l=200;                                    ##低支座宽度，单位mm。限制在1~1000之间
*b_h=200;                                  ##高支座宽度，单位mm。限制在1~1000之间
*c=15;                                       ##保护层厚度，单位mm。限制在1~1000之间
*as=20;                                     ##计算受压区高度时用的初始as。限制在1~1000之间
*rou_min=0.20;                         ##最小配筋率，0.20的意思是0.20%，限制在0.01~1之间
*gamma_g=1.3;                        ##恒荷载分项系数，限制在0.1~10之间
*gamma_l=1.5;                        ##活荷载分项系数，限制在0.1~10之间
*deflection=on;                        ##计算挠度开关，on或者off，其他值自动转换为on
*fissure=on;                             ##计算裂缝开关，on或者off，其他值自动转换为on
*phi_c=0.7;                              ##组合值系数ψc，默认0.7，限制在0.01~1之间
*phi_q=0.3;                             ##准永久值系数ψq，多层住宅0.4，其他0.3，限制在0.01~1之间
*s=8,10,12,14,16,18;                                                 ## 钢筋直径库，限制实际存在的钢筋直径
*d=100,110,120,130,140,150,160,170,180,190,200;     ## 钢筋间距库，限制在10~800之间的整十数
*r=8@110,10@120;                                                 ## 钢筋补充库，记录直径库和间距库里不存在的配筋，若重复则无效。同上。 
######################################################
    '''
    return s


def strdeal(str1,split1,split2):
    '''
    本模组用于提取文本内容，用split1和split2夹取取str1的文本，注意此处该文本只能存在一个，否则只取第一个
    :param str1: 要处理的字符串
    :param split1: 提取数字前的字符串,若str1不存在此字符串返回：none
    :param split2: 提取数字后的字符串
    :return: 两个字符串之间的字符
    '''
    if split1 == '':
        n = str1.split(str(split2))[0]
    else:
        if str1.find(str(split1)) == -1:
            n = 'none'
        else:
            n= str1.split(str(split1))[1].split(str(split2))[0]
    return n

def vidasset(vset):
    '''
    :param :设置文件vset字符串
    :return: vset字典
    '''
    vidasset = {}
    vidasset['name'] = strdeal(vset, '*name=', ';')
    vidasset['project_name_1'] = strdeal(vset, '*project_name_1=', ';')
    vidasset['project_name_2'] = strdeal(vset, '*project_name_2=', ';')
    vidasset['lamda_steady'] = strdeal(vset, '*lamda_steady=', ';')
    vidasset['lamda_span'] = strdeal(vset, '*lamda_span=', ';')
    vidasset['con'] = strdeal(vset, '*con=', ';')
    vidasset['fy'] = strdeal(vset, '*fy=', ';')
    vidasset['gamma_c'] = strdeal(vset, '*gamma_c=', ';')
    vidasset['l_1'] = strdeal(vset, '*l_1=', ';')
    vidasset['l_2'] = strdeal(vset, '*l_2=', ';')
    vidasset['l_3'] = strdeal(vset, '*l_3=', ';')
    vidasset['h'] = strdeal(vset, '*h=', ';')
    vidasset['n'] = strdeal(vset, '*n=', ';')
    vidasset['b'] = strdeal(vset, '*b=', ';')
    vidasset['g'] = strdeal(vset, '*g=', ';')
    vidasset['l'] = strdeal(vset, '*l=', ';')
    vidasset['b_l'] = strdeal(vset, '*b_l=', ';')
    vidasset['b_h'] = strdeal(vset, '*b_h=', ';')
    vidasset['c'] = strdeal(vset, '*c=', ';')
    vidasset['as'] = strdeal(vset, '*as=', ';')
    vidasset['rou_min'] = strdeal(vset, '*rou_min=', ';')
    vidasset['gamma_g'] = strdeal(vset, '*gamma_g=', ';')
    vidasset['gamma_l'] = strdeal(vset, '*gamma_l=', ';')
    vidasset['deflection'] = strdeal(vset, '*deflection=', ';')
    vidasset['fissure'] = strdeal(vset, '*fissure=', ';')
    vidasset['phi_c'] = strdeal(vset, '*phi_c=', ';')
    vidasset['phi_q'] = strdeal(vset, '*phi_q=', ';')
    vidasset['s'] = strdeal(vset, '*s=', ';')
    vidasset['d'] = strdeal(vset, '*d=', ';')
    vidasset['r'] = strdeal(vset, '*r=', ';')
    return vidasset

def rein_lib(s,d,r):
    '''
    :param s:直径库，用逗号隔开 ，如：8,10,12,14,16
    :param d: 间距库，用逗号隔开，如：100,110,120,140
    :param r: 补充库，直径@间距，用逗号隔开，如：8@100,10@100
    :return:
    '''
    lib = {}
    s = s.split(',')
    d = d.split(',')
    r = r.split(',')
    for i in range(0,len(s)):
        for j in range(0,len(d)):
            lib[s[i]+'@'+d[j]] = round(para.Area_2(s[i],d[j]),1)
    for k in range(0,len(r)):
        dk = r[k].split('@')
        lib[r[k]] = round(para.Area_2(dk[0],dk[1]),1)
    return lib

def rein_select(A_s,lib):
    '''
    :param A_s:需要的钢筋
    :param lib: 选筋库字典
    :return: 选择的钢筋文本
    '''
    STR = str(A_s)+'选筋库无此配筋，修改配筋库'
    lib_new=sorted(lib.items(), key=lambda kv: (kv[1], kv[0])) #对字典进行排序
    for i in lib_new:
        if i[1] >= A_s:
            STR = i[0]
            break
    return STR

dic=('''
字典対如下：
vset['name']=标题，格式str
vset['project_name_1']=工程名，格式str
vset['project_name_2']=项目名，格式str
vset['con']=输入的混凝土强度，需要转格式
vset['CON']=转格式之后的混凝土强度 #待处理
vset['fy']=输入的钢筋强度等级，需要转格式
vset['FY']=转格式之后的钢筋强度等级 #待处理
vset['lamda_steady']=输入的支座弯矩系数
vset['lamda_span']=输入的跨中弯矩系数
vset['gamma_c']=输入的混凝土容重,单位KN/m^3
vset['GAMMA_C']=转格式的混凝土容重,单位N/mm^3=vset['gamma_c']/1000000
vset['l_1']=输入低端平台水平长度，单位mm
vset['l_2']=输入斜梯板水平长度，单位mm
vset['l_3']=输入高端平台水平长度，单位mm
vset['h']=输入楼梯总高度，单位mm
vset['n']=输入楼梯踏步数量，注意是沿高度方向的，等于沿水平方向的踏步数＋1
vset['m']=输入楼梯踏步数量，注意是沿水平方向的
vset['b']=输入的板厚，1/27或者120两种格式
vset['b_0']=实际板厚取值，单位mm
vset['g']=输入恒荷载，一般输入1.5，单位kN/m^2
vset['G']=恒荷载，单位N/mm^2=vset['g']/1000
vset['l']=输入活荷载，一般输入3.5，单位kN/m^2
vset['L']=活荷载，单位N/mm^2=vset['l']/1000
vset['b_l']=请输入低支座宽度，单位mm
vset['b_h']=请输入高支座宽度，单位mm
vset['c']=保护层厚度，单位mm
vset['as']=请输入计算受压区高度时用的初始as，单位mm
vset['rou_min']=最小配筋率，0.20的意思是0.20%
vset['gamma_g']=恒荷载分项系数
vset['gamma_l']=活荷载分项系数
vset['phi_c']=组合值系数ψc
vset['phi_q']=准永久值系数ψq
vset['f_c']=混凝土抗压强度设计值，单位N/mm^2
vset['f_t']=混凝土抗拉强度设计值，单位N/mm^2
vset['f_tk']=混凝土抗拉强度标准值，单位N/mm^2
vset['E_c']=混凝土弹性模量，单位10^4N/mm^2
vset['fy_1']=钢筋抗拉强度设计值,单位N/mm^2
vset['E_s']=钢筋弹性模量，单位10^5N/mm^2
vset['l_0']=计算跨度，单位mm
vset['b_0']=板厚，单位mm
vset['h_s']=台阶高，单位mm
vset['b_s']=台阶宽，单位mm
vset['a']=倾角，单位弧度
vset['A']=倾角，单位°
vset['h_1']=板竖直厚度，单位mm
vset['T']=踏步板平均厚度，单位mm
vset['g_k20']=斜梯板自重恒载，单位N/mm^2
vset['g_k']=梯板恒载，单位N/mm^2
vset['Q']=荷载基本组合值.单位N/mm^2
vset['Q_q']=荷载准永久.单位N/mm^2
vset['Mmax_steady']=支座弯矩,单位KN*M/延米
vset['Mmax_span']=跨中弯矩，单位KN*M/延米
vset['h_0']=板有效高度，单位mm
vset['ASb_steady']=支座ASb
vset['x_steady']=支座截面受压高度，单位mm
vset['S_steady']=支座配筋面积，单位mm^2
vset['ASb_span']=跨中ASb
vset['x_span']=跨中截面受压高度，单位mm
vset['S_pan']=跨中配筋面积，单位mm^2
''')








if __name__ == '__main__':
    # print(vidasset(vset(True)))
    # print(rein_lib(vidasset(vset(True))['s'],vidasset(vset(True))['d'],vidasset(vset(True))['r']))
    lib=rein_lib(vidasset(vset())['s'], vidasset(vset())['d'], vidasset(vset())['r'])
    print(rein_select(334.9,lib))

