# 文件名:inputset.py
# 作者:Midas
# 版本:v1.0.0
# 时间:2021－12－15
# 文件作用:本文件用于输出计算书文本

import os

def namefind():

    '''
    :return: 返回一个列表，其值是SET文件的全名
    '''

    q=os.path.abspath('VIDAS.SET')
    s = q.split('\\VIDAS.SET')[0]
    Files =os.listdir(s)
    Files1={}
    Files2={}
    Files3={}
    F=[]
    for k in range(len(Files)):
        Files1[k] = os.path.splitext(Files[k])[0]
        # print(Files1[k])
        Files2[k] = os.path.splitext(Files[k])[1]
        if (Files2[k] =='.SET') and (Files1[k] != 'VIDAS'):
               Files3[k]=Files[k]
    for value in Files3.values():
        F.append(value)

    return F

def write(name,namefix,str0,prefix,suffix):
    '''
    :param name: 文件名
    :param namefix: 删去后缀
    :param str0: 写入内容
    :param prefix: 前缀
    :param suffix: 后缀
    :return: 自动生成并覆盖文件
    '''
    name1=str(prefix)+name.split(namefix)[0]+str(suffix)
    f = open(name1, 'w')
    f.write(str(str0))
    f.close()



def single(vset):
    '''

    :param vset:
    :return:
    '''


