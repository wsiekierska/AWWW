from bs4 import BeautifulSoup
import requests
import markdownify
from duckduckgo_search import DDGS


response = requests.get('https://www.favikon.com/blog/the-20-most-famous-tiktok-influencers-in-the-world')
soup = BeautifulSoup(response.text, 'html.parser')

html_text = ''''''
page_title = soup.title
html_text += "# " + page_title.string + "\n\n"

all_paragraphs = [p.text for p in soup.find_all('div')]
paragraphs = soup.find_all('li', class_="")
i = 1
for p in paragraphs:
    html_inside = "### " + p.string + "\n\n"
    name = p.a['href']
    anchor_element = soup.find('a', {'name': name[1:]})
    paragraphs_below = anchor_element.find_all_next('p')
    divs_below = anchor_element.find_all_next('div')
    links_below = anchor_element.find_all_next('a')
    text_do_display = paragraphs_below[1].text
    video_link = ''''''
    video_link += divs_below[0].prettify()
    html_inside += "#### Description:"+ "\n\n"
    html_inside += text_do_display + "\n\n"
    tiktoker=p.string[3:p.string.rfind("-")-1]

    results = DDGS().images(
        keywords=tiktoker,
        region="wt-wt",
        safesearch="off",
        size=None,
        type_image=None,
        layout=None,
        license_image=None,
        max_results=100,
    )

    html_inside += "#### Tiktok link:" + "\n\n"
    if divs_below[0].find_all('blockquote'):
        html_inside += video_link + "\n\n"
    else:
        html_inside += links_below[0]['href']+"\n\n"

    j = 0
    html_inside += "#### Photos:" + "\n\n"
    for res in results:
        if j > 3:
            break
        else:
            html_inside += f'![Alt text]({res["image"]} "a title") \n\n'
            j+=1

    markdown_s = markdownify.markdownify(html_inside, heading_style='ATX')
    with open(name[1:] + ".md", 'w') as f:
        f.write(markdown_s)
    html_text += "#### [" + p.string + "]" + "(" + name[1:] + ".md) \n\n"

markdown_string = markdownify.markdownify(html_text, heading_style='ATX')
with open('my_page.md', 'w') as f:
    f.write(markdown_string)
