#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:32:38 2023

@author: ertugruloney
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

from lxml import etree
import re
from urllib.request import urlopen

import pandas as pd
import xlwings as xw

def AmazonGetirme(Url):
        
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    Url = Url
    while True:
        webpage = requests.get(Url, headers=headers)
        soup = BeautifulSoup(webpage.content, "html.parser")
        Stext = str(soup)
        if len(Stext)>50000:
            break
    
    # %%
    Rows=[]
    dom = etree.HTML(str(soup))
    ao = ""
    for i in dom.xpath('//*[@id="bylineInfo"]/span/a'):
        ao += ' ' + i.text
    Name = dom.xpath(' //*[@id="productTitle"]')[0].text
    
    
    #Tur = soup.findAll('span', attrs={'class': 'a-unordered-list a-nostyle a-vertical zg_hrsr'})
    Sayfa=soup.findAll('div',attrs={'class':'a-section a-spacing-none a-text-center rpi-attribute-value'})
    
    for count, i in  enumerate(Sayfa):
        if count==0:
            ID=i.text
        if count==7:
            Sayfa=i.text[1:4]
        if count==4:
            yayinT=i.text
        if count==3:
            yayinci=i.text
    Rate=soup.findAll('span',attrs={'class':'a-size-base a-color-base'})
    for count, i in  enumerate(Rate):
        if count==5:
           rate= i.text
    Rating=soup.findAll('span',attrs={'id':'acrCustomerReviewText'})
    for count, i in  enumerate(Rating):
        rating=i.text.split(' ')[0]
    
   
    Tur=soup.findAll('a',attrs={'class':'a-link-normal a-color-tertiary'})
    tur=""
    for count, i in  enumerate(Tur):
        if count>0:
            tur+=','
        for j in i.text.split(" "):
            if len(j)>0:
                tur+=j
            
        
    Row=[Url,"",tur,ID,Name,Sayfa,ao,yayinT,yayinci,"",rate,rating,"","","","","","","","","","","","","","","","","",
          "","","",""]
    return Row
if __name__ == "__main__":
    result=AmazonGetirme('https://www.amazon.com.tr/Hayvan-%C3%87iftli%C4%9Fi-George-Orwell/dp/9750719387/ref=sr_1_1?pf_rd_i=12466381031&pf_rd_m=A1UNQM1SR2CHM&pf_rd_p=5f0edf8a-d874-4433-a6ea-34a186ff3c12&pf_rd_r=S3EZ4GC0PS3PSJXDC4AD&pf_rd_s=merchandised-search-4&qid=1695206431&refinements=p_27%3AGeorge+Orwell&s=books&sr=1-1')