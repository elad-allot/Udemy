import requests
from pages.qoutes_page import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content

page = QuotesPage(page_content)
print("line 7")
# print(page.tags)
# for q in page.quotes:
#     print(q.content)

# print(page.tags)

print("line 15")
# print
for t in page.tags:
    print(t)
