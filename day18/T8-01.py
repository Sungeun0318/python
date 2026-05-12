
# FastAPI : 파이썬 웹 프로그래밍
# RESTAPI, API 문서자동, 
# 사용처 : 데이터분석, AI모델(머신러닝/딥러닝) 서버

# 설치 : pip install "fastapi[standard]"

# import : import uvicorn
import uvicorn                  # 파이썬 서버(8000) # 자바의 톰캣 역할
from fastapi import FastAPI     # REST정의        # 자바의 SPRINGWEB 역할

# app 객체 생성
app = FastAPI()

# 모듈(.py) 실행 시작점
if __name__ == "__main__":
    uvicorn.run("T8-01:app", host="127.0.0.1", port=8000, reload=True)
