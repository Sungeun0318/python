
# 서비스 : 스프링에서도 서비스는 HTTP 매핑
import pandas as pd
import httpx # HTTP 통신

class ProductService : 
    def __init__(self):
        self.df = pd.DataFrame([
            {'id' : 1, 'name' : '콜라', 'price' : 1000},
            {'id' : 2, 'name' : '사이다', 'price' : 1500}
        ])
        
    # 7. 서비스 함수
    def products(self) :
        return self.df.to_dict(orient='records')
    
    # 8. 외부 서버(API 또는 스프링)와 통신하기
    # httpx.AsyncClient() vs axios()
    async def getSpring(self) :
        async with httpx.AsyncClient() as client :
            response = await client.get("http://localhost:8080/api/product") # 통신할 스프링 주소 
            print(response)
            return response.json()
        
ProductService = ProductService() # 서비스 객체 생성
