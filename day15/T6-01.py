import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns

# 캐글 : 데이터셋 공유하는 사이트, 데이터분석/머신러닝/연구 등 사용되는 곳

df = pd.read_csv('./day15/titanic/train.csv')
print(df.head()) # 속성타입 확인
print(df.isnull().sum()) # 결측치 확인

# [1. 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster
# https://www.kaggle.com/competitions/titanic/overview



# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# [3. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
df['Age'] = df['Age'].fillna(df['Age'].median()) # 177
print(df.isnull().sum())
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.
df['Embarked'].fillna(df['Embarked'].mode()[0]) # 2
print(df.isnull().sum()) # 결측치 확인



# [4. 데이터 시각화 및 분석]
# 4-1 : 생존 분포 분석: 전체 생존자(survival)와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
sns.countplot(data=df, x= 'Survived')
plt.title('생존자 분포') 
plt.xlabel('생존여부 0 : 사망 1 : 생존') # x축 제목
plt.xticks([0, 1], ['사망', '생존']) # 범주형 x축 레이블 수정
plt.ylabel('인원 수')   # y축 제목
plt.show()

# 4-2 : 연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
sns.histplot(data=df, x='Age', hue='Survived', kde=True)
plt.title('연령대별 생존/사망 분포')
plt.show()

# 4-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df, x = 'Sex', hue='Survived' )
plt.title('성별에 따른 생존 여부')
plt.show()

# 4-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('객실 등급에 따른 생존 여부')
plt.show()


# 4-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df, x = 'Embarked', hue='Survived')
plt.title('승선 항구에 따른 생존 여부')
plt.show()


