# �ļ���:single.py
# ����:Midas
# �汾:v1.0.0
# ʱ��:2021��12��15
# �ļ�����:����һ����ͼ

import parameter as para

dic=('''
�ֵ䌝���£�
vset['name']=���⣬��ʽstr
vset['project_name_1']=����������ʽstr
vset['project_name_2']=��Ŀ������ʽstr
vset['con']=����Ļ�����ǿ�ȣ���Ҫת��ʽ
vset['CON']=ת��ʽ֮��Ļ�����ǿ�� #������
vset['fy']=����ĸֽ�ǿ�ȵȼ�����Ҫת��ʽ
vset['FY']=ת��ʽ֮��ĸֽ�ǿ�ȵȼ� #������
vset['lamda_steady']=�����֧�����ϵ��
vset['lamda_span']=����Ŀ������ϵ��
vset['gamma_c']=����Ļ���������,��λKN/m^3
vset['GAMMA_C']=ת��ʽ�Ļ���������,��λN/mm^3=vset['gamma_c']/1000000
vset['l_1']=����Ͷ�ƽ̨ˮƽ���ȣ���λmm
vset['l_2']=����б�ݰ�ˮƽ���ȣ���λmm
vset['l_3']=����߶�ƽ̨ˮƽ���ȣ���λmm
vset['l_n']=�ݰ���=l_1+l_2+l_3����λmm
vset['h']=����¥���ܸ߶ȣ���λmm
vset['n']=����¥��̤��������ע�����ظ߶ȷ���ģ�������ˮƽ�����̤������1
vset['m']=����¥��̤��������ע������ˮƽ�����
vset['b']=����İ��1/27����120���ָ�ʽ
vset['b_0']=ʵ�ʰ��ȡֵ����λmm
vset['g']=�������أ�һ������1.5����λkN/m^2
vset['G']=����أ���λN/mm^2=vset['g']/1000
vset['l']=�������أ�һ������3.5����λkN/m^2
vset['L']=����أ���λN/mm^2=vset['l']/1000
vset['b_l']=�������֧�����ȣ���λmm
vset['b_h']=�������֧�����ȣ���λmm
vset['c']=�������ȣ���λmm
vset['as']=�����������ѹ���߶�ʱ�õĳ�ʼas����λmm
vset['rou_min']=��С����ʣ�0.20����˼��0.20%
vset['gamma_g']=����ط���ϵ��
vset['gamma_l']=����ط���ϵ��
vset['phi_c']=���ֵϵ����c
vset['phi_q']=׼����ֵϵ����q
vset['f_c']=��������ѹǿ�����ֵ����λN/mm^2
vset['f_t']=����������ǿ�����ֵ����λN/mm^2
vset['f_tk']=����������ǿ�ȱ�׼ֵ����λN/mm^2
vset['E_c']=����������ģ������λ10^4N/mm^2
vset['fy_1']=�ֽ��ǿ�����ֵ,��λN/mm^2
vset['E_s']=�ֽ��ģ������λ10^5N/mm^2
vset['l_0']=�����ȣ���λmm
vset['b_0']=��񣬵�λmm
vset['h_s']=̨�׸ߣ���λmm
vset['b_s']=̨�׿�����λmm
vset['a']=��ǣ���λ����
vset['A']=��ǣ���λ��
vset['h_1']=����ֱ��ȣ���λmm
vset['T']=̤����ƽ����ȣ���λmm
vset['g_k20']=б�ݰ����غ��أ���λN/mm^2
vset['g_k']=�ݰ���أ���λN/mm^2
vset['Q']=���ػ������ֵ.��λN/mm^2
vset['Q_q']=����׼����.��λN/mm^2
vset['Mmax_steady']=֧�����,��λKN*M/����
vset['Mmax_span']=������أ���λKN*M/����
vset['h_0']=����Ч�߶ȣ���λmm
vset['ASb_steady']=֧��ASb
vset['x_steady']=֧��������ѹ�߶ȣ���λmm
vset['S_steady']=֧������������λmm^2
vset['ASb_span']=����ASb
vset['x_span']=���н�����ѹ�߶ȣ���λmm
vset['S_pan']=��������������λmm^2
''')

