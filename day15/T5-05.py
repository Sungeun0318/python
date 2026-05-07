
import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json


# [1] T5_data.json 파일내 'financial_performance_data'
with open('./T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['financial_performance_data'])

# [2] 플롯박스 : '수익' '비용' '이익' 별 박스 플롯
# plt.boxplot() : 데이터 최솟값, 최대값, 1사분위, 중앙값 3사분위 시각화
plt.figure(figsize = (10, 6)) 
plt.boxplot([df['수익'], df['비용'], df['이익']], tick_labels=['수익', '비용', '이익'])
plt.title('재무 성과 분포')
plt.ylabel('금액')
plt.show()
            
# [3] 플롯박스 : 분기별 수익 데이터로 박스플롯 표시
df.boxplot(column=['수익'], by='분기')
plt.title('분기별 수익 분포')
plt.suptitle("")
plt.ylabel('수익')
plt.show()

# 재무 성과 분포
fig, ax = plt.subplots(figsize = (10, 6))
ax.boxplot(df[['수익', '비용', '이익']].values, tick_labels=['수익', '비용', '이익'])
ax.bar(['수익', '비용', '이익'], df[['수익', '비용', '이익']].mean(), color='orange', alpha=0.3, label = '평균')
ax.set_ylabel('금액')
ax.legend()
plt.title('재무 성과 분포 및 평균')
plt.show()


