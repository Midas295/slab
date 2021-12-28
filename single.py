# 文件名:single.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:先做一个草图

import parameter as para

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
vset['l_n']=梯板跨度=l_1+l_2+l_3，单位mm
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

# 输入参数

## 1.基本资料
vset=[]
vset['name']='嘉宇地产'#标题，格式str
vset['project_name_1']='3#'#工程名，格式str
vset['project_name_2']='LT1'#项目名，格式str
vset['lamda_steady']=20  #输入的支座弯矩系数
vset['lamda_span']=20  #输入的跨中弯矩系数
vset['l_1']=100   #输入低端平台水平长度，单位mm
vset['l_2']=2300  #输入斜梯板水平长度，单位mm
vset['l_3']=100   #输入高端平台水平长度，单位mm
vset['l_n']=vset['l_1']+vset['l_2']+vset['l_3'] #梯板跨度=l_1+l_2+l_3，单位mm
vset['b_l']=200   #请输入低支座宽度，单位mm
vset['b_h']=200   #请输入高支座宽度，单位mm
vset['l_01']=vset['l_n']+0.5*(vset['b_l']+vset['b_n']) #计算跨度中间值1
vset['l_02']=1.05*vset['l_n'] # 计算跨度中间值2
vset['l_0']=min(vset['l_01'],vset['l_02']) #计算跨度，单位mm
vset['b']= 'L/27' #输入的板厚，1/27或者120两种格式

vset['b_0'] = 0.00
if para.is_floatorint(vset['b']) == True:
    vset['b_0'] = float(vset['b'])  # 板厚，单位mm
else:
    vset['b1'] = '1/' + str(vset['b'].split('/')[1]) # 板厚的中间值，多少分之一
    vset['b_0'] = para.round_up(vset['l_0'], float(vset['b1'].split('/')[1]))  # 板厚，单位mm

vset['h']=1450 #输入楼梯总高度，单位mm
vset['n']=9 #输入楼梯踏步数量，注意是沿高度方向的，等于沿水平方向的踏步数＋1
vset['m']=8 #输入楼梯踏步数量，注意是沿水平方向的
vset['P_k']=1 #线性恒荷载标准值，单位kN/m
vset['q_k']=3.5 #楼梯均布活荷载标准值，单位kN/m^2
vset['phi_c']=0.7 #组合值系数ψc
vset['phi_q']=0.3 #准永久值系数ψq
vset['c_1']=25 #面层厚度，单位mm
vset['gamma_1']= 20 #面层容重KN/m^3
vset['c_1']=20 #顶棚厚度，单位mm
vset['gamma_1']= 18 #顶棚容重KN/m^3
vset['gamma_c']=25#输入的混凝土容重,单位KN/m^3
vset['con']='C30'#输入的混凝土强度，需要转格式
vset['steel']='HRB400'#输入的钢筋强度等级，需要转格式
vset['f_c']=para.fc(vset['con'])#混凝土抗压强度设计值，单位N/mm^2
vset['f_t']=para.ft(vset['con'])#混凝土抗拉强度设计值，单位N/mm^2
vset['f_tk']=para.ftk(vset['con'])#混凝土抗拉强度标准值，单位N/mm^2
vset['E_c']=para.Ec(vset['con'])#混凝土弹性模量，单位10^4N/mm^2
vset['fy_1']=para.fy(vset['steel'])#钢筋抗拉强度设计值,单位N/mm^2
vset['E_s']=para.Es(vset['steel'])#钢筋弹性模量，单位10^5N/mm^2
vset['c']=20 # 保护层厚度，单位mm


## 2.楼梯几何参数





## 3.均布永久荷载标准值

## 4.均布荷载的基本组合值


## 5.梯板支座反力

## 6.梯板斜截面受剪承载力计算

## 7.正截面受弯承载力计算

## 8.跨中挠度验算

## 9.裂缝验算

## 10.整体计算结果

# 输出结果和计算书