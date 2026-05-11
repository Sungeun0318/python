
# 동적페이지 크롤링
# 웹페이지 자료가 대기 상태 / 이벤트가 있는 경우(JS통신 AXIOS)

# [1] 설치
# pip install playwright # 파이썬 라이브러리
# playwright install     # 브라우저 설치

# [2] 라이브러리
import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright # 동적웹페이지 크롤링
import pandas as pd

# [3] 크롤링 주소
# 주소 : https://search.naver.com/search.naver?where=image&query=짱구
# 박스 : tile_item, 이미지 : _fe_image_tab_content_thumbnail_image, 제목 : info_title

# [4] 비동기 웹크롤링
async def naverRun() : # 동기화된 함수
    # (1) playwright 실행하기
    async with async_playwright() as p : #
        # (2) await(대기) 상태 이용한 크롬 실행, await.chromium.launch()
        # headless = False : 브라우저가 직접 실행된다. <봇차단 방지>
        browser = await p.chromium.launch(headless=False)
        
        # (3) 실행된 브라우저(chromium)에서 새로운 페이지에 지정한 URL 대입하여 이동
        url = "https://search.naver.com/search.naver?where=image&query=짱구" # url
        page = await browser.new_page()                                     # 새로운 페이지 탭) 열기
        await page.goto(url)
    
asyncio.run(naverRun()) # 동기화된 함수 실행