# �������

## 1.��������
vset=[]
vset['name']='����ز�'#���⣬��ʽstr
vset['project_name_1']='3#'#����������ʽstr
vset['project_name_2']='LT1'#��Ŀ������ʽstr
vset['lamda_steady']=20  #�����֧�����ϵ��
vset['lamda_span']=20  #����Ŀ������ϵ��
vset['l_1']=100   #����Ͷ�ƽ̨ˮƽ���ȣ���λmm
vset['l_2']=2300  #����б�ݰ�ˮƽ���ȣ���λmm
vset['l_3']=100   #����߶�ƽ̨ˮƽ���ȣ���λmm
vset['l_n']=vset['l_1']+vset['l_2']+vset['l_3'] #�ݰ���=l_1+l_2+l_3����λmm
vset['b_l']=200   #�������֧�����ȣ���λmm
vset['b_h']=200   #�������֧�����ȣ���λmm
vset['l_01']=vset['l_n']+0.5*(vset['b_l']+vset['b_n']) #�������м�ֵ1
vset['l_02']=1.05*vset['l_n'] # �������м�ֵ2
vset['l_0']=min(vset['l_01'],vset['l_02']) #�����ȣ���λmm
vset['b']= 'L/27' #����İ��1/27����120���ָ�ʽ

vset['b_0'] = 0.00
if para.is_floatorint(vset['b']) == True:
    vset['b_0'] = float(vset['b'])  # ��񣬵�λmm
else:
    vset['b1'] = '1/' + str(vset['b'].split('/')[1]) # �����м�ֵ�����ٷ�֮һ
    vset['b_0'] = para.round_up(vset['l_0'], float(vset['b1'].split('/')[1]))  # ��񣬵�λmm

vset['h']=1450 #����¥���ܸ߶ȣ���λmm
vset['n']=9 #����¥��̤��������ע�����ظ߶ȷ���ģ�������ˮƽ�����̤������1
vset['m']=8 #����¥��̤��������ע������ˮƽ�����
vset['P_k']=1 #���Ժ���ر�׼ֵ����λkN/m
vset['q_k']=3.5 #¥�ݾ�������ر�׼ֵ����λkN/m^2
vset['phi_c']=0.7 #���ֵϵ����c
vset['phi_q']=0.3 #׼����ֵϵ����q
vset['c_1']=25 #����ȣ���λmm
vset['gamma_1']= 20 #�������KN/m^3
vset['c_1']=20 #�����ȣ���λmm
vset['gamma_1']= 18 #��������KN/m^3
vset['gamma_c']=25#����Ļ���������,��λKN/m^3
vset['con']='C30'#����Ļ�����ǿ�ȣ���Ҫת��ʽ
vset['steel']='HRB400'#����ĸֽ�ǿ�ȵȼ�����Ҫת��ʽ
vset['f_c']=para.fc(vset['con'])#��������ѹǿ�����ֵ����λN/mm^2
vset['f_t']=para.ft(vset['con'])#����������ǿ�����ֵ����λN/mm^2
vset['f_tk']=para.ftk(vset['con'])#����������ǿ�ȱ�׼ֵ����λN/mm^2
vset['E_c']=para.Ec(vset['con'])#����������ģ������λ10^4N/mm^2
vset['fy_1']=para.fy(vset['steel'])#�ֽ��ǿ�����ֵ,��λN/mm^2
vset['E_s']=para.Es(vset['steel'])#�ֽ��ģ������λ10^5N/mm^2
vset['c']=20 # �������ȣ���λmm


## 2.¥�ݼ��β���





## 3.�������ú��ر�׼ֵ

## 4.�������صĻ������ֵ


## 5.�ݰ�֧������

## 6.�ݰ�б�����ܼ�����������

## 7.�������������������

## 8.�����Ӷ�����

## 9.�ѷ�����

## 10.���������

# �������ͼ�����