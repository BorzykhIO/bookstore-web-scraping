# Book store web-scraper
This Python script scrapes products data from [a fictional bookstore](http://books.toscrape.com/).

## Python libraries used:
- BeautifulSoup4
- Selenium
- Pandas

![books.toscrape.com](https://media.geeksforgeeks.org/wp-content/uploads/20200626163350/website2-1024x559.png)

## Data:
- Title
- Price
- Rating
- Stock availability

## Scraping algorithm:
1. Creating a dictionary to store the data;
2. Initializing the web driver;
3. Getting total pages number;
4. Getting the element (books) that contains data of all books on the page;
5. Iterating through all book elements and scraping book info;
6. Iterting through all pages;
7. Converting the dict to a pandas dataframe;
8. Converting the pandas dataframe to an Excel file.

## Excel file containing the scraped data:
![excel file](https://i.imgur.com/rQ9XmfU.png)

