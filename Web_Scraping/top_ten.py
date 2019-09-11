from bs4 import BeautifulSoup

ITEM_HTML = """<div class="col-md-4 tags-box">
        
            <h2>Top Ten tags</h2>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 28px" href="/tag/love/">love</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 26px" href="/tag/inspirational/">inspirational</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 26px" href="/tag/life/">life</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 24px" href="/tag/humor/">humor</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 22px" href="/tag/books/">books</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 14px" href="/tag/reading/">reading</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 10px" href="/tag/friendship/">friendship</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 8px" href="/tag/friends/">friends</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 8px" href="/tag/truth/">truth</a>
            </span>
            
            <span class="tag-item">
            <a class="tag" style="font-size: 6px" href="/tag/simile/">simile</a>
            </span>
            
        
    </div>"""

soup = BeautifulSoup(ITEM_HTML, 'html.parser')

locator = 'a.tag'
tags = soup.select(locator)

# print(dir(soup.select(locator)))

for tag in tags:
    print(tag.string)
    print(tag.attrs['style'])
