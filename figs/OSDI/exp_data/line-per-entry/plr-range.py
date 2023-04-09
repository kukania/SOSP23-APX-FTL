import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes 
from matplotlib.font_manager import FontProperties
import matplotlib
import matplotlib as mat
###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 1
workname_list = ["BF-PLR"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path ="data.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_fio"#분석할 sheet name 입력 
sheet_name = "new_data"
output_path = "" # default: ""
output_name = "PLR-Range" 
#output_name = "TPCH"

def extract_xy(idx, path, sheet_name):
	start_int = 2
	df_from_excel = pd.read_excel(path,
							  sheet_name = sheet_name,
							  header = 2,
							  usecols=[start_int,start_int+1, start_int+2]
					)
	x = np.array(df_from_excel["density"])
	y1 = np.array(df_from_excel["OURS"])		
	return x, y1

x, y1= extract_xy("0", result_path, sheet_name)

print(x)
print(y1)
#print(y2)
#일단 넣어놓은 코드 
#font = FontProperties()
#font.set_family('serif')
#font.set_name('Droid Sans')

#figure size=(16,4) subgraph가 4개이기 때문에 각각 4,4로 크기 맞추기 위해 설정
fig = plt.figure(figsize=(4,3.785))
fsize = 25.5
matplotlib.rc('axes', linewidth=2.5)
font = "Times New Roman"
#font = "Helvetica"
csfont = {'fontname':'Times New Roman'}
if font == "Times New Roman":
	plt.rcParams["font.family"] = "Times New Roman"
	mat.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman']
	mat.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

OURS = plt.plot(x, y1, linewidth=1.5, color="midnightblue", markerfacecolor="None",marker='v', markersize=11, markevery=[0,12,24,36,48])
#BF = plt.plot(x, y2, linewidth=1.5, color="green", markerfacecolor="None",marker='o', markersize=11, markevery=[0,12,24,36,48])
#PLR = plt.plot(x, y3, linewidth=1.5, color="orangered", markerfacecolor="None",marker='^', markersize=11, markevery=[0,12,24,36,48])
#subplot 생성, 4개, 각 subplot draw object를 sub_list에 넣음
plt.xlabel("Run size", fontsize=fsize)
plt.ylabel("Line-per-entry", fontsize=fsize)
plt.xlim([1,50])
plt.ylim([5,20])
plt.yticks([0,10,20], fontsize=fsize, x=-0.015)
plt.xticks([1,25,50],["1x", "25x", "50x"], fontsize=fsize, y=-0.015)
#plt.xtickslabel([0,5,10,15,20])
plt.grid(axis='y', color='grey',linestyle='--',linewidth=1.2,zorder=0)
plt.rc('axes', axisbelow=True)

plt.tick_params(axis='y',direction='in', right=True)
plt.tick_params(axis='x', direction='in')

plt.legend([OURS], labels=["PLR"], frameon=False,loc="upper center", bbox_to_anchor=(0.48, 1.23),ncol=3, handlelength=1, columnspacing=1, handletextpad=0.2,fontsize=20)
#fig.legend(tmp_list[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], frameon=False,loc="lower right", bbox_to_anchor=(0.91,0.09),ncol=1, fontsize=13)
plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=600, bbox_inches = "tight")
plt.savefig(output_path+output_name+".png", format='png', dpi=600, bbox_inches = "tight")
