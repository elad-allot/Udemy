import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_itme_name():
    locator = 'article.product_pod h3 a'  # css locator
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']
    return item_name


def find_att_by_css_locator(css_locator, att):
    item_link = soup.select_one(css_locator)
    item_name = item_link.attrs[att]
    return item_name


print(find_itme_name())
print(find_att_by_css_locator('html body li article h3 a', 'href'))
# print(find_att_by_css_locator('html body li article.product_pod div.price_color p', 'price_color'))

locator = 'html body li article div p'  # css locator
item_price = float(soup.select_one(locator).string[1:])


print(item_price)