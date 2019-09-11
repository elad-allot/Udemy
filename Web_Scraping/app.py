from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simp_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_titile():
    h1_tag = simp_soup.find('h1')
    print(h1_tag)

def find_list_items():
    li_tag = simp_soup.find_all('li')
    list_content = [i.string for i in li_tag]
    return list_content

def find_att(att_name):
    paragraph = simp_soup.find_all('p', att_name)
    print(paragraph)
    # pass

def find_other_p():
    paragraph = simp_soup.find_all('p')
    other_p = [p for p in paragraph if 'subtitle' not in p.attrs.get('class', [])]
    # for i in p:
    #     print(i.attrs)
    print("p:")
    print(other_p)
    # print(paragraph)


print(find_list_items())
find_att({'class': 'subtitle'})
find_other_p()