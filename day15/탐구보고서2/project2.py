import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import seaborn as sns

# 1. 주택 가격 데이터 탐색 분석
# 출처: Kaggle - House Prices - Advanced Regression Techniques

df = pd.read_csv('./day15/탐구보고서2/train.csv')
print(df.head()) # 속성타입 확인

# 본 문서는 Kaggle의 주택 가격 데이터를 활용하여 주택 가격(SalePrice)에 영향을 미치는 주요 요인을 탐색하고 가설을 검증하기 위한 데이터 분석(EDA) 계획을 수립합니다.
# 2. 가설
# 가설 번호
# 내용
# 가설 1 지상 주거 면적 (GrLivArea)이 넓을수록 판매 가격은 정비례하여 상승할 것이다.
# 가설 2 주택의 스타일 (HouseStyle)이나 외장재 (Exterior1st)에 따라 가격 분포의 차이가 뚜렷할 것이다.
# 가설 3 주택 가격과 가장 강력한 상관관계를 가진 특정 수치형 변수들이 존재할 것이다.

# 3. 자료수집
# 단계
# 내용
# 3-1
# 데이터 파일 접근: https://drive.google.com/file/d/1o_6VjiQDwAwHyXFZcu6QsJOigfuFoC82/view
# 3-2
# train_HousePrices.csv 파일 판다스 라이브러리로 불러오기

# 4. 데이터 전처리
# 4-1. 수치형 변수 결측치 처리
# 'LotFrontage', 'MasVnrArea', 'GarageYrBlt' 등의 수치형 변수의 결측치는 데이터의 중앙값(Median)으로 대체하여 보정한다.
df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].median())
df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].median())
df['GarageYrBlt'] = df['GarageYrBlt'].fillna(df['GarageYrBlt'].median())



# 4-2. 범주형 변수 결측치 처리 (정보 부재 명확)
# 정보 부재가 명확한 범주형 변수('Alley', 'PoolQC', 'Fence' 등)는 결측치를 'NoAlley', 'NoPool', 'NoFence'와 같이 특정 문자열로 대체한다.
df['Alley'] = df['Alley'].fillna(df['Alley'])
df['PoolQC'] = df['PoolQC'].fillna(df['PoolQC'])
df['Fence'] = df['Fence'].fillna(df['Fence'])
df['HouseStyle'] = df['HouseStyle'].fillna(df['HouseStyle'])


# 4-3. 범주형 변수 결측치 처리 (일반)
# 아래 17개 주요 범주형 변수는 최빈값(Mode)을 활용하여 결측치를 일괄 보정한다.
mode_cols = ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 
            'Electrical', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 
            'GarageCond', 'MSZoning', 'Functional', 'SaleType', 'Exterior1st', 'Exterior2nd', 'MasVnrType'
]

for col in mode_cols :
    df[col] = df[col].fillna(df[col].mode()[0])
    


# 5. 데이터 시각화 및 분석
# 5-1. 주택 판매 가격(SalePrice) 분포 분석
# sns.histplot을 사용하여 주택 판매 가격(SalePrice)의 분포와 치우침(Skewness) 정도를 확인한다. (KDE 포함)

# [차트 사진]
# [차트 해석]

# 5-2. 주거 면적과 가격 관계 분석 (가설 1 검증)
# sns.scatterplot을 사용하여 지상 주거 면적(GrLivArea)과 판매 가격(SalePrice) 간의 상관관계를 산점도로 분석한다.

# [차트 사진]
# [차트 해석]

# 5-3. 주택 스타일별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 주택 스타일(HouseStyle)별 가격 분포와 이상치(Outlier)를 파악한다.
sns.boxplot(data=df, x='HouseStyle', y='SalePrice')
plt.title('주택 스타일별 가격 분포와 이상치')
plt.show()

# [차트 사진]
# [차트 해석]

# 5-4. 주요 외관 요소별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 지붕 스타일(RoofStyle) 및 외장재(Exterior1st)에 따른 가격 차이를 분석한다.

# [차트 사진]
# [차트 해석]

# 5-5. 상관관계 시각화 및 핵심 인자 도출 (가설 3 검증)
# sns.heatmap을 사용하여 수치형 변수 전체의 상관계수를 시각화하고한다.
