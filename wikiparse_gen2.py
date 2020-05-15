# ===========================================================
# NAME: Wikipedia Unusual Articles- Wikiparse
# BY: Toby Tang 
# DATE: MAY 14, 2020
#
# Written in Python, the algorithm accesses the web to import 
# the Wikipedia Unusual Articles page in HTML using the requests 
# library. The HTML data can then be parsed using the BeautifulSoup 
# library to obtain a list of articles. This list is only generated 
# once upon start up, not each time the bot is called. This is done 
# to minimize bot response time. A random python function is then 
# used to select an article. The chosen article will then be parsed 
# one last time to obtain the title, description and link. 
# 
# Discord bot link: https://top.gg/bot/704890634984751126
# Github: https://github.com/Toby-Tang/DiscordBot-WikiFact
# ===========================================================

import requests
import random
from bs4 import BeautifulSoup


def article_compiler():
    #With internet access 
    URL = 'https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_articles = []

    #with downloaded html file
    #with open("Wikipedia_Unusual.html", encoding="utf-8") as f:
    #    data = f.read()
    #    soup = BeautifulSoup(data, 'html.parser')


    #Find content section
    content = soup.find(id='content')
    #Find all the tables
    wikitables = content.find_all('table', class_='wikitable')
    #Find all the articles
    for table_elems in wikitables:
        list_articles.extend(table_elems.find_all('tr'))

    print(f'Article list length: {len(list_articles)}')
    #return compiled list
    return(list_articles)



def WikiFact(article_elems):
    #choose a random article
    article = random.choice(article_elems)
    #find all the table cells of the article
    td_elems = article.find_all('td')

    #DEV_NOTE: started from last cell because
    #some articles have 3 cells with a unique first cell. eg flags

    #last cell is always the comment
    comment = td_elems[-1]
    #second last cell is always the title w/ link
    title_elem = td_elems[-2]
            #acquire text from <b></b>
    title = title_elem.find('b')
            #acquire link from <a></a>
    link = title_elem.find('a')['href']

    # print(title.text.strip())
    # print(comment.text.strip())
    # print(f"https://en.wikipedia.org{link}\n")

    p_title = (title.text.strip())
    p_comment = (comment.text.strip())
    p_link = (f"https://en.wikipedia.org{link}\n") #remove https://en.wikipedia.org if pasring from html file
    return p_title,p_comment,p_link
