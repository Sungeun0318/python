
# 서비스 : 스프링에서도 서비스는 HTTP 매핑
import pandas as pd

class ProductService : 
    def __init__(self):
        self.df = pd.DataFrame([
            {'id' : 1, 'name' : '콜라', 'price' : 1000},
            {'id' : 2, 'name' : '사이다', 'price' : 1500}
        ])
        
    # 7. 서비스 함수
    def products(self) :
        return self.df.to_dict(orient='records')
        
ProductService = ProductService() # 서비스 객체 생성