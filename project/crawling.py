import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# url = 'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber=120&pageSize=120'

book_list = []
for page in range(1, 10) :
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}&pageSize=120'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select('#yesBestList > li')
   
   # 제목 : .gd_name
   # 가격 : .yes_b
   # 판매 지수 : .saleNum
   # 출판년월 : .authPub info_date
   
    for book in books :  
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        saleNum = book.select_one('.saleNum').get_text().strip()
        info_date = book.select_one('.authPub.info_date').get_text().strip()
        book_list.append({"제목" : gd_name, "가격" : yes_b, "판매지수" : saleNum, "출판년월" : info_date})

    time.sleep(2)
    

df = pd.DataFrame(book_list)
print(df)

import os

if not os.path.exists('project/data') :
    os.makedirs('project/data')
    
df.to_csv('project/data/books.csv', index=False, encoding='utf-8')
print('csv 저장 완')