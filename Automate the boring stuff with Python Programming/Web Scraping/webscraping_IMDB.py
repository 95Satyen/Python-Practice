# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 02:15:52 2020

@author: satye
"""
import bs4, requests
#res=requests.get('https://www.imdb.com/title/tt6751668/?ref_=fn_al_tt_1')
#
#res.raise_for_status()
#
#soup= bs4.BeautifulSoup(res.text,'html.parser')
#sp = soup.select('#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span')
#print(sp[0].text)

def getImdbRating(movieURL):
    res = requests.get(movieURL)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span')
    return elems[0].text.strip()

ratings = getImdbRating('https://www.imdb.com/title/tt6751668/?ref_=fn_al_tt_1')
print('The rating is ' + ratings)