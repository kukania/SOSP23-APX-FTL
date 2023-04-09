import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###해당 부분은 입력해주셔야하는 부분입니다.
###xlsx 파일의 경우 양식에 맞추어 작성해주세요!! 

#workload의 개수 입력, workname_list는 각각의 workload name을 작성.  
workload_num = 3
workname_list = ["oltp","varmail","webproxy"] #반드시 workname_list elem 개수와 workload num이 일치해야함. 
result_path = "FAST21-RESULT-throughput.xlsx" #분석위한 xlsx파일 path 입력
sheet_name = "16_frag_high_default" #분석할 sheet name 입력 
output_path = "" # default: ""
output_name = "filebench" 


# extract_throughput: 엑셀을 읽어들여 Throughput 결과 출력 
def extract_throughput(workload_num, path, sheet_name):
    use_col = [i+1 for i in range(workload_num)]
    df = pd.read_excel(path, #file path
                              sheet_name = sheet_name, #sheet name
                              header = 0, #0번째 row를 header로
                              usecols=use_col, #해당 col만 데이터로 사용하겠다.
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
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

#figure 사이즈 변경하고 싶을 때 사용, figsize = (a,b)에서 a가 더 커야 이쁨
plt.figure(figsize=(7,3))

index_list = np.array([i*0.8 for i in range(workload_num)])

#color => matplotlib color 참고
p1 = plt.bar(index_list-0.3, th_list[0], width=0.1, color = 'white', align='edge', edgecolor='black')
p2 = plt.bar(index_list-0.2, th_list[1], width=0.1, color = 'skyblue', align='edge', edgecolor='black')
p3 = plt.bar(index_list-0.1, th_list[2], width=0.1, color = 'darkorange', align='edge', edgecolor='black')
p4 = plt.bar(index_list+0.0, th_list[3], width=0.1, color = 'green', align='edge', edgecolor='black')
p5 = plt.bar(index_list+0.1, th_list[4], width=0.1, color = 'pink', align='edge', edgecolor='black')
p6 = plt.bar(index_list+0.2, th_list[5], width=0.1, color = 'black', align='edge', edgecolor='black')


plist = [p1,p2,p3,p4,p5,p6]
plt.xlabel('Workload',fontsize=15)
plt.ylabel('Throughput (ops/s)',fontsize=15)

plt.xticks(index_list,workname_list, fontsize=14)

#grid 추가시 사용 
#plt.grid(axis='y', color='black',linestyle='--')
#plt.rc('axes', axisbelow=True)


plt.tick_params(axis='y',direction='in', right=True)
plt.tick_params(axis='x', direction='in', top=True)
plt.tight_layout()

#legend option: bbox_to_anchor-> 그래프 외부로 legend 빼고 싶을 때 사용 (e.g. (0.5,1)=> 센터 위)
#Frameon: legend frame 만들건지
#ncols: colonm 개수, 6개에 3이면 2*3
#loc: 그래프내 legend 위치, bbox_to_anchor와 상충됨 
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('PAGE','COARSE','FINE','SFTL','TPFTL','APPX'),bbox_to_anchor=(0.5, 1.3), loc='upper center', frameon=False, fontsize=11, ncol=3)

plt.draw()


plt.savefig(output_path+output_name+".eps", format='eps', bbox_inches="tight") #eps 저장 
plt.savefig(output_path+output_name+".png", format='png', dpi=1200, bbox_inches="tight") #png 저장 dpi<1500 1500이상시 컴퓨터 엄청 렉걸림
