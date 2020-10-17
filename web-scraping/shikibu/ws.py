# -*- encoding: utf-8 -*-
import requests
import codecs
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from data import *
from msg import *


# . chrome instance 
option = Options()
option.headless = True
option.add_argument("--incognito")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(3)

def driver_load(url):    
    driver.get(url)
    driver.implicitly_wait(1)

    return

def get_soup(element, type): # driver call, soup call 
    if type == cd.xp:
        element = driver.find_element_by_xpath(element)
    elif type == cd.id:
        element = driver.find_element_by_id(element)
    elif type == cd.nm:
        element = driver.find_element_by_name(element)
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')

    return soup

def find_content(soup, to_find): # find content in soup
    content = []
    if to_find == cd.at: # -!
        for a in soup.find_all("a"):
            content.append(a.text)
    elif to_find == cd.ah:
        for a in soup.find_all("a"):
            content.append(a.get('href'))
    elif to_find == cd.st:
        for a in soup.find_all("strong"):
            content.append(a.text)
    elif to_find == cd.t:
        for a in soup.find_all("a"):
            content.append(a.get('title'))
    if len(content) == 1:
        content = str(content).strip('[]')
  
    return content   

def write_data(to_write, file):
    with codecs.open(file, 'a', encoding='utf-8') as fp:
        for data in to_write:
            fp.write(data + "\n")    

    return     

def load_list(url): #start the script
    anime_list = []
    condition = msg_get_input()
    if condition == "n":
        msg_build_list()
        try:  # while break
            while 1 == 1: #get anime list
                ct.page += 1
                if ct.page > 1:
                    a = "https://www.animesking.com/category/animes/page/" + str(ct.page) + "/"
                    driver_load(a)
                else:  
                    driver_load(url)
                soup = get_soup(xpath.anime_list, cd.xp)
                content = find_content(soup, cd.ah)
                write_data(content, fl.anime_list) # write captured anime list animelist.txt
                msg_page_ct()
        except Exception as e: 
            print(e)
            for item in open(fl.anime_list, 'r'):
                anime_list.append(item)
            pass        
    elif condition == "y":
        msg_import_list()
        for item in open(fl.anime_list, 'r'):
            anime_list.append(item)
        msg_anime_counter()
    else:    
        msg_invalid_input()

    return anime_list

def scraping(animes):
    anime_dict = {}
    iiii = ct.json
    iiiii = ct.error
    for anime in animes: #  get ep lists for each anime listed
        try:
            driver_load(anime)
            # get title
            soup = get_soup(xpath.title, cd.xp)  
            anime_title = soup.find('h1').contents[0] 
            # get description
            i = ct.desc   
            anime_desc = ""
            while 1 == 1:  
                try:    
                    xpath_ani_desc_ct = xpath.desc + "[" + str(i) + "]"    
                    desc = driver.find_element_by_xpath(xpath_ani_desc_ct).text       
                    if desc != "":
                        anime_desc = anime_desc + desc
                    i += 1
                    pass
                except:
                    break    
            # get cover
            element_img = driver.find_element_by_xpath(xpath.cover)        
            anime_cover = element_img.get_attribute('src')
            # get tabs
            soup = get_soup(xpath.tabs, cd.xp)
            i = 1
            content_tabs = find_content(soup, cd.at)
            tab_dict = {}
            if type(content_tabs) != list:
                t = content_tabs
                content_tabs = []
                content_tabs.append(t)
            for tab in content_tabs:
                soup = get_soup(xpath.lang, cd.xp)
                languages = find_content(soup, cd.st)
                ii = 1
                lang_dict = {}
                for n in languages:
                    iii = 0
                    ep_dict = {}
                    a = str(xpath.eps1 + "[" + str(i) + "]" + str(xpath.eps2) + "[" + str(ii) + "]")
                    try:
                        soup = get_soup(a, cd.xp)
                        ep_titles = find_content(soup, cd.t)
                        ep_tokens = find_content(soup, cd.ah)
                    except:
                        ep_titles = cd.eti
                        ep_tokens = cd.eto
                    if len(ep_titles) == 0:
                        ep_url = cd.eur
                        ep_dict.update({cd.edc : cd.edc})   
                    else:         
                        if type(ep_titles) == str:
                            if len(token[22:]) != 59:
                                ep_url = fl.vd2 + ep_tokens[22:]
                            else:
                                ep_url = fl.vd2 + ep_tokens[22:]
                            
                            ep_dict.update({ep_titles : ep_url})
                        else:    
                            for token in ep_tokens:   
                                token.strip()
                                token = token.replace("\n", "")                      
                                if len(token[21:]) == 60:
                                    ep_url =  + token[21:]
                                elif len(token[21:]) == 121:
                                    ep_url = fl.vd3 + token[21:]                                              
                                else:                      
                                    ep_url = fl.vd2 + token[21:]
                                ep_dict.update({ep_titles[iii] : ep_url})
                                iii += 1                
                    lang_dict.update({n : ep_dict})  
                    ii += 1                 
                tab_dict.update({tab : lang_dict})    
                i += 1          
            anime_dict.update({ iiii : { "title" : anime_title , "cover" : anime_cover, "description" : anime_desc, "videos" : tab_dict}})     
            print(str(iiii) + "/" + str(len(animes)))
            iiii += 1
        except:
            iiiii += 1
            fl.error_list.append(anime)
            msg_error(iiiii)
    return anime_dict


