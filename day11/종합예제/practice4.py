# [ 프로젝트 배경 ] 당신은 대형 온라인 쇼핑몰의 데이터 팀에 소속되어 있습니다. 전 세계 고객들의 [고객
# ID, 방문 횟수, 평균 체류 시간(분), 장바구니 담은 횟수, 최종 구매 금액($)] 데이터를 분석하여, 우수 고객
# (VVIP)을 식별하고 마케팅 효율을 높이기 위한 분석 보고서를 작성해야 합니다.

# 1. 데이터 준비 : 데이터 구조 (Columns)
# [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]

# [고객ID, 방문횟수, 체류시간, 장바구니횟수, 구매금액]


# 2. 프로젝트 단계별 미션
# Step 1: 데이터 기초 통계 분석
# 전체 데이터에서 구매 금액(마지막 열)만 추출하여 sales 배열을 만드세요.

# 고객들의 평균 구매 금액과 총 매출액을 계산하여 출력하세요.


# Step 2: 충성 고객 필터링 (Boolean Indexing)
# 방문 횟수(1번 열)가 20회 이상이거나 구매 금액이 2000달러 이상인 고객을 '충성 고객'으로 분류하
# 세요.

# 충성 고객들의 ID를 추출하여 출력하세요.


# Step 3: 구매 전환율 및 효율성 계산 (Broadcasting)
# 구매금액 / 방문횟수를 계산하여 방문당 평균 매출(ARPV) 배열을 생성하세요.

# ARPV가 가장 높은 고객의 ID를 출력하세요.


# Step 4: 휴면 고객 및 이탈 위험군 식별 (Logic)
# 방문 횟수가 3회 이하이면서 장바구니에 담은 횟수가 1회 이하인 고객을 '이탈 위험 고객'으로 분류합
# 니다.

# 이 조건에 해당하는 고객들의 데이터를 추출하고, 전체에서 몇 명인지 출력하세요.


# Step 5: 고객 등급 정규화 및 VVIP 선정 (Normalization)
# 구매 금액 데이터를 0과 1 사이의 값으로 정규화(Min-Max Scaling) 하세요.

# 정규화된 값이 0.9 이상인 고객을 'VVIP'로 정의하고, 해당 고객들의 모든 정보(Row 전체)를 출력하
# 세요.

# 샘플 데이터 : 다운로드 , 
# https://drive.google.com/file/d/1SqzLBPZufZQpl-N39-9mE_zmQ_Dx_9DA/view?usp=sharing
# 샘플 데이터 넘파이 배열에 대입 코드 참고

# import numpy as np


# # CSV 파일 로드 (헤더 제외, 콤마 구분)

# data = np.genfromtxt('./customer_purchase_data.csv', delimiter=',', skip_header=1)

# # 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]

# print(f"데이터 형태: {data.shape}")

import numpy as np

# 1. .csv(,쉼표로 구분한 자료의 형식) 파일 가져오기
# data = np.genfromtxt("파일경로", delimiter = '구분문자', skip_header = 제외할헤더(행)수)
data = np.genfromtxt('./day11/종합예제/customer_purchase_data.csv', delimiter=',', skip_header=1)

# 2. 가져온 데이터의 넘파이 형식 확인
print(data.shape)

# 3. Step 1: 데이터 기초 통계 분석
sales = data[:, -1]
print(np.mean(sales))
print(np.sum(sales))

# 4. Step 2: 충성 고객 필터링 (Boolean Indexing)
a = (data[:, 1] >= 20) | (data[:, 4] >= 2000)
id = data[a, 0]
print(id)

# 5. Step 3: 구매 전환율 및 효율성 계산 (Broadcasting)
b = data[:, 4] / data[:, 1]
max_id = np.argmax(b)
print(data[max_id, 0])

# 6. Step 4: 휴면 고객 및 이탈 위험군 식별 (Logic)
c = (data[:, 1] <= 3) & (data[:, 3] <= 1)
c_id = data[c]
print(len(c_id)) # print(np.sum(c))

# 7. Step 5: 고객 등급 정규화 및 VVIP 선정 (Normalization)
d = (sales - np.min(sales) / (np.max(sales) - np.min(sales)))
vvip = d >= 0.9
print(data[vvip])