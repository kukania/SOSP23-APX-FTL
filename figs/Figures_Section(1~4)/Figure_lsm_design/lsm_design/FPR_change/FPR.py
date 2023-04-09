import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes 
from matplotlib.font_manager import FontProperties
import matplotlib

###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 1
workname_list = ["FPR"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path ="data.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_fio"#분석할 sheet name 입력 
sheet_name = "data"
output_path = "" # default: ""
output_name = "FPR" 
#output_name = "TPCH"

def extract_xy(idx, path, sheet_name):
    start_int = 1
    df_from_excel = pd.read_excel(path,
                              sheet_name = sheet_name,
                              header = 2,
                              usecols=[start_int,start_int+1]
                    )
    x = np.array(df_from_excel["FPR"])
    y = np.array(df_from_excel["usage"])        
    index = np.where(x == 0.95)[0][0]
    x = x[:index+1]
    y = y[:index+1]
    return x, y

x, y = extract_xy("0", result_path, sheet_name)
new_x = []
new_y = []

for i in range(len(y)):
	if i%2 == 0:
		new_y.append(y[i])
		new_x.append(x[i])

x = np.array(new_x)
y = np.array(new_y)

#일단 넣어놓은 코드 
#font = FontProperties()
#font.set_family('serif')
#font.set_name('Droid Sans')

#figure size=(16,4) subgraph가 4개이기 때문에 각각 4,4로 크기 맞추기 위해 설정
fig = plt.figure(figsize=(4,4.1))
fsize = 20
matplotlib.rc('axes', linewidth=2.5)
#font
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rc('font', family='sans-serif') 
plt.rc('font', serif='Helvetica') 
x = np.array(x)
usage = plt.plot(x, y, linewidth=2.5, color="orangered", markerfacecolor="None",marker='o', markersize=8, markevery=1)
'''
for i in range(len(x)):
	plt.text(x[i]+0.01, y[i]+0.01, y[i], rotation=60, fontsize=13)
'''
#subplot 생성, 4개, 각 subplot draw object를 sub_list에 넣음
plt.xlabel("Error rate", fontsize=fsize)
plt.ylabel("Memory usage", fontsize=fsize)
#plt.text(0.1,0.2,"AA")
plt.xlim([0.05,0.95])
plt.ylim([0.15,0.22])
plt.yticks([0.16, 0.18, 0.20, 0.22],fontsize=fsize)
plt.xticks([0,0.25,0.5,0.75],["0","0.25","0.5","0.75"], fontsize=fsize)
plt.grid(axis='y', color='grey',linewidth=2,linestyle='--',zorder=0)
plt.rc('axes', axisbelow=True)
#plt.minorticks_on()
plt.tick_params(axis='y',which='minor', direction='in', right=True)
plt.tick_params(axis='y',direction='in', right=True, labelsize=fsize)
plt.tick_params(axis='x', direction='in', labelsize=fsize)
#plt.minorticks_on()
#plt.legend([], labels=["PLR","BF"], frameon=False,loc="upper center", bbox_to_anchor=(0.7, 1.05),ncol=2, fontsize=14)
#fig.legend(tmp_list[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], frameon=False,loc="lower right", bbox_to_anchor=(0.91,0.09),ncol=1, fontsize=13)
plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=1000, bbox_inches = "tight")
plt.savefig(output_path+output_name+".png", format='png',bbox_inches = "tight")
