
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 1
#workname_list = ["OLTP", "Varmail", "Webproxy", "Webserver"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
workname_list = ["TPC-H"]
result_path = "data.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_frag_gamma" #분석할 sheet name 입력 
sheet_name = "tpc_throughput"
output_path = "" # default: ""
#output_name = "Filebench_GAMMA" 
output_name = "TPC_throughput"

# extract_throughput: 엑셀을 읽어들여 Throughput 결과 출력 
def extract_throughput(workload_num, path, sheet_name, start_col, flag):
    use_col = [start_col for i in range(workload_num)]
    df = pd.read_excel(path, #file path
                              sheet_name = sheet_name, #sheet name
                              header = 0, #0번째 row를 header로
                              usecols=use_col, #해당 col만 데이터로 사용하겠다.
                               nrows=6 #6개의 row만 읽는다.
                             )
    df_trp = df.transpose() #ploting을 위한 변환
    if flag != 1:
        df_trp = df_trp/1000
    th_list = []
    name_list = ["A","B","C","D","E","F"]
    df_trp.columns = name_list
    for i in range(6):
        th_list.append(np.array(df_trp[name_list[i]]))
        
    print(th_list)
    return th_list

# th_list: throughput list     
th_list = []
flag = 0
for i in range(4):
    
    if i == 1:
        flag = 1
        th_list.append(extract_throughput(workload_num, result_path, sheet_name, i*3+1, flag))
        flag = 0
    else:
        th_list.append(extract_throughput(workload_num, result_path, sheet_name, i*3+1, flag))

#font 설정, 주석 처리하면 기본 글씨체 사용 (해당 부분은 time new roman을 사용하기 위한 것)
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rc('font', family='sans-serif') 
plt.rc('font', serif='Helvetica') 

width_list=[1,1]
#figure 사이즈 변경하고 싶을 때 사용, figsize = (a,b)에서 a가 더 커야 이쁨
plt.figure(figsize=(13,3))
fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(8,3),gridspec_kw={'width_ratios': width_list})
print(len(axs))

title_list = ["TPC-C", "TPC-H"]
for i in range(len(axs)):
    if i == 0:
        xx=0.61
    elif i == 1:
        xx=0.38
    axs[i].set_title(title_list[i], fontsize=16, x=xx, y=-0.13,pad=-14, fontweight='normal')
    axs[i].set_frame_on(False)
    axs[i].axis('off')

x_list = ["LOAD","RUN","LOAD","RUN"]
sub_list = [] 
for i in range(4):
    ax = fig.add_subplot(1,4,i+1)
    sub_list.append(ax)
    #ax.set_xlabel(x_list[i], fontsize=15)

print(sub_list)
'''
sub_list = []
for i in range(len(axs)):
    sub_list.append(axs[i])
'''
x_list = ["LOAD","RUN","LOAD","RUN"]
index_list = np.array([i*0.8 for i in range(workload_num)])
y_list = ["Time (s)", "TpmC", "Time (s)", "Time (s)"]
#color => matplotlib color 참고
for i in range(len(sub_list)):
    print(i)
    p1 = sub_list[i].bar(index_list-0.3, th_list[i][0], width=0.1, color = 'indianred', align='edge', edgecolor='black', zorder=3)
    p2 = sub_list[i].bar(index_list-0.2, th_list[i][1], width=0.1, color = 'skyblue', align='edge', edgecolor='black', zorder=3)
    p3 = sub_list[i].bar(index_list-0.1, th_list[i][2], width=0.1, color = 'orange', align='edge', edgecolor='black', zorder=3)
    p4 = sub_list[i].bar(index_list+0.0, th_list[i][3], width=0.1, color = 'darkseagreen', align='edge', edgecolor='black', zorder=3)
    p5 = sub_list[i].bar(index_list+0.1, th_list[i][4], width=0.1, color = 'plum', align='edge', edgecolor='black', zorder=3)
    p6 = sub_list[i].bar(index_list+0.2, th_list[i][5], width=0.1, color = 'midnightblue', align='edge', edgecolor='black', zorder=3)
    plist = [p1,p2,p3,p4,p5,p6]
    #sub_list[i].set_xlabel(x_list[i],fontsize=15)
    #sub_list[i].set_xticks(index_list,workname_list, fontsize=14)
    sub_list[i].tick_params(axis='y',direction='in', right=True, labelsize=14)
    sub_list[i].set_xticks([0])
    sub_list[i].set_xticklabels([x_list[i]])
    sub_list[i].tick_params(axis='x', direction='in', labelsize=14)
    print(x_list[i])
    #sub_list[i].set_xticklabels(x_list[i])
    
    #축 lim 설정 (x,y)
    if i == 0:
        sub_list[i].set_ylim([0,350])
    #sub_list[i].set_xlim([0,3000])
    #sub_list[i].set_xlabel("Time (ms)", fontsize=15, fontproperties=font)
    #if i == 0:
    sub_list[i].set_ylabel(y_list[i], fontsize=14)
    sub_list[i].grid(axis='y', color='grey',linestyle='--', zorder = 0)
    #sub_list[i].set_title(title_list[i], fontsize=15, y=-0.15,pad=-14)
fig.legend(plist[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], handlelength=1, handleheight=1,frameon=False,loc="upper center", bbox_to_anchor=(0.52, 1.1),ncol=6, fontsize=14)
#plt.rcParams['legend.handlelength'] = 1
#plt.rcParams['legend.handleheight'] = 1
plt.draw()
#grid 추가시 사용 
#plt.grid(axis='y', color='black',linestyle='--')
#plt.rc('axes', axisbelow=True)

plt.tight_layout()

#legend option: bbox_to_anchor-> 그래프 외부로 legend 빼고 싶을 때 사용 (e.g. (0.5,1)=> 센터 위)
#Frameon: legend frame 만들건지
#ncols: colonm 개수, 6개에 3이면 2*3
#loc: 그래프내 legend 위치, bbox_to_anchor와 상충됨 
#plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('PAGE','COARSE','FINE','SFTL','TPFTL','APPX'),bbox_to_anchor=(0.5, 1.3), loc='upper center', frameon=False, fontsize=11, ncol=3)

plt.draw()


plt.savefig(output_path+output_name+".eps", format='eps', bbox_inches="tight") #eps 저장 
plt.savefig(output_path+output_name+".png", format='png', dpi=1200, bbox_inches="tight") #png 저장 dpi<1500 1500이상시 컴퓨터 엄청 렉걸림

