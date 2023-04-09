from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import math
import matplotlib.patheffects as PathEffects

def log_tick_formatter(val, pos=None):
    return f"$2^{{{int(val)}}}$"

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection = "3d")
ax.set_rasterized(True)
ax.set_rasterization_zorder(-10)
ax=Axes3D(fig)
fig.subplots_adjust(left=0.4, right=0.6, top=0.6, bottom=0.4, hspace=0., wspace=0)
ax.set_box_aspect(aspect = (0.8,0.8,0.4))

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# memory usage: slack에 보내주신 양식대로 txt파일 만들으셔야함!
f = open("memory_usage.txt", "r")
tmp = f.readlines()
usage_list = []
for i in range(len(tmp)):
    sub = tmp[i].split("\t")
    for j in range(4):
        usage_list.append(float(sub[j+1]))
        
#usage_list = [0.213, 0.215, 0.385, 0.435, 0.192, 0.216, 0.276, 0.435, 0.193, 0.197, 0.275, 0.415, 0.199, 0.225, 0.329, 0.445]

# breakdown: slack에 보내주신 양식대로 넣어야 함)
f = open("breakdown.txt", "r")
tmp = f.readlines()
data_list = []
L0 = []
BF = []
PLR = []
TLB = []

for i in range(len(tmp)):
    sub = tmp[i].split("\t")
    mul_value = float(usage_list[(i%4)*4+int(i/4)])
    L0.append(float(sub[1])*mul_value)
    BF.append(float(sub[2])*mul_value)
    PLR.append(float(sub[3])*mul_value)
    TLB.append(float(sub[4])*mul_value)

# 어떤 시야로 출력할건지
ax.view_init(elev=12, azim=-13)



#label name
ax.set_xlabel("T", fontsize =14, labelpad=-3)
ax.set_ylabel("L0 (MB)",fontsize =14, labelpad=4.5)
ax.set_zlabel("Memory", fontsize=14, labelpad=-3)

#수정 x
ax.set_xticks([2.5,4.5,6.5,8.5])
ax.set_yticks([2.5,4.5,6.5,8.5])
#x, y축 label
ax.set_xticklabels(["2","14","26","38"])
ax.set_yticklabels(["5","169","5420","173456"])
#ax.tick_params(axis='x', which='major', pad=10)
#z축 range
ax.set_zlim3d(0,0.7)

#label size
ax.tick_params(axis='x', labelsize=12, labelbottom=False, labeltop=True, pad=1)
ax.tick_params(axis='y', labelsize=12, pad=0)
ax.tick_params(axis='z', labelsize=12, labelbottom=True, labeltop=True, pad=0)

#수정 x
ypos = np.array([2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8])
xpos = np.array([2,2,2,2,4,4,4,4,6,6,6,6,8,8,8,8])
#zpos = np.zeros(16)

dx = np.array([0.8 for i in range(4)])
dy = np.array([0.8 for i in range(4)])
dz = [TLB, L0, PLR, BF]

#_zpos = zpos   # the starting zpos for each bar

#breakdown element color 설정
#colors = ["yellow", "slategrey", "orangered", "limegreen"]
colors = ["salmon", "lightgreen", "lightskyblue", "purple"]

point_203 = [0., 0., 0.]
for i in range(4):
	_zpos = np.zeros(4)
	dx = np.array([0.8 for k in range(4)])
	dy = np.array([0.8 for k in range(4)])
	#_zpos = zpos[i*4:i*4+4]

	for j in range(4):
		tmp_dx = np.array([0.8 for k in range(4)])
		tmp_dy = np.array([0.8 for k in range(4)])
		if dz[j][i*4+j] == 0.0:
			tmp_dx[j] = 0
			tmp_dy[j] = 0
		#print(tmp_dx, "\n", tmp_dy)
		bar = ax.bar3d(xpos[i*4:i*4+4],ypos[i*4:i*4+4], _zpos, tmp_dx, tmp_dy, dz[j][i*4:i*4+4], color=colors[j], edgecolor='black', linewidth=0.5)
		#bar_list.append(bar)
		_zpos+= dz[j][i*4:i*4+4]
		for k in range(4):
			if round(_zpos[k],3) == 0.203:
				print("203!")
				point_203[0] = xpos[i*4+k]
				point_203[1] = ypos[i*4+k]
				point_203[2] = 0.203
				print(point_203)


'''
bar_list = []
for i in range(4):
    dx = np.array([0.8 for k in range(16)])
    dy = np.array([0.8 for k in range(16)])
    for j in range(len(dz[i])):
        if dz[i][j] == 0.0:
            print("0!")
            #dz[i][j] = -0.0001
            dy[j] = 0
            dx[j] = 0
    bar = ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i], edgecolor='black', linewidth=0.5)
    bar_list.append(bar)
    _zpos += dz[i]    # add the height of each bar to know where to start the next
'''
plt.gca().invert_xaxis()


b1 = plt.Rectangle((0, 0), 1, 1, fc=colors[0])
b2 = plt.Rectangle((0, 0), 1, 1, fc=colors[1])
b3 = plt.Rectangle((0, 0), 1, 1, fc=colors[2])
b4 = plt.Rectangle((0, 0), 1, 1, fc=colors[3])
plt.rcParams['legend.handlelength'] = 1
plt.rcParams['legend.handleheight'] = 1
#plt.legend([b1,b2,b3,b4],['TLB', 'E-Map', 'PLR', "BF"], ncol=4, frameon=False)
plt.legend([b1,b2,b3,b4],['S-TLB', 'E-Idx', 'PLR', "BF"], framealpha=1, bbox_to_anchor=(0.6,0.8), fontsize=14, ncol=2,edgecolor='white')
'''
txt_list = []
for i in range(16):
	if round(_zpos[15-i], 3) == 0.203:
		txt = ax.text(xpos[15-i]+0.2, ypos[15-i], _zpos[15-i]+0.015, round(_zpos[15-i],3),fontsize=16, zorder=100)
		txt_list.append(txt)
		txt_list[-1].set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
'''

txt = ax.text(point_203[0]+0.3, point_203[1]-0.2, point_203[2]+0.02, round(point_203[2], 3), fontsize=16, zorder=100)
txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
#plt.show()
plt.draw()


plt.savefig('3d_memory.png', dpi=1000, bbox_inches = "tight")
#plt.savefig('fig1.svg', dpi=1000, format='svg', bbox_inches = "tight")
#plt.savefig('fig1.pdf', format='pdf', dpi=1000, bbox_inches = "tight")
plt.savefig('3d_memory.eps', format='eps', dpi=1000,bbox_inches = "tight")
