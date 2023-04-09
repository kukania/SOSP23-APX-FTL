import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 
'''
#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 6
workname_list = ["OLTP", "Varmail", "Webproxy", "Webserver"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path = "FAST21-RESULT-throughput.xlsx" #분석위한 xlsx파일 path 입력
sheet_name = "16_frag_filebench" #분석할 sheet name 입력 
#sheet_name = "16_frag_tpch"
output_path = "" # default: ""
output_name = "Filebench_new_throughput" 
#output_name = "TPCH"
'''
workload_num = 1
workname_list = ["SR"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path = "data.xlsx" #분석위한 xlsx파일 path 입력
sheet_name = "16_fio_frag" #분석할 sheet name 입력 
#sheet_name = "16_frag_tpch"
output_path = "" # default: ""
output_name = "fio_sr_throughput" 

# extract_throughput: 엑셀을 읽어들여 Throughput 결과 출력 
def extract_throughput(workload_num, path, sheet_name):
    use_col = [i+1 for i in range(workload_num)]
    df = pd.read_excel(path, #file path
                              sheet_name = sheet_name, #sheet name
                              header = 0, #0번째 row를 header로
                              usecols=[5], #해당 col만 데이터로 사용하겠다.
                               nrows=6 #6개의 row만 읽는다.
                             )
    df_trp = df.transpose() #ploting을 위한 변환
    th_list = []
    name_list = ["A","B","C","D","E","F"]
    df_trp.columns = name_list
    for i in range(6):
        th_list.append(np.array(df_trp[name_list[i]]))
    return th_list

# th_list: throughput list     
th_list = extract_throughput(workload_num, result_path, sheet_name)


#font 설정, 주석 처리하면 기본 글씨체 사용 (해당 부분은 time new roman을 사용하기 위한 것)
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
from matplotlib import rc

plt.rc('font', family='sans-serif') 
plt.rc('font', serif='Helvetica') 
plt.rcParams['axes.xmargin'] = 0.2
#figure 사이즈 변경하고 싶을 때 사용, figsize = (a,b)에서 a가 더 커야 이쁨
plt.figure(figsize=(workload_num*1.6,3))

index_list = np.array([i*0.8 for i in range(workload_num)])

#color => matplotlib color 참고
p1 = plt.bar(index_list-0.3, th_list[0], width=0.1, color = 'indianred', align='edge', edgecolor='black', zorder=3)
p2 = plt.bar(index_list-0.2, th_list[1], width=0.1, color = 'skyblue', align='edge', edgecolor='black', zorder=3)
p3 = plt.bar(index_list-0.1, th_list[2], width=0.1, color = 'orange', align='edge', edgecolor='black', zorder=3)
p4 = plt.bar(index_list+0.0, th_list[3], width=0.1, color = 'darkseagreen', align='edge', edgecolor='black', zorder=3)
p5 = plt.bar(index_list+0.1, th_list[4], width=0.1, color = 'plum', align='edge', edgecolor='black', zorder=3)
p6 = plt.bar(index_list+0.2, th_list[5], width=0.1, color = 'midnightblue', align='edge', edgecolor='black', zorder=3)

color_list = ['firebrick','skyblue', 'darkorange', 'green', 'pink', 'black']

plist = [p1,p2,p3,p4,p5,p6]
plt.xlabel('Workload',fontsize=14)
plt.ylabel('Throughput (MB/s)',fontsize=14)
plt.yticks([(i)*500 for i in range(6)], fontsize=14)
plt.ylim([0,2500])
plt.xticks(index_list,workname_list, fontsize=14)

#grid 추가시 사용 s
plt.grid(axis='y', color='grey',linestyle='--',zorder=0)
plt.rc('axes', axisbelow=True)

plt.tick_params(axis='y',direction='in', right=True)
plt.tick_params(axis='x', direction='in', top=True)
#plt.tight_layout()
#fig.set_rasterized(True)
#legend option: bbox_to_anchor-> 그래프 외부로 legend 빼고 싶을 때 사용 (e.g. (0.5,1)=> 센터 위)
#Frameon: legend frame 만들건지
#ncols: colonm 개수, 6개에 3이면 2*3
#loc: 그래프내 legend 위치, bbox_to_anchor와 상충됨 
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1
#plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('PAGE','COARSE','FINE','SFTL','TPFTL','APPX'),framealpha=1, bbox_to_anchor=(1.03,1.22), fontsize=13, ncol=6, edgecolor='white')

plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=1500, bbox_inches="tight")
plt.savefig(output_path+output_name+".png", format='png', dpi=1200, bbox_inches="tight") #png 저장 dpi<1500 1500이상시 컴퓨터 엄청 렉걸림

