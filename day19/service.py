import pandas as pd

# 서비스 클래스
class ItemService :
    
    def __init__(self):
        self.df = pd.DataFrame([
            {'id' : 1, 'name' : '콜라', 'price' : 1000},
            {'id' : 2, 'name' : '사이다', 'price' : 1500}
        ])
        
    # 함수
    
    # (1) 개별조회 서비스
    def item(self, id) :
        