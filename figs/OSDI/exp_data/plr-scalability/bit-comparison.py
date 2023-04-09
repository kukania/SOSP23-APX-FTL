import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes 
from matplotlib.font_manager import FontProperties
import matplotlib
import matplotlib as mat
import matplotlib.patheffects as path_effects
###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 1
workname_list = ["FPR"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path ="data.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_fio"#분석할 sheet name 입력 
sheet_name = "bit-data"
output_path = "" # default: ""
output_name = "twinx-scale" 
#output_name = "TPCH"

def extract_xy(idx, path, sheet_name):
    start_int = 1
    df_from_excel = pd.read_excel(path,
                              sheet_name = sheet_name,
                              header = 1,
                    )
    x = np.array(df_from_excel["TB"])
    y1 = np.array(df_from_excel["bit"])        
    y2 = np.array(df_from_excel["APX-FTL"])        
    y3 = np.array(df_from_excel["ratio"])        
    return x, y1,y2,y3

ori_x, y1,y2,y3 = extract_xy("0", result_path, sheet_name)
x = np.array([i+1 for i in range(len(ori_x))])

x = x[:9]
y1 = y1[:9]
y2 = y2[:9]
y3 = y3[:9]
print(x)
print(y1)
print(y2)
print(y3)

#일단 넣어놓은 코드 
#font = FontProperties()
#font.set_family('serif')
#font.set_name('Droid Sans')

font = "Times New Roman"
#font = "Helvetica"
csfont = {'fontname':'Times New Roman'}
if font == "Times New Roman":
#plt.rcParams["font.family"] = "Times New Roman"
    mat.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman']
    mat.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']


#figure size=(16,4) subgraph가 4개이기 때문에 각각 4,4로 크기 맞추기 위해 설정
fig = plt.figure(figsize=(3.4,3.785))
fig, bit = plt.subplots(figsize=(4,3.535))
fsize = 22.5
matplotlib.rc('axes', linewidth=2.5)
ratio = bit.twinx()

sub_list = [ratio, bit]
#font
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

bar_width=0.6
same_xlim=[0,10]

ratio_ylim=[0.2,0.31]
ratio_yticks=[0.2,0.25,0.3]
ratio_yticklabels=[20,25,30]

bit_ylim=[0,42]
bit_yticks=[0,10,20,30,40]

ratio_line = ratio.plot(x, y3, linewidth=1.85, color="red",  zorder=6,marker='o', markerfacecolor="None", markersize=10,markevery=[0,4,8])
text1 = ratio.text(x[0]+0.35,y3[0]+0.005,str(round(y3[0]*100.,1))+"%",fontsize=fsize-1,ha='center',zorder=7)
text2 = ratio.text(x[4],y3[4]+0.005,str(round(y3[4]*100.,1))+"%",fontsize=fsize-1,ha='center',zorder=7)
text3 = ratio.text(x[8]-0.3,y3[8]+0.005,str(round(y3[8]*100.,1))+"%",fontsize=fsize-1,ha='center',zorder=8)
text = [text1, text2, text3]
for i in range(3):
	text[i].set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'),
                       path_effects.Normal()])
ori_bit = bit.bar(x,y1, width=bar_width, color="yellowgreen", edgecolor="black",zorder=4)
apx_bit = bit.bar(x,y2, width=bar_width, color="cornflowerblue", edgecolor="black",zorder=5)

ratio.tick_params(axis='y', direction='in',right=False, labelsize=fsize)
bit.tick_params(axis='x', direction='in', labelsize=fsize)
bit.tick_params(axis='y', direction='in',right=True, labelsize=fsize)

bit.set_xlim(same_xlim)
bit.set_xticks([1,5,9])
bit.set_xticklabels(['16TB', "256TB", "4PB"], y=-0.015)
ratio.set_ylim(ratio_ylim)
ratio.set_yticks(ratio_yticks)
ratio.set_yticklabels(ratio_yticklabels)
bit.set_xlabel("SSD capacity", fontsize=fsize)
ratio.set_ylabel("Percentage (%)", fontsize=fsize, rotation=-90,labelpad=27.5)

bit.set_ylim(bit_ylim)
bit.set_yticks(bit_yticks)
bit.set_ylabel("Bits-per-entry", labelpad=5, fontsize=fsize)





'''
for i in range(len(x)):
	plt.text(x[i]+0.01, y[i]+0.01, y[i], rotation=60, fontsize=13)
'''
#subplot 생성, 4개, 각 subplot draw object를 sub_list에 넣음
#plt.minorticks_on()
#plt.legend([], labels=["PLR","BF"], frameon=False,loc="upper center", bbox_to_anchor=(0.7, 1.05),ncol=2, fontsize=14)
fig.legend(handles=[ori_bit[0], apx_bit[0], ratio_line[0]], handlelength=0.65, handleheight=0.65, labels=["OPT","APX", "Rate"], frameon=False,loc="upper center", columnspacing=1.3, handletextpad=0.3, bbox_to_anchor=(0.5,1.065),ncol=3, fontsize=fsize-1)
plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=1000, bbox_inches = "tight")
plt.savefig(output_path+output_name+".png", format='png',bbox_inches = "tight")
