import numpy as np

# Phase 2: NumPy를 이용한 5개 이상 미션 수행
# Step 1: 유지취업률 우수 학과 분석 (Statistics & Boolean Indexing)
# 미션: 대학/학과별 유지취업률 추이를 확인하고, 유지취업률이 90% 이상인 학교/학과를 추출하세요.
# 분석 결과: 유지취업률 90% 이상 학교/학과 수 (                ) 개  ,  대표 학교/학과: (                )
# 의미: 단순히 취업에 성공한 것뿐만 아니라, 취업 상태를 안정적으로 유지하고 있는 학교/학과를 파악할 수 있습니다. 유지취업률이 높은 학과는 취업의 질이나 직무 적합도가 상대적으로 높다고 해석할 수 있습니다.
data = np.genfromtxt('./day11/탐구보고서/data.csv', delimiter=',', skip_header=1, encoding='utf-8', dtype=str)
print(data.shape)
print(data)


# Step 1
school = data[:, 1] # 학제 -> 대학만 가능하게 함
university = data[:, 2] # 대학
department = data[:, 13] # 학과
print(department)
print(university)
retention_rate = data[:, -6].astype(float) # 4차 유지 취업률
print(retention_rate)
employment_4rate = np.sum(retention_rate >= 30) # 유지취업률 90퍼 이상
print("유지취업률 90% 이상 학교/학과 수 : ", employment_4rate)
employment_max = np.argmax(retention_rate) # 유지 취업률 제일 높은 곳
print("대표 학교/학과 : ", data[employment_max, 2], "/", data[employment_max, 13])

# Step 2: 취업률 상위 학교/학과 분석 (Boolean Indexing & Sorting)
# 미션: 졸업자 수 또는 취업대상자 수가 30명 이상인 학과를 기준으로, 취업률이 가장 높은 학교/학과를 찾으세요.  
# 분석 결과: 취업률 1위 학교/학과 (                )  ,  취업률: (                ) %
# 의미: 일정 규모 이상인 학과 중 실제 취업 성과가 가장 우수한 학교/학과를 확인합니다. 표본 수가 너무 적은 학과를 제외함으로써, 보다 신뢰도 높은 취업률 비교가 가능합니다.
graduates = data[:, 15].astype(float)  # 졸업자 수
employment_rate = data[:, 18].astype(float) # 취업률 
print(graduates)
print(employment_rate)

a = (graduates >= 30) & (school == '대학') # 30
b = data[a] # 학교/학과 조건의 맞는 행
c = employment_rate[a] # 취업률 행

c_max = np.argmax(c) # 가장 높은 취업률 
print(b)
print(c_max)
print("취업률 1위 학교/학과 : ", b[c_max, 2], b[c_max, 13])
print("취업률 : ", f"{c[c_max]}%")

# Step 3: 취업률 하위 학교/학과 분석 (Boolean Indexing & Sorting)
# 미션: 졸업자 수 또는 취업대상자 수가 30명 이상인 학과를 기준으로, 취업률이 가장 낮은 학교/학과를 찾으세요.
# 분석 결과: 취업률 최하위 학교/학과 (                )  ,  취업률: (                ) %
# 의미: 취업 성과가 상대적으로 낮은 학교/학과를 파악하여, 취업 지원 프로그램이나 진로 상담이 우선적으로 필요한 대상을 찾을 수 있습니다.

c_min = np.argmin(c) # 가장 낮은 취업률 
print("취업률 최하위 학교/학과 : ", b[c_min, 2], b[c_min, 13])
print("취업률 : ", f"{c[c_min]}%")


# Step 4: 진학률 상위 학교/학과 분석 (Statistics & Sorting)
# 미션: 대학원 진학 등 취업 대신 학업을 이어가는 비율이 높은 학교/학과를 찾기 위해, 진학률이 가장 높은 학교/학과를 추출하세요. 
# 분석 결과: 진학률 1위 학교/학과 (                )  ,  진학률: (                ) %
# 의미: 해당 학과의 학생들이 취업보다 학업 연장이나 전문성 강화를 선택하는 경향이 강한지 확인할 수 있습니다. 진학률이 높은 학과는 연구직, 전문직, 대학원 진학과 관련된 진로 특성이 강할 가능성이 있습니다.

is_upper_30 = data[:, 15].astype(int) >= 30 # '졸업자_계'가 30명 이상인지
is_university = data[:, 1] == "대학"
upper_30 = data[is_upper_30 & is_university] # '졸업자_계'가 30명 이상, "대학"인 행


jinhak_rate = upper_30[:, 45].astype(float)
max_index = np.argmax(jinhak_rate)
print('학교/학과명 : ', upper_30[max_index, 2] + ' ' + upper_30[max_index, 13], '|| 진학률 : ', jinhak_rate[max_index])



# Step 5: 취업준비생 비율 분석 (Broadcasting & Ratio Calculation)
# 미션: 졸업자 수에서 취업자 수, 진학자 수, 취업불가능자 수를 제외하여 취업준비생 수를 계산하고, 취업준비생 비율이 가장 높은 학과를 찾으세요. (취업준비생 수 = 졸업자 수 - 취업자 수 - 진학자 수 - 취업불가능자 수)
# 분석 결과: 취업준비생 비율이 가장 높은 학교/학과 (                )  ,  취업준비생 비율: (                ) %
# 의미: 졸업 후 취업도, 진학도 하지 않은 학생의 비율을 확인하여 실질적인 취업 지원이 필요한 학과를 찾을 수 있습니다. 이 비율이 높은 학과는 취업 준비 장기화, 진로 미결정, 취업 지원 부족 등의 문제가 있을 가능성이 있습니다.

graduate = upper_30[:, 15].astype(int) # upper_30 행들의 졸업생 수
employed = upper_30[:, 21].astype(int) # upper_30 행들의 취업자 수
student = upper_30[:, 48].astype(int) # upper_30 행들의 진학자 수
enlistee = upper_30[:, 51].astype(int) # upper_30 행들의 입대자 수
impossible = upper_30[:, 52].astype(int) # upper_30 행들의 취업불가능자 수
foreigner = upper_30[:, 55].astype(int) # upper_30 행들의 외국인유학생 수
excluded = upper_30[:, 58].astype(int) # upper_30 행들의 제외인정자 수
etc = upper_30[:, 52].astype(int) # upper_30 행들의 기타 수
unknown = upper_30[:, 52].astype(int) # upper_30 행들의 미상 수


job_seeker = graduate - employed - student - enlistee - impossible - foreigner - excluded - etc - unknown
job_seeker_percentage = job_seeker / graduate


baeksu = upper_30[job_seeker_percentage > 0.7]
baeksu_univ = baeksu[:,2]
baeksu_dept = baeksu[:,13]
baeksu_percentage = job_seeker_percentage[job_seeker_percentage > 0.7]


baeksu_grad = graduate[job_seeker_percentage > 0.7]
baeksu_js = job_seeker[job_seeker_percentage > 0.7]


print("[취업준비생 비율이 70% 이상인 학교/학과]")
for i in range(len(baeksu_dept)):
   print(f"{baeksu_univ[i]} {baeksu_dept[i]} || 비율 : {baeksu_percentage[i] * 100:.2f}% || 졸업자 수 : {baeksu_grad[i]}명 || 취업준비생 수 : {baeksu_js[i]}명")