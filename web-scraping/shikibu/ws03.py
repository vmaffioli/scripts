# -*- encoding: utf-8 -*-
import requests
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

def start():
    anime_list = load_list(url.anime_list)
    scraping(anime_list)

    return

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
    elif to_find == cd.ht:
        for a in soup.find_all("a"):
            content.append(a.href)
    if len(content) == 1:
        content = str(content).strip('[]')
  
    return content   

def format_token(token):
    p_ini = token.split('.php?')
    print("----p_ini   " + p_ini)
    # =!

    return f_token

def write_data(to_write, file):
    with codecs.open(file, 'a', encoding='utf-8') as fp:
        for data in to_write:
            fp.write(data)    

    return     

def load_list(url): #start the script
    anime_list = []
    condition = msg_get_input()
    counter.page += 1
    if condition == "n":
        msg_build_list()
        while 1 == 1: #get anime list
            try:  # while break  
                if counter.page > 1:
                    a = "https://www.animesking.com/category/animes/" + str(counter.page) + "/"
                    driver_load(a)
                else:
                    driver_load(url.anime_list)
                    soup = get_soup(xpath.anime_list, cd.x)
                    content = find_content(soup, cd.ht)
                    write_data(content, fl.anime_list) # write captured anime list animelist.txt
                    msg_page_counter()
            except: 
                for item in open(fl.anime_list, 'r'):
                    anime_list.append(item)
                break        
    elif condition == "y":
        msg_import_list()
        for item in open(fl.anime_list, 'r'):
            anime_list.append(item)
        msg_anime_counter()
    else:    
        msg_invalid_input()

    return anime_list

def scraping(animes):
    for anime in animes: #  get ep lists for each anime listed
        driver_load(anime)
        # get title
        soup = get_soup(xpath.title, cd.xp)  
        anime_title = soup.find('h1').contents[0] 
        # get description
        i = counter.desc   
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

        print(anime_title)
        print(anime_desc)
        print(anime_cover)

    return

start()



    


    



quit()
