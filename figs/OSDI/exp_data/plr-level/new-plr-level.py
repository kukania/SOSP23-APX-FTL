import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes 
from matplotlib.font_manager import FontProperties
import matplotlib
import matplotlib as mat
from matplotlib import RcParams
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 1
workname_list = ["BF-PLR"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
#workname_list = ["TPC-H"]
result_path ="data.xlsx" #분석위한 xlsx파일 path 입력
#sheet_name = "16_fio"#분석할 sheet name 입력 
sheet_name = "test"
output_path = "" # default: ""
output_name = "level-PLR" 
#output_name = "TPCH"

scale_fac = 135
xlim = [0,scale_fac]
ylim = [0,14]
def extract_xy(idx, path, sheet_name):
    start_int = 2
    df_from_excel = pd.read_excel(path,
                              sheet_name = sheet_name,
                              header = 2,
                              usecols=[start_int,start_int+1]
                    )
    x = np.array(df_from_excel["Densely sorted"])
    y1 = np.array(df_from_excel["Coalesced entry"])        
    return x, y1

x, y1, = extract_xy("0", result_path, sheet_name)
x = x[:scale_fac]
y1 = y1[:scale_fac]
print(x)
print(y1)
four_idx = 0
for i in range(len(y1)):
	if y1[i] >= 8:
		four_idx = i
		break
#일단 넣어놓은 코드 
#font = FontProperties()
#font.set_family('serif')
#font.set_name('Droid Sans')

#figure size=(16,4) subgraph가 4개이기 때문에 각각 4,4로 크기 맞추기 위해 설정
fig = plt.figure(figsize=(6,2))
fsize = 14
matplotlib.rc('axes', linewidth=1.5)
font = "Times New Roman"
#font = "Helvetica"
csfont = {'fontname':'Times New Roman'}
if font == "Times New Roman":
#plt.rcParams["font.family"] = "Times New Roman"
    mat.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman']
    mat.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
mat.rcParams['text.usetex']=True

latex_style_times = RcParams({'font.family': 'serif',
               'font.serif': ['Times'],
               'text.usetex': True,
               })

plt.style.use(latex_style_times)
test = plt.plot(x, y1, linewidth=0.8, color="red",zorder=5)
test = plt.plot([four_idx, four_idx], [0,ylim[1]], linestyle='--',linewidth=0.8, color='darkred',zorder=3)
high = plt.gca().add_patch(
   patches.Rectangle(
      (0,0),                   # (x, y)
      four_idx, ylim[1],                     # width, height
      edgecolor = "None",
      facecolor = 'mistyrose',
      fill=True,
	  zorder=1
   ))
low = plt.gca().add_patch(
   patches.Rectangle(
      (four_idx, 0),                   # (x, y)
      scale_fac-1, ylim[1],                     # width, height
      edgecolor = 'None',
      facecolor = 'aliceblue',
      fill=True,
	  zorder=1
   ))


xx = np.array(x)
print(xx[0])
xx[0] = 1
yy = 1.7228*np.log(xx)+3.4267
#yy = 1.6828*np.log(xx)+4.1267
xxx = list(xx)
yyy = list(yy)
xxx.insert(0,0)
yyy.insert(0,0)
		
plt.plot(xxx,yyy,linewidth=0.8,linestyle='--',color='midnightblue',zorder=5)
#test = plt.plot([x[0],x[-1]], [4,4], linestyle='-',linewidth=1.1, color='red',zorder=6)
#test = plt.plot(x, y1, linewidth=1.5, color="midnightblue", markerfacecolor="None",marker='^', markersize=11, markevery=[0,9,19,29])
#subplot 생성, 4개, 각 subplot draw object를 sub_list에 넣음
plt.xlabel("Level height", fontsize=fsize)
plt.ylabel("Mapping entries\nper equation", fontsize=fsize,labelpad=5)
plt.xlim([1,scale_fac])
plt.ylim([0,14])
plt.yticks([0,4,8,12], fontsize=fsize, x=-0.005)
plt.gca().yaxis.get_ticklabels()[2].set_color("red")
#plt.grid(linestyle='--',linewidth=0.8,color='grey')
plt.xticks([x[0],four_idx+1, x[-1]], ["1","k","h-1"],fontsize=fsize)
#plt.xticks([(four_idx+1)/2., (x[-1]-four_idx)/2+four_idx],[r'$L_{1 \sim k-1}$', r'$L_{k \sim h-1}$'], fontsize=fsize, y=-0.06)
print(len(x))
#plt.annotate('', (x[0],y1[0]), (four_idx,y1[0]), clip_on=False, arrowprops={'arrowstyle':'<->'},zorder=15)
#plt.text(21,3,"High memory overhead",fontsize=fsize,color='red')
#plt.annotate('', xy=(0.95,0.7), xycoords='axes fraction', xytext=(0.95, -0.01),arrowprops=dict(arrowstyle="<->", linewidth=0.5,color='red'))


text1 = plt.text((four_idx+1)/2, 1.9, r'$L_{1 \sim k-1}$', fontsize=fsize, ha='center', zorder=8)
text2 = plt.text((x[-1]-four_idx)/2+four_idx, 1.9, r'$L_{k \sim h-1}$', fontsize=fsize, ha='center', zorder=8)

text = [text1, text2]
for i in range(2):
    text[i].set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'),
                       path_effects.Normal()])


plt.annotate('', xy=(0, 0.05), xycoords='axes fraction', xytext=(four_idx/scale_fac, 0.05),arrowprops=dict(arrowstyle="<->", linewidth=0.5,color='black'))
plt.annotate('', xy=(four_idx/scale_fac, 0.05), xycoords='axes fraction', xytext=(1.00, 0.05),arrowprops=dict(arrowstyle="<->", linewidth=0.5,color='black'))
plt.tick_params(axis='x', bottom=False)
#plt.xtickslabel([0,5,10,15,20])
#plt.grid(axis='y', color='grey',linestyle='--',linewidth=1.2,zorder=0)
#plt.rc('axes', axisbelow=True)

plt.tick_params(axis='y',direction='in', right=True)
plt.tick_params(axis='x', direction='in')
#plt.legend(handles=[high, fake],labels=["High mem. overhead", "Low mem. overhead"], frameon=False, loc="upper center", bbox_to_anchor=(0.48,1.32),ncol=2, handlelength=0.8, handleheight=0.8, columnspacing=1, handletextpad=0.2, fontsize=fsize)
#plt.legend([OURS,BF,PLR], labels=["OURS","BF","PLR (ORIG)"], frameon=False,loc="upper center", bbox_to_anchor=(0.48, 1.25),ncol=3, handlelength=1, columnspacing=1, handletextpad=0.2,fontsize=20)
#fig.legend(tmp_list[:6], labels=["PAGE","COARSE","FINE","SFTL", "TPFTL", "APPX"], frameon=False,loc="lower right", bbox_to_anchor=(0.91,0.09),ncol=1, fontsize=13)
plt.draw()

plt.savefig(output_path+output_name+".eps", format='eps', dpi=600, bbox_inches = "tight")
plt.savefig(output_path+output_name+".png", format='png', dpi=600, bbox_inches = "tight")
