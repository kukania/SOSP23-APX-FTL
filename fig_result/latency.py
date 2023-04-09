import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes 
from matplotlib.font_manager import FontProperties


###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 3
workname_list = ["oltp","varmail","webproxy"]
 #반드시 workname_list elem 개수와 workload num이 일치해야함. 
result_path = "16_frag_high_default.xlsx" #분석위한 xlsx파일 path 입력
sheet_name = "16_frag_high_default" #분석할 sheet name 입력 
output_path = "" # default: ""
output_name = "a" 

def convert_startptr(start_ptr):
    start_int = 0
    for i in range(len(start_ptr)):
        if i == 0:
            start_int += ((ord(start_ptr[-1-i])-65)%26)
        elif i == 1:
            start_int += (i*26)*(int((ord(start_ptr[-1-i])-65)%26)+1)
    return start_int

def extract_xy(start_ptr, idx, path, sheet_name):
    start_int = convert_startptr(start_ptr)
    df_from_excel = pd.read_excel(path,
                              sheet_name = sheet_name,
                              header = 2,
                              usecols=[start_int,start_int+2]
                             )
    if idx != "0":
        x = np.array(df_from_excel["latency."+idx])
        y = np.array(df_from_excel['CDF.'+idx])
        #print(x[-1], x[0])
    else:
        x = np.array(df_from_excel["latency"])
        y = np.array(df_from_excel['CDF'])        
    index = np.where(y == 1)[0][0]
    x = x[:index+1]
    y = y[:index+1]
    return x,y

def create_startptr(st_point, workload_num):
    tmp = []
    for i in range(workload_num*6):
        num = ord(st_point[-1])+i*3
        if num - 90 > 0:
            if len(st_point) == 1:
                two_num = 65 + int((num - 90) / 26)
                num = (num - 90) % 26 + 64 
                one = chr(num)
                two = chr(two_num)
                tmp.append(two+one)
            else:
                two_num = ord(st_point[0]) +1
                num = num + 64 - 90
                one = chr(num)
                two = chr(two_num)
                tmp.append(two+one)
        else:
            if len(st_point) == 1:
                tmp.append(chr(num))
            else:
                tmp.append(st_point[0]+chr(num))
    return tmp


t = create_startptr("H", workload_num)
#CA로 넘어가게 되면 버그가 있는데, 임의로 값을 변경해주면 해결됨. 
#print(t)
#t값 확인 후 뭔가 이상하면 t[i] = ... 이런식으로 변경해주시면 됩니다.  
#i.e., t[-1] = "CA"
#이부분이 잘되야 데이터를 올바르게 뽑을 수 있어용 

x_list = []
y_list = []
for i in range(len(t)):
    x,y = extract_xy(t[i], str(i), result_path, sheet_name)
    x_list.append(x)
    y_list.append(y)

#일단 넣어놓은 코드 
font = FontProperties()
font.set_family('serif')
font.set_name('Droid Sans')

sub_list = []


#figure size=(16,4) subgraph가 4개이기 때문에 각각 4,4로 크기 맞추기 위해 설정
fig = plt.figure(figsize=(workload_num*4,workload_num))

#font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

#subplot 생성, 4개, 각 subplot draw object를 sub_list에 넣음
width_list = [1 for i in range(workload_num)]
fig, axs = plt.subplots(1,workload_num,figsize=(3*workload_num+0.5,3),gridspec_kw={'width_ratios': width_list})
sub_list = []
for i in range(len(axs)):
    sub_list.append(axs[i])
print(sub_list)

#각 graph object line의 특성 
color_list = ['r','b','g','purple', 'darkorange','dimgray', "r"]
shape_list = ['o','x','^','p','s','v']

#sub graph title
title_list = workname_list
tmp_list = []


for i in range(len(sub_list)):
    for j in range(6):
        tmp2 = sub_list[i].plot(x_list[j+6*i], y_list[j+6*i], linewidth=0.8,color=color_list[j], markerfacecolor="None",marker=shape_list[j], markevery=70)
        tmp_list.append(tmp2)
    sub_list[i].tick_params(axis='y',direction='in', right=True)
    #축 lim 설정 (x,y)
    sub_list[i].set_ylim([0.85,1])
    sub_list[i].set_xlim([0,3000])
    sub_list[i].set_xlabel("Time (ms)", fontsize=15, fontproperties=font)
    
    if i == 0:
        sub_list[i].set_ylabel("CDF", fontsize=15, fontproperties=font)
    sub_list[i].set_title(title_list[i], fontsize=15, y=-0.25,pad=-14)
fig.legend(tmp_list[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], frameon=False,loc="upper center", bbox_to_anchor=(0.51, 1.05),ncol=6, fontsize=13)

plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=1500, bbox_inches = "tight")
plt.savefig(output_path+output_name+".png", format='png',bbox_inches = "tight")
