
import uvicorn
from fastapi import FastAPI

# 2. fastApi 객체생성
app = FastAPI()

# 3. 서버 실행
if __name__ == "__main__" :
    uvicorn.run("T8-02:app", host= "127.0.0.1", port=8000, reload=True)    
    
# 4. REST 정의하기
# REST : 자원 주고 받는 상태 구조
# REST API : 자원 주고 받는 상태 구조조 # REST API : HTTP로 REST 구현
# @GetMapping("/URL") vs @app.get("/URL")

@app.get("/")
async def index() :
    return "안녕 파이썬웹"