if __name__ == '__main__':
    print(namefind())
    str1=('''# 楼梯计算程序范例

## 1 基本资料

工程名称：工程一

工程项目：项目一

楼梯编号：板式楼梯

是否考虑人防荷载：否

支座类型：两端弹性

跨中弯矩系数：1/10

支座弯矩系数: 1/20

混凝土强度等级：C30

混凝土抗压强度设计值$f_\\mathrm{c}$：14.3  $\\mathrm{N} / \\mathrm{mm}^{2}$

混凝土抗拉强度设计值$f_\\mathrm{t}$：1.43  $\\mathrm{N} / \\mathrm{mm}^{2}$

混凝土抗拉强度标准值$f_\\mathrm{tk}$：2.01  $\\mathrm{N} / \\mathrm{mm}^{2}$

混凝土弹性模量$E_\\mathrm{c}$：3.00  $\\times 10^4 \\mathrm{N} / \\mathrm{mm}^{2}$

混凝土容重$\\gamma_c$ : 25   $\\mathrm{kN} / \\mathrm{m}^{3}$

钢筋强度等级：HRB400

钢筋抗拉强度设计值$f_\\mathrm{y}$：360   $\\mathrm{N} / \\mathrm{mm}^{2}$

钢筋弹性模量$E_\\mathrm{s}$：3.00  $\\times 10^5 \\mathrm{N} / \\mathrm{mm}^{2}$

低标高段水平梯板长度(0代表无此段)$L_\\mathrm{l}$：520  $\\mathrm{mm}$

斜梯板水平长度$L_\\mathrm{s}$：2240  $\\mathrm{mm}$

高标高段水平梯板长度(0代表无此段)$L_\\mathrm{h}$：520  $\\mathrm{mm}$

判断梯板类型：D型

斜梯板竖直高度H：1500 $\\mathrm{mm}$

踏步竖直分段数n：9 段

踏步高$h_\\mathrm{s}=\\mathrm{H/n}$：166.7 $\\mathrm{mm}$

踏步宽$b_\\mathrm{s}=L_\\mathrm{s}/(\\mathrm{n-1})$：280.0 $\\mathrm{mm}$

低标高支座梁宽度$b_l$：200  $\\mathrm{mm}$

高标高支座梁宽度$b_h$：200  $\\mathrm{mm}$

梯板跨度$L_n=L_\\mathrm{l}+L_\\mathrm{s}+L_\\mathrm{h}=520+2240+520=3280\\mathrm{mm}$

计算跨度$L_0=\\mathrm{min}( {\\mathrm{L}_{\\mathrm{n}}+0.5\\left(\\mathrm{~d}_{1}+\\mathrm{d}_{\\mathrm{h}}\\right), 1.05 \\mathrm{~L}_{\\mathrm{n}}})=\\mathrm{min}(3480,3444)=3444 \\mathrm{mm} $

梯板厚度$t=1/27 * L_0=3444/27=143.5 \\mathrm{mm} $，实际取$150\\mathrm{mm}$ 

保护层厚度$c$：15   $\\mathrm{mm}$

板底到钢筋合力点距离$a_s$: 20  $\\mathrm{mm}$

恒荷载分项系数$\\gamma_G$：1.3

活荷载分项系数$\\gamma_Q$：1.5

组合值分项系数$\\psi_\\mathrm{c}$：0.7

准永久值分项系数$\\psi_\\mathrm{c}$：0.3

计算梯板自重：是

板面恒荷载G：1.5 $\\mathrm{kN} / \\mathrm{m}^{2}$

板面活荷载L：3.5  $\\mathrm{kN} / \\mathrm{m}^{2}$

## 2 梯段荷载计算

踏步倾角$\\alpha=\\arctan(h_\\mathrm{s}/b_\\mathrm{s})=\\arctan(166.7/ 280.0)=30.7^{\\circ}$

踏步斜板的长度$L_\\mathrm{x}=L_\\mathrm{s}/ \\cos \\alpha = 2240/\\cos 30.7^{\\circ}=2605.1 \\mathrm{mm}$

踏步段的平均厚度$T=0.5 h_{\\mathrm{s}}+\\mathrm{t}/\\cos \\alpha=0.5*166.7+150/\\cos30.7^{\\circ}=257.8\\mathrm{mm}$

梯板的有效高度$h_{0}=t-a_s=150-20=130\\mathrm{mm}$

踏步板的均布恒荷载$G_\\mathrm{k}=\\gamma_c *(T*L_\\mathrm{s}+t*L_\\mathrm{l}+t*L_\\mathrm{h})/L_\\mathrm{n} + G=25/1000*(257.8*2240+150*520+150*520)/3280 +1.5=7.09\\mathrm{kN} / \\mathrm{m}^{2}$

均布荷载的组合值$Q=\\gamma_G \\cdot G_k +\\gamma_L \\cdot L=1.3*7.09+1.5*3.5=14.5\\mathrm{kN} / \\mathrm{m}^{2}$



# 3 正截面承载力计算

跨中 $M_{st}=1 / 10 \\cdot Q \\cdot L_{0}^{2}=0.1 * 14.5 * 3.444^{2}=17.2 \\mathrm{kN} \\cdot \\mathrm{m}$

$\\mathrm{A}_{\\mathrm{s}}=375 \\mathrm{~mm}^{2}$, 相对受压区高度 $\\xi=0.1561$, 配筋率 $\\rho=0.518 \\%$

实配纵筋: $10 @ 140 \\quad\\left(\\mathrm{~A}_{\\mathrm{s}}=393\\right)$; 

支座 $M_{sp}=1 / 20 \\cdot Q \\cdot L_{0}^{2}=0.05 * 14.5 * 3.444^{2}=8.6 \\mathrm{kN} \\cdot \\mathrm{m}$

$\\mathrm{A}_{\\mathrm{s}}=389 \\mathrm{~mm}^{2}$, 相对受压区高度 $\\xi=0.1561$, 配筋率 $\\rho=0.518 \\%$

实配纵筋: $10 @ 200 \\quad\\left(\\mathrm{~A}_{\\mathrm{s}}=393\\right)$; 

# 4 跨中裂缝验算

跨中实配钢筋$\\mathrm{A}_{\\mathrm{s}}=375 \\mathrm{~mm}^{2}$

# 5 支座裂缝验算

# 6 挠度验算

# 7 平法表示








''')



    for i in range(len(namefind())):
        write(namefind()[i],'.SET',str1,i,'.md')