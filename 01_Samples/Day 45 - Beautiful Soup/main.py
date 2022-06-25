from bs4 import BeautifulSoup
import requests
# try:
#     with open("website.html", encoding="utf8") as web:
#         contents = web.read()
# except UnicodeError as e:
#     print(e)
# else:
#     soup = BeautifulSoup(contents, 'html.parser')
#     # print(soup.title)
#     print(soup.title.string)
#     all_para_tags = soup.findAll(name="p")
#     for tag in all_para_tags:
#         print(tag.getText())
#
#     section_heading = soup.find(name="h3", class_="heading")
#     print(section_heading.getText())
#
#     company_url = soup.select_one(selector="p a")
#     print(company_url)
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
story_tags = soup.find_all(name="a", class_="titlelink")
story_texts = []
story_links = []

for tag in story_tags:
    story_text = tag.getText()
    story_texts.append(story_text)
    story_link = tag.get("href")
    story_links.append(story_link)
story_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(story_texts)
# print(story_links)
# print(story_scores)
ind = story_scores.index(max(story_scores))
print(story_texts[ind], story_links[ind], story_scores[ind])