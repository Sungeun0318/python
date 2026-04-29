import numpy as np

# 1차원 배열 통계
x = np.array([1, 2, 3, 4, 5])

print(np.min(x)) # 최소값
print(np.max(x)) # 최대값
print(np.argmin(x)) # 최소값(인덱스)위치 / 0
print(np.argmax(x)) # 최대값(인덱스)위치 / 4
print(np.ptp(x)) # 최대값 - 최솟값 / 4
print(np.sum(x)) # 합계 / 15
print(np.mean(x)) # 평균 / 3.0
print(np.median(x)) # 중앙값 / 3.0
print(np.var(x)) # 분산 : 요소들의 흩어짐 정도 / 2.0
print(np.std(x)) # 표준편차 : 분산의 양의 제곱근 / 1.4142135623730951
print(np.sqrt(x)) # 루트 / [1.         1.41421356 1.73205081 2.         2.23606798]

# 사분위수 : 구역을 4개 구역으로 나눠서 데이터 분포 위치 파악, q1 : 제1사분위수, 
q1 = np.percentile(x, 25)  # 1/4, 25%, 하위 25%
q3 = np.percentile(x, 75)  # 3/4, 75%, 하위 75%
print(q1)
print(q3)
q2 = np.percentile(x, 50)  # 1/2, 50%, 중앙값 
print(q2)
q4 = q3 - q1
print(q4)

# 2차원 배열 통계, 통계함수(x, axis = 0) 0 = 열 기준, 1 = 행 기준
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.min(y))
print(np.min(y, axis=0)) # 열 개수가 3개이니까 최소값 3개
print(np.min(y, axis=1)) # 행 개수가 3개이니까 최소값 3
print(np.max(y))   # axis 생략하면 2차원배열 평탄화(1차원으로 변경)해서 통계 / 9
print(np.argmax(y)) # 최댓값 위치 / 8(인덱스 위치)
print(np.argmin(y)) # 0
print(np.sum(y)) # 45
print(np.mean(y)) # 5.0
print(np.median(y)) # 5.0
print(np.var(y)) # 6.666666666666667
print(np.std(y)) # 2.581988897471611
print(np.sqrt(y))       # [[1.         1.41421356 1.73205081]
                        # [2.         2.23606798 2.44948974]
                        # [2.64575131 2.82842712 3.        ]]
print(np.argsort(y))    #[[0 1 2]
                        # [0 1 2]
                        # [0 1 2]]
