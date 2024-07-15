import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com",
    "Connection": "keep-alive"
}

url = "https://books.toscrape.com/catalogue/page-2.html"

# Make a request with the defined headers
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')\

books_name=[book_title for book in books ]
prices_name=[book_price for book in books]

data={
    "Book_name":books_name,
    "Price_name":prices_name
}

df=pd.DataFrame(data)
excel_filename = "books.xlsx"
df.to_excel(excel_filename, index=False)

# Extract the title of the page

books = soup.select('article.product_pod')
for book in books:
    book_title = book.select_one('h3 > a')['title']
    book_price = book.select_one('p.price_color').text
    print(f"Title: {book_title}, Price: {book_price}")


s=random.uniform(1,3)
print(f"Sleep time :{s:.2f} seconds")
time.sleep(s)
