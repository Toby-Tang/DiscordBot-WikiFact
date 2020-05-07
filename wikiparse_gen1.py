# ===========================================================
# NAME: Wikipedia Unusual Articles- Webscrapper
# BY: Toby Tang 
# DATE: MAY 2, 2020
#
# -Scrapes website for tables containing articles
# and returns random article with name, link and comment
# ===========================================================

import requests
import random
from bs4 import BeautifulSoup

def WikiFact():
    #With internet access 
    URL = 'https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Find content section
    content = soup.find(id='content')
    #Find all the tables
    wikitables = content.find_all('table', class_='wikitable')

    #choose a random table
    table_elems = random.choice(wikitables)
        #find all articles within this table
    article_elems = table_elems.find_all('tr') 

    # #choose a random article
    article = random.choice(article_elems)
        #find all the table cells of the article
    td_elems = article.find_all('td')
    ##print(article)

    #DEV_NOTE: had to start from last cells because
    #some tables have 3 cells with unique first cell. eg flags.

        #last cell is always the comment
    comment = td_elems[-1]
        #second last cell is always the title w/ link
    title_elem = td_elems[-2]
            #acquire text from <b></b>
    title = title_elem.find('b')
            #acquire link from <a></a>
    link = title_elem.find('a')['href']

    print(title.text.strip())
    print(comment.text.strip())
    print(f"https://en.wikipedia.org{link}\n")

    p_title = (title.text.strip())
    p_comment = (comment.text.strip())
    p_link = (f"https://en.wikipedia.org{link}\n")
    return p_title,p_comment,p_link
