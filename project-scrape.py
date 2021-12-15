import requests as req
from bs4 import BeautifulSoup as bs


page = req.get("http://www.konkanibible.org/index.html")
# html_file = open("html_test.txt", "w")

soup = bs(page.content, 'html.parser')

# This includes all the information and href's required for scraping
print(list(soup.children)[26])


# html_file.write(soup.prettify())
# html_file.close()