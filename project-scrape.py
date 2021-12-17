import requests as req
from bs4 import BeautifulSoup as bs

# Access the Home page to get all the Book's links
home_page = req.get("http://www.konkanibible.org/index.html")

soup = bs(home_page.content, 'html.parser')

# This includes all the tags and href's required for scraping
books = list(soup.children)[26]
tag = books.findAll("a", href = True)
tag = tag[1:]

# Separating The links and creating a list to parse through 
book_links = list()
for i in tag:
    link = str(i['href'])
    if('updated' not in link and "http" in link):
        book_links.append(str(i['href']))

book_no = 0
chap_no = 0

# The main for loop
while(book_no < len(book_links)):
    book_page = req.get(book_links[book_no])
    book_soup = bs(book_page.content, 'html.parser')
    content = book_soup.findAll('a', href = True)
    chapter_links = []
    for i in content:
        link = str(i['href'])
        if('Chapter' in link):
            chapter_links.append(book_links[book_no] + '/' + i['href'])

    book = open("book" + str(book_no), "w")
    chapter_text = ''
    while(chap_no < len(chapter_links)):
        chapter_content = req.get(chapter_links[chap_no])
        chapter_soup = bs(chapter_content.content, 'html.parser')
        for i in chapter_soup.find_all('p'):
            chapter_text += i.get_text()
        chap_no += 1
    book.write(chapter_text)
    book_no += 1
    book.close()
    
# html_file.write(soup.prettify())
# html_file.close()