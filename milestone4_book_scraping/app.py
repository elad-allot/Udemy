import requests
from pages.elements import PageElements




def get_books_from_page(url):
    page_content = requests.get(url).content
    page = PageElements(page_content, url)
    books = page.book_product
    return [b for b in books if b.price < 20 and b.rating > 3]


url = 'http://books.toscrape.com/'

page_content = requests.get(url).content
page = PageElements(page_content, url)
cats = page.categorie_list

books = page.book_product
print([b for b in books])


cat_list = ([c for c in cats])
print("there are %s categories" % len(cat_list))
for c in cat_list:
    print(f'number of books in {c.category_name} category')
    print(get_books_from_page(c.cat_link))
