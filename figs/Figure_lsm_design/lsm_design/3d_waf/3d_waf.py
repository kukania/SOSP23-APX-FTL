from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import math
import matplotlib.patheffects as PathEffects
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib

def log_tick_formatter(val, pos=None):
    return f"$2^{{{int(val)}}}$"

fig = plt.figure()
#fig.subplots_adjust(bottom=-0.15,top=1.2)
ax = fig.add_subplot(111, projection = "3d")
ax.set_rasterized(True)
ax.set_rasterization_zorder(-10)
ax=Axes3D(fig)
fig.subplots_adjust(left=0.4, right=0.6, top=0.6, bottom=0.4, hspace=0., wspace=0)
ax.set_box_aspect(aspect = (0.8,0.8,0.4))

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

# memory usage: slack에 보내주신 양식대로 txt파일 만들으셔야함!
f = open("waf.txt", "r")
tmp = f.readlines()
WAF_list = [0. for i in range(16)]
for i in range(len(tmp)):
    sub = tmp[i].split("\t")
    for j in range(4):
        WAF_list[j*4+i]=float(sub[j+1])
        
#usage_list = [0.213, 0.215, 0.385, 0.435, 0.192, 0.216, 0.276, 0.435, 0.193, 0.197, 0.275, 0.415, 0.199, 0.225, 0.329, 0.445]

# 어떤 시야로 출력할건지
ax.view_init(elev=12, azim=-13)
#ax.view_init(elev=0, azim=-0)
#ax.view_init(elev=0, azim=-0)
#ax.set_box_aspect(aspect = (0.2,0.2,0.1))
WAF_list = np.array(WAF_list)+1
print(WAF_list)
#WAF_list = WAF_list
#label name
ax.set_xlabel("T", fontsize =14, labelpad=-3)
ax.set_ylabel("L0 (MB)",fontsize =14, labelpad=7)
ax.set_zlabel("   WAF   ",fontsize=14, labelpad=-1)

#수정 x
ax.set_xticks([2.5,4.5,6.5,8.5])
ax.set_yticks([2.5,4.5,6.5,8.5])
ax.set_zticks([5,10,15,20])
ax.set_zticks([i+1 for i in range(21)], minor=True)
ax.grid(True, color='black', linestyle='--')
#ax.zaxis._axinfo["grid"].update({"linewidth":1})
#x, y축 label
ax.set_xticklabels(["2","14","26","38"])
ax.set_yticklabels(["5","169","5420","173456"])
#ax.set_zticklabels([2.5*i for i in range(8)], minor=False)
#z축 range
ax.set_zlim3d(0,20)

#label size
ax.tick_params(axis='x', labelsize=12, labelbottom=False, labeltop=True, pad=3)
ax.tick_params(axis='y', labelsize=12, labelbottom=True, labeltop=True, pad=2)
ax.tick_params(axis='z', labelsize=12, labelbottom=True, labeltop=True, pad=-1)

#수정 x
ypos = np.array([2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8])
xpos = np.array([2,2,2,2,4,4,4,4,6,6,6,6,8,8,8,8])
zpos = np.zeros(16)

dx = np.array([0.5 for i in range(16)])
dy = np.array([0.5 for i in range(16)])
dz = np.array(WAF_list)

_zpos = zpos   # the starting zpos for each bar

#breakdown element color 설정
colors = ["wheat", "chocolate",'saddlebrown', 'darkred']
#colors = ["mistyrose", "indianred", "brown", "darkred"]
#colors = ["pink", "indianred", "brown", "purple"]
#colors = ["darkgrey", "rosybrown", "indianred", "brown"]
dx = np.array([0.8 for k in range(16)])
dy = np.array([0.8 for k in range(16)])

def color_matching(value):
	
	if value == 2:
		return colors[0]
	elif value >=3 and value < 4:
		return colors[1]
	elif value >=4 and value < 6:
		return colors[2]
	elif value >=6 and value < 20:
		return colors[3]

for i in range(16):
	bar = ax.bar3d(xpos[i], ypos[i], _zpos[i], dx[i], dy[i], dz[i], color=color_matching(dz[i]), edgecolor='black', linewidth=0.5)
#bar_list.append(bar)
#_zpos += dz
# add the height of each bar to know where to start the next

plt.gca().invert_xaxis()
'''
txt_list = []
for i in range(4):
    txt = ax.text(xpos[i], ypos[i]-0.1, _zpos[i]+0.5, round(_zpos[i],2), fontsize=16, zorder=100)
    txt_list.append(txt)
    txt_list[-1].set_path_effects([PathEffects.withStroke(linewidth=2, foreground='w')])
#plt.show()
'''
#plt.show()
#plt.tight_layout()
#ax.margins(y=0)
#plt.margins(y=0)
b1 = plt.Rectangle((0, 0), 1, 1, fc=colors[0])
b2 = plt.Rectangle((0, 0), 1, 1, fc=colors[1])
b3 = plt.Rectangle((0, 0), 1, 1, fc=colors[2])
b4 = plt.Rectangle((0, 0), 1, 1, fc=colors[3])
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1
#plt.legend([b1,b2,b3,b4],['TLB', 'E-Map', 'PLR', "BF"], ncol=4, frameon=False)
ax.legend([b1,b2,b3,b4],['2', '3', '4~5', ">=6"], framealpha=1, bbox_to_anchor=(0.5,0.8), fontsize=14, ncol=2,edgecolor='white')
#ax.legend([b1,b2,b3,b4],['<5', '5<=WAF<10', '10<=WAF<15', ">=15"], framealpha=1, bbox_to_anchor=(0.93,0.9), fontsize=14, ncol=2,edgecolor='white')



plt.draw()
from matplotlib.transforms import Bbox
bbox = Bbox(np.array([[0,0],[1,1]]))

#exportgraphics(plt,'fourplots.eps','BackgroundColor','none')
plt.savefig('3d_waf_2.png', dpi=1000, bbox_inches = "tight", pad_inches = 0)
#plt.savefig('WAF.svg', dpi=1000, format='svg', bbox_inches = "tight")
#plt.savefig('WAF.pdf', format='pdf', dpi=1000, bbox_inches = "tight")
plt.savefig('3d_waf_2.eps', dpi=1000, format='eps', bbox_inches = "tight")
#plt.savefig('WAF.eps', format='eps', pad_inches = 0)
