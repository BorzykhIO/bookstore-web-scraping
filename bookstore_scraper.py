from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd


titles, prices, rating, stock = [], [], [], []                                          #lists of books info
ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four' : 4, 'Five': 5}                       #dict for converting words to int
books_lst = {'name':titles, 'price': prices, 'rating':rating, 'in_stock':stock}         #dict to store info

path = 'C:\Program Files (x86)\chromedriver.exe'                                        #locating chrome web-driver
driver = webdriver.Chrome(path)
driver.get('https://books.toscrape.com/')                                               #URL of the online-store
driver.implicitly_wait(10)                                                              #waiting for the website to load

total_pages =  int(driver.find_element(By.XPATH, "//li[@class='current']").text[-2:])   #getting total pages number

for page in range(1, total_pages):                                                      #cycling throgh all pages
    html = BeautifulSoup(driver.page_source, 'html.parser')                             #getting page source code using BS4
    books = html.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})       #getting list containing books info

    for book in books:                                                                  #cycling through all the books on the page
        titles.append(book.find('h3').find('a').get('title'))                           #getting book title
        prices.append(book.find("p", {"class": "price_color"}).string)                  #getting book price
        rating.append(ratings[book.find('p').get('class')[1]])                          #getting book rating
        stock_ = book.find(class_='instock availability').text.strip()                  #getting stock availability
        stock.append(stock_)

    next_page = driver.find_element(By.XPATH, "//a[contains(text(), 'next')]")
    next_page.click()                                                                   #going to the next page


df = pd.DataFrame(data = books_lst)                                                     #converting dict into a pandas dataframe
df.to_excel('books.xlsx')                                                               #creating an excel file
