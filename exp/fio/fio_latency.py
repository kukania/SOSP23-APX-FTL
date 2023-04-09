import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes 
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import matplotlib as mat
###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 
'''
#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 2
workname_list = ["TPC-C", "TPC-H"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path = "FAST21-RESULT-throughput.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_fio"#분석할 sheet name 입력 
sheet_name = "16_frag_tpcc"
output_path = "" # default: ""
output_name = "TPC_zoom_latency" 
#output_name = "TPCH"
'''
'''
#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 4
workname_list = ["OLTP", "Varmail", "Webproxy", "Webserver"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path = "FAST21-RESULT-throughput.xlsx" #분석위한 xlsx파일 path 입력
sheet_name = "16_frag_filebench" #분석할 sheet name 입력 
#sheet_name = "16_frag_tpch"
output_path = "" # default: ""
output_name = "Filebench_zoom_latency" 
'''
#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 3
workname_list = ["RM", "RR", "SR"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path = "data.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_fio"#분석할 sheet name 입력 
sheet_name = "16_fio_frag"
output_path = "" # default: ""
output_name = "FIO_latency" 
#output_name = "TPCH"

# 0: TPC, 1:Filebench, 2:FIO
wl = 2
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


t = create_startptr("I", workload_num)
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
#font = FontProperties()
#font.set_family('serif')
#font.set_name('Droid Sans')

sub_list = []


#figure size=(16,4) subgraph가 4개이기 때문에 각각 4,4로 크기 맞추기 위해 설정
fig = plt.figure(figsize=(3.3*workload_num+0.4,3))

#font
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rc('font', family='sans-serif') 
plt.rc('font', serif='Helvetica') 

in_list = []
#subplot 생성, 4개, 각 subplot draw object를 sub_list에 넣음
width_list = [1 for i in range(workload_num)]
fig, axs = plt.subplots(1,workload_num,figsize=(3.3*workload_num+0.6, 3),gridspec_kw={'width_ratios': width_list})
plt.subplots_adjust(wspace=0.3)

for i in range(workload_num):
    axins = inset_axes(axs[i], 1,1 , loc=2, bbox_to_anchor=(0.41,0.6), bbox_transform=axs[i].transAxes)
    in_list.append(axins)



sub_list = []
for i in range(len(axs)):
    sub_list.append(axs[i])
print(sub_list)

#각 graph object line의 특성 
#color_list = ['b','r','g','purple', 'dimgray','darkorange', "r"]
color_list = ['brown','dodgerblue', 'darkorange', 'darkgreen', 'purple', 'midnightblue']

shape_list = ['o','x','^','p','s','v']
#shape_list = ["" for i in range(6)]
#sub graph title
title_list = workname_list
tmp_list = []
a = 0
ZTPC_list = [[[1900,2400],[0.95,1]], [[100,500],[0.97,1]]]
ZFB_list = [[[1900,2400],[0.95,1]],[[1700,2200],[0.8,1]],[[1500,2000],[0.95,1]],[[200,700],[0.9,1]]]
ZFIO_list = [[[100,600],[0.90,1]],[[100,400],[0.7,1]],[[90,250],[0.9,1]]]
Z_list = [ZTPC_list, ZFB_list, ZFIO_list]


STPC_list = [[[0,3000],[0,1]], [[0,3000],[0,1]]]
SFB_list = [[[0,3000],[0,1]],[[0,2500],[0,1]],[[0,2500],[0,1]],[[0,2000],[0,1]]]
SFIO_list = [[[0,2000],[0,1]],[[0,800],[0,1]],[[0,800],[0,1]]]
S_list = [STPC_list, SFB_list, SFIO_list]

point_list=[60, 25, 20]
zpoint_list=[16, 16, 10]

for i in range(len(sub_list)):
    for j in range(6):
        tmp2 = sub_list[i].plot(x_list[j+6*i], y_list[j+6*i], linewidth=0.8,color=color_list[j], markerfacecolor="None",marker=shape_list[j], markersize=4.6, markevery=point_list[i])
        tmp3 = in_list[i].plot(x_list[j+6*i], y_list[j+6*i], linewidth=0.8,color=color_list[j], markerfacecolor="None",marker=shape_list[j], markersize=4.6, markevery=zpoint_list[i])
        tmp_list.append(tmp2)
    #sub_list[i].set_aspect('equal')
    #sub_list[i].set(adjustable='box-forced', aspect='equal')
    sub_list[i].tick_params(axis='y',direction='in', right=True, labelsize=14)
    sub_list[i].tick_params(axis='x', labelsize=14)
    
    in_list[i].tick_params(axis='y',direction='in', right=True, labelsize=12)
    in_list[i].tick_params(axis='x', labelsize=12)
    print(Z_list[wl][0])
    in_list[i].set_xlim(Z_list[wl][i][0])
    in_list[i].set_ylim(Z_list[wl][i][1])
    #축 lim 설정 (x,y)
    sub_list[i].set_xlim(S_list[wl][i][0])
    sub_list[i].set_ylim(S_list[wl][i][1])
    sub_list[i].set_xlabel("Time (µs)", fontsize=14)
    
    if i == 0:
        sub_list[i].set_ylabel("CDF", fontsize=14)
    sub_list[i].set_title(title_list[i], fontsize=14, y=-0.24,pad=-14)
fig.legend(tmp_list[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], markerscale=1.5,frameon=False,loc="upper center", bbox_to_anchor=(0.51, 1.07),ncol=6, fontsize=14)
#fig.legend(tmp_list[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], frameon=False,loc="lower right", bbox_to_anchor=(0.91,0.09),ncol=1, fontsize=13)
plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=1000, bbox_inches = "tight")
plt.savefig(output_path+output_name+".png", format='png',dpi=1000,bbox_inches = "tight")
