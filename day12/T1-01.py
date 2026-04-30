
# numpy : 배열 기반, 공학 수치 계산
# pandas : 테이블 기반(라벨 포함), 전처리/필터링(+ numpy)

# [1] pandas 설치 : pip install pandas // mac은 brew install pandas 설치해야됨
# [2] import pandas as pd
    # 1차원 : series
    # 2차원 : dataframe
import pandas as pd
print(pd.__version__) # 3.0.2

# series
# 1. 생성
x = [10, 20, 30 ,40 ,50] # 리스트
x = pd.Series(x)
print(x)
# 0    10   # 0 ~ 4 : 각 요소들의 인덱스
# 1    20   # 10 ~ 50 : 각 요소의 값
# 2    30
# 3    40
# 4    50
# dtype : int64 # 데이터의 타입

# 2. 각 요소들의 라벨 포함하기
y = ['a', 'b', 'c', 'd']
z = pd.Series(x, index = y)
print(z)


# 3. 딕셔너리로 생성
# 파이썬 주요 타입, [리스트] (튜플) {딕셔너리}
x = {'apple' : 1, 'banana' : 2, 'cherry' : 3}
z = pd.Series(x)
print(z)

# 4. 주요 속성 확인
print(z.dtype) # 타입반환, int64
print(z.index) # 인덱스반환, Index(['apple', 'banana', 'cherry'], dtype='str')
print(z.values) # 값반환, 1 2 3]
print(z.head(5)) # .head(n), 상위 n개(기본값 : 5)개만 출력(확인용)
print(z.tail((2))) # .tail(n), 하위 n개만 출력
print(z.iloc[0]) # iloc[인덱스번호], 라벨이 아닌 위치로 조회
print(z.iloc[1:3]) # 슬라이싱도 가능

# 5. 인덱싱, 슬라이싱
print(z.iloc[0])                     # iloc[인덱스번호], 라벨이 아닌 위치로 조회
print(z.loc['apple'])                # loc[라벨명], 라벨명으로 조회
print(z.loc['apple' : 'cherry'])     # loc[시작라벨 : 끝라벨]

# 6. 데이터 수정
z['apple'] = 10     # [라벨명] = 새로운값
print(z)
print(z['apple'])   # [라벨명]

# 7. 데이터 추가
z['berry'] = 40     # [새로운라벨명] = 새로운값
print(z)

# 8. 병합, .concat([x, y]), 판다스 합치기 
x = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
y = pd.Series([40, 50], index=['d', 'e'])
z = pd.concat([x, y])
print(z)

# 9. 라벨 이름 변경, .rename({'기존' : '새로운'})
# 파이썬
test = 'hello java' # hello ccccccccjava
test = test.replace(' ', '-') # 문자열(리터럴)은 불변성 특징
print(test) # hello-java 

x = z.rename({'a' : 'apple'})
print(x)

# 10. 필터링, [조건식], [(조건식1) | (조건식2)]
print(z[ z > 30 ]) # 30 초과한 요소 값에 10 더한 후에 
x = z[z > 30]
print(x)

x = z[(z < 25) | (z > 35)] # 25보다 작거나 35보다 크다
print(x)
x = z[(z > 25) & (z < 35)] # 25보다 크면서 35보다 작다
print(x)
z[z > 30] = z[ z > 30 ] + 10 # 30초과 한 요소값에 10 더한 후에 30 초과한 요소에만 대입
print(z)

# 11. 통계
print(z.sum()) # .sum() 합계
print(z.mean()) # .mean() 평균
print(z.max()) # .max() 최대값
print(z.min()) # .min() 최소값
print(z.median()) # .median() 중앙값
print(z.var()) # .var() 분산
print(z.std()) # .std() 표준편차
print(z.count()) # .count() 요소 개수
print(z.value_counts()) # .value_counts() 각 요소별 중복 개수
print(z.value_counts(normalize=True)) # 각 요소가 전체에서 차지하는 비율(0~1)

