#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:11:00 2023

@author: ertugruloney
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:22:10 2023

@author: ertugruloney
"""

import sys

import time
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *



import threading


import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from lxml import etree
import re
from urllib.request import urlopen
from openpyxl import load_workbook
import pandas as pd
import threading
import time
import aiohttp
import asyncio
import time
import warnings

from aiohttp import ClientSession, ClientTimeout

import xlwings as xw

import nest_asyncio
nest_asyncio.apply()



class MainAs():
    # Create a counter thread
    change_value = pyqtSignal(float)
    def __init__(self,URLS):
        super().__init__()
     
       
        self.count2=0
        self.TURS=[]
        self.IDD=[]
        self.Edi=[]
        self.Sayfa=[]
        self.Dates=[]
        self.Rating=[]
        self.Rew=[]
        self.RateN=[]
        self.Kitapyurdu=[]
        self.Amazon=[]
        self.Dr=[]
        self.Alinks=[]
        self.Kdate=[]
        self.Marka=[]
        self.Names=[]
        self.Stats=[]
        self.Rows=[]
        self.Links=[]
        self.Linksa=URLS
        self.Linksa2=URLS
        self.result=[]
        self.Kayit=[]
        self.Rows2=[]
        self.Bos=[]
        
     
    
        #%%
        
        self.baslangic=0
        
     
    def run(self):
        print('deneme')
        self.Main()

    def monthToNum(self,shortMonth):
        return {
                'January': 1,
                'February': 2,
                'March': 3,
                'April': 4,
                'May': 5,
                'June': 6,
                'July': 7,
                'August': 8,
                'September': 9, 
                'October': 10,
                'November': 11,
                'December': 12
        }[shortMonth]
    
    
    

    
    async def yazma(self,Stext,URL):
        
          
            #%%turbulma
            if len(Stext)>100000:
              
                
            
                #MArka Bulma
                StextnewM=Stext
                x=StextnewM.find(""":{"__typename":"BookDetails""")
                StextnewM=StextnewM[x+27:]
                x=StextnewM.find("publisher")
            
                StextnewM=StextnewM[x+12:]
            
                x=StextnewM.find("isbn")
            
            
                StextnewM=StextnewM[:x-3]
                self.Marka.append(StextnewM)
                
                
                turs=[]
                Stext=Stext[3000:60000]
                Stextnew=Stext
                while True:
                    x=Stextnew.find("BookPageMetadataSection__genreButton")
                    if x<0:
                        break
                    Stextnew=Stextnew[x+36:]
                    x=Stextnew.find('class="Button__labelItem">')
                    
                    Stextnew=Stextnew[x+26:]
                    x=Stextnew.find('<')
                    turs.append(Stextnew[:x])
                self.TURS.append(turs)
                
                #kitap ismini bulma
                
                StextnewN=Stext
                x=StextnewN.find("""="og:description"/><title>""")
                StextnewN=StextnewN[x+26:]
                x=StextnewN.find(")")
                
                if x>150:
                        x=StextnewN.find("by")
                        self.Names.append(StextnewN[:x-1])
                else:
                    self.Names.append(StextnewN[:x+1])
                StextnewN=StextnewN[x+2:]
                x=StextnewN.find("|")
            
                
                
                
                idd=URL.split("/")
                self.IDD.append(idd[-1][:8])
                
                Stextnew2=Stext
                x=Stextnew2.find("""class="BookPageMetadataSection__contributor"><h3 aria-label="By:""")
                if x==-1:   
                
                   x=Stextnew2.find("""="og:description"/><title>""")
                   Stextnew2=Stextnew2[x+26:]
                   x=Stextnew2.find(")")
                   
                   if x>150:
                           x=Stextnew2.find("by")
                           
                   
                      
                   Stextnew2=Stextnew2[x+2:]
                   x=Stextnew2.find("|")
                   Stextnew2=Stextnew2[:x]
                   Stextor=Stextnew2[:x]
                   
                   if Stextor[0]==" ":
                       self.Edi.append(Stextor[1:])
                   else:
                       self.Edi.append(Stextor.replace('by ',''))
                    
                else:
                    Stextnew2=Stextnew2[x+65:]
                    x=Stextnew2.find("class")
                    Stextnew2=Stextnew2[:x-2]
                    
                    if Stextnew[0]==" ":
                        self.Edi.append(Stextnew2[1:])
                    else:
                        self.Edi.append(Stextnew2.replace('by ',''))
                #sayfa bulma
                Stextnew3=Stext
                x=Stextnew3.find("""FeaturedDetails""")
                Stextnew3=Stextnew3[x+46:]
                x=Stextnew3.find(" ")
                
                Stextnew3=Stextnew3[:x]
                try:
                    self.Sayfa.append(int(Stextnew3))
                except:
                    self.Sayfa.append(None)
                
                #yayınlşanma tarihi
                Stextnew3=Stext
                x=Stextnew3.find("""FeaturedDetails""")
                Stextnew3=Stextnew3[x+119:]
                x=Stextnew3.find("<")
                Stextnew3=Stextnew3[:x]
                S=Stextnew3.split()
                try:
                    gg=self.monthToNum(S[-3])
                    startdate=S[-2][0:2]+'.'+str(gg)+'.'+S[-1]
                    
                    self.Dates.append( startdate.replace(',',''))
                except:
                    self.Dates.append( None)
                
                #Rating
                Stextnew4=Stext
                x=Stextnew4.find("""RatingStatistics__rating""")
                Stextnew4=Stextnew4[x+26:]
                try:
                    self.Rating.append(float(Stextnew4[:3]))
                except:
                    self.Rating.append('Yok!')
                
                Stextnew5=Stext
                x=Stextnew5.find("""ratingsCount""")
                Stextnew5=Stextnew5[x+14:]
                x=Stextnew5.find("<")
                try:
                    self.RateN.append(float(Stextnew5[:x].replace(',',''))   )
                except:
                    self.RateN.append('Yok!')
                x=Stextnew5.find("""reviewsCount""")
                Stextnew5=Stextnew5[x+14:]
                x=Stextnew5.find("<")
                try:
                    
                    self.Rew.append(float(Stextnew5[:x].replace(',','')))
                except:
                    self.Rew.append('Yok')
                
                self.Stats.append('https://www.goodreads.com/book/stats?utf8=%E2%9C%93&id='+idd[-1][7])
                
                from datetime import date
                
                today = date.today()
                self.Kdate.append(today)
                
                
                self.Alinks.append('https://www.goodreads.com/book_link/follow/1?book_id='+idd[-1]+'source=compareprices')
                
                
                URLkitap='https://www.kitapyurdu.com/index.php?route=product/search&filter_name='
                URLkitap=URLkitap+Stextnew2
                page = requests.get(URLkitap)
                soup = BeautifulSoup(page.content, 'html.parser')
                Ky=soup.findAll("div",{"class":"name ellipsis"})
                
                if len(Ky)!=0:
                    self.Kitapyurdu.append(URLkitap)
                else:
                    self.Kitapyurdu.append('Yok!')
                    
                    
                URLdr1='https://www.dr.com.tr/search?q='
                URLdr2='&ShowNotForSale=false&redirect=search'
                URldr=URLdr1+Stextnew2+URLdr2
                
                page = requests.get(URldr)
                soup = BeautifulSoup(page.content, 'html.parser')
                DRs=soup.findAll("a",{"class":"prd-name js-search-prd-item"})
                if len(DRs)!=0:
                    self.Dr.append(URldr)
                else:
                    self.Dr.append('Yok!')
                Turr=''
                count2=len(self.Dr)-1
           
                for t in self.TURS[count2]:
                    Turr=Turr+t+', '
             
                self.Rows.append((URL,'',Turr,self.IDD[count2],self.Names[count2],self.Sayfa[count2],self.Edi[count2],self.Dates[count2],self.Marka[count2],self.Stats[count2],self.Rating[count2],self.RateN[count2],self.Rew[count2],str(self.Kdate[count2]),None,None,self.Kitapyurdu[count2],self.Dr[count2],
                             None,None,None,None, None,None,None,None, None,0,0,0,None,None,None,self.Alinks[count2]))
                self.Rows2.append((URL,'',Turr,self.IDD[count2],self.Names[count2],self.Sayfa[count2],self.Edi[count2],self.Dates[count2],self.Marka[count2],self.Stats[count2],self.Rating[count2],self.RateN[count2],self.Rew[count2],str(self.Kdate[count2]),None,None,self.Kitapyurdu[count2],self.Dr[count2],
                             None,None,None,None, None,None,None,None, None,0,0,0,None,None,None,self.Alinks[count2]))
                dasAS=self.Rows
                self.count2+=1
                print(self.count2+1)
            else:
                self.Bos.append(URL)
           
    async def scrape(self,url):
    
        conn = aiohttp.TCPConnector()
        timeout = ClientTimeout(total=500)
        async with aiohttp.ClientSession(connector=conn,timeout=timeout,trust_env=True) as session:
           async with session.get(url) as resp:
               body = await resp.text()
               soup = BeautifulSoup(body, 'html.parser')
               Stext=str(soup)
               try:
                   await self.yazma(Stext,url)
               except (aiohttp.ServerDisconnectedError, aiohttp.ClientResponseError,aiohttp.ClientConnectorError) as s:
                    print("Oops, the server connection was dropped on ", url, ": ", s)
                    # don't hammer the server
               
    async def main(self):
        
        start_time = time.time()
        tasks = []
        if len(self.Linksa)<=250:
            for urlll in self.Linksa:
                task = asyncio.create_task(self.scrape(urlll))
                tasks.append(task)
        else:
            for urlll in self.Linksa[:250]:
                task = asyncio.create_task(self.scrape(urlll))
                tasks.append(task)
    
        print('Saving the output of extracted information')
        await asyncio.gather(*tasks)
        
        time_difference = time.time() - start_time
        print(f'Scraping time: %.2f seconds.' % time_difference)
        
        
    def Main(self):
       durum=0
       try:
           
           loop = asyncio.get_event_loop()
           loop.run_until_complete(self.main())
           if len(self.Linksa)>250:
               self.result.append(self.Rows)
               self.Rows=[]
               self.Main()
       except:
           if len(self.Rows)>0:
               self.result.append(self.Rows)
               
              
           durum=1
           Links2=[]
           for i in self.Linksa2:
               durum2=0
               for j in self.Rows2:
                   if i==j[0]:
                       durum2=1
                       break
               if durum2==0:
                   for k in self.Bos:
                       if k==j[0]:
                           durum2=1
                           break
               if durum2==0:
                   Links2.append(i)
           self.Linksa=Links2.copy() 
           self.Rows=[]
           self.Main()
       
      

       if durum==0:
           
           
       
         
        
            
            self.result.append(self.Rows)
       return self.result    
       
          

    
if __name__ == "__main__":
 Url=['https://www.goodreads.com/book/show/54369251-a-wizard-s-guide-to-defensive-baking',
      'https://www.goodreads.com/book/show/61884755-the-water-outlaws',
      'https://www.goodreads.com/book/show/61884755-the-water-outlaws',
      'https://www.goodreads.com/book/show/61884755-the-water-outlaws',
      'https://www.goodreads.com/book/show/61884755-the-water-outlaws'
]
 scra=MainAs(Url)
 reult=scra.Main()
 
