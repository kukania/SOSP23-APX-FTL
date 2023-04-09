from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import math
def log_tick_formatter(val, pos=None):
    return f"$2^{{{int(val)}}}$"

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.set_rasterized(True)
ax.set_rasterization_zorder(-10)
ax=Axes3D(fig)

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
ax.view_init(elev=30, azim=-20)



#label name
ax.set_xlabel("SF", fontsize =15)
ax.set_ylabel("L0 (KB)",fontsize =15)
ax.set_zlabel("Memory",fontsize=15)

#수정 x
ax.set_xticks([2.5,4.5,6.5,8.5])
ax.set_yticks([2.5,4.5,6.5,8.5])
#x, y축 label
ax.set_xticklabels(["2","6","18","54"])
ax.set_yticklabels(["0.5","16","512","16384"])

#z축 range
ax.set_zlim3d(0,0.5)

#label size
ax.tick_params(axis='x', labelsize=12, labelbottom=False, labeltop=True)
ax.tick_params(axis='y', labelsize=12, labelbottom=True, labeltop=True)
ax.tick_params(axis='z', labelsize=12, labelbottom=True, labeltop=True)

#수정 x
ypos = np.array([2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8])
xpos = np.array([2,2,2,2,4,4,4,4,6,6,6,6,8,8,8,8])
zpos = np.zeros(16)

dx = np.array([1 for i in range(16)])
dy = np.array([1 for i in range(16)])
dz = [L0, BF, PLR, TLB]

_zpos = zpos   # the starting zpos for each bar

#breakdown element color 설정
colors = ["lightgreen", "lightpink", "lightskyblue", "lightcoral"]

bar_list = []
for i in range(4):
    bar = ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i], edgecolor='black', linewidth=0.5)
    bar_list.append(bar)
    _zpos += dz[i]    # add the height of each bar to know where to start the next
plt.gca().invert_xaxis()
b1 = plt.Rectangle((0, 0), 1, 1, fc="lightgreen")
b2 = plt.Rectangle((0, 0), 1, 1, fc="lightpink")
b3 = plt.Rectangle((0, 0), 1, 1, fc="lightskyblue")
b4 = plt.Rectangle((0, 0), 1, 1, fc="lightcoral")

plt.legend([b1,b2,b3,b4],['L0','BF', 'PLR', 'TLB'], ncol=4, frameon=False)

plt.draw()


plt.savefig('fig1.png', dpi=1000, bbox_inches = "tight")
plt.savefig('fig1.svg', dpi=1000, format='svg', bbox_inches = "tight")
plt.savefig('fig1.pdf', format='pdf', dpi=1000, bbox_inches = "tight")
plt.savefig('fig1.eps', format='eps', bbox_inches = "tight")
