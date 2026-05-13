import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns

# [1] 데이터 불러오기
file_path = 'project/data/books.csv'

df = pd.read_csv(file_path)
print(df.head())

# 가격 데이터 전처리
# 가. 쉼표(,) 제거 및 "원" 문자열 제거
df['가격'] = df['가격'].str.replace(',', '').str.replace('원', '')
# 나. 숫자형(int) 변환
df['가격'] = df['가격'].astype(int)

# 출판년월 데이터 전처리
# 가. 연도(year) 컬럼 추출
df['연도'] = df['출판년월'].str.split('년').str[0].astype(int)
# 나. 월(month) 컬럼 추출,
df['월'] = df['출판년월'].str.split('년').str[1].str.replace('월', '').str.strip().astype(int)

print(df.head())


# 3. 기본 통계 분석 기능
#   1. 가격 통계 분석
#     가. 평균 가격 계산
avg_price = df['가격'].mean()
print(avg_price)
#     나. 최고 가격 계산

max_price = df['가격'].max()
print(max_price)

#     다. 최저 가격 계산
min_price = df['가격'].min()
print(min_price)

#   2. 출판년도 분석
#     가. 연도별 도서 수 계산
year_counts = df['연도'].value_counts().sort_index()
print(year_counts)

# 4. 데이터 시각화 기능
#   1. 가격 분포 시각화
plt.figure(figsize=(10, 6))
#     가. 히스토그램 구현
sns.histplot(df['가격'], bins=10, color='blue')
#     나. 가격대별 도서 개수 출력
#     다. 그래프 제목 및 축 이름 출력
plt.title('도서 가격 분포')
plt.xlabel('가격(원)')
plt.ylabel('도서 개수')
plt.show()
#   2. 출판년도별 도서 수 시각화
#     가. 막대그래프 구현
plt.figure(figsize=(10, 6))
#     나. 연도별 출판 도서 수 출력
#     다. 그래프 제목 및 축 이름 출력
plt.bar(year_counts.index, year_counts.values, color = 'red' )
plt.title('출판년도별 도서 수')
plt.xlabel('출판 연도')
plt.ylabel('출판된 도서 개수')
plt.show()

