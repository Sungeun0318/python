
import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

# [1] T5_data.json 파일내 'patient_status_data'
with open('./T5_data.json', 'r', encoding='utf-8') as json_file :
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['patient_status_data'])

print(df)

# [2] 막대차트 : 상태별 환자수 비교


# [3] 원형차트 : 전체대비 각 상태의 환자수 비율

