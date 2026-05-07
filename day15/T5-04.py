import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json


# [1] T5_data.json 파일내 'risk_return_data'
with open('./T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['risk_return_data'])

# [2] 산점도 : 리스크 대비 수익률, 값에 따른 계산식별로 원형크기 조정 -> 버블 차트 
plt.scatter(df['리스크'], df['수익률(%)'])
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.title('리스크 대비 수익률 산점도')
plt.show()

# 버블 차트
plt.scatter(df['리스크'], df['수익률(%)'], s = df['리스크']*1000, alpha=0.5)
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.title('리스크 대비 수익률 버블 차트')
plt.show()


# [3] 산점도 : 자산별(그룹) 리스크 대비 수익률
categories = df['자산'].unique() # 중복제거된 자산 리스트
colors = ['red', 'green', 'blue', 'orange', 'cyan', 'skyblue', '#4FDE3E', '#DE83F3']

for i, category in enumerate(categories) : # enumerate(리스트) 반복순회자로 인덱스와 요소값 하나씩 반환 
    subset = df[df['자산'] == category] # 동일한 자산 정보 가져오기.
    print(subset)
    plt.scatter(subset['리스크'], subset['수익률(%)'], color = colors[i], label = category)
    
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.legend()
plt.title('리스크 대비 수익률(자산별)')
plt.show()

