import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import codecs
import time


# timer 
start = time.time()

# . inputs
url = "https://animesonline.ru/anime/"
xpath_ani = "//div[@class ='listupd']"
xpath_next_page = "//a[class='r']"
xpath_ani_title = "//h1[@class='entry-title']"
xpath_ani_desc = "//div[@class='entry-content']//p"
xpath_ani_tags = "//div[@class='genxed']"
xpath_ani_img = "//div[@class='thumb']/img"
xpath_ani_eps = "//div[@class='eplister']"
xpath_url = "//div[@class='post']//video"
xpath_url_2 = "//div[@class='item video-nav']"
animes_list = []
animes_list_updt = []
anime_pack = []
anime_pack_updt = []
error_list = []
ct_page = 1
ct_anime_total = 0
ct_anime_proc = 0
ct_ep = 0
ct_print_t = 0

# . chrome instance 
option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)


condition = input("Usar txt [1]     Capturar [2]")

if condition == "2":
    print("condition 2")

    url_2 = "https://animesonline.ru/anime/?status=&type=&order=update"
    driver.get(url_2)
    driver.implicitly_wait(1)
    element = driver.find_element_by_xpath(xpath_ani)
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')

    with codecs.open('animeslist_updt.txt', 'a', encoding='utf-8') as fpli_2:
        for link in soup.find_all('a'):
            animes_list_updt.append(link.get('href')) 
            fpli_2.write(link.get('href') + "\n")                

    while 1 == 1: #get anime list
        
        try:    

            if ct_page > 1:
                url = "https://animesonline.ru/anime/?page=" + str(ct_page)
                
                #print(url)
                #break

            print("")
            print("")
            print("***************** Processando pagina " + str(ct_page) + "... ( " + url + " ) *****************")
            print("")
            print("")
    

            driver.get(url)
            driver.implicitly_wait(1)
            element = driver.find_element_by_xpath(xpath_ani)
            html_content = element.get_attribute('outerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')

            ct_anime_page = 0 
            with codecs.open('animeslist.txt', 'a', encoding='utf-8') as fpli:
                for link in soup.find_all('a'):
                    animes_list.append(link.get('href')) 
                    fpli.write(link.get('href') + "\n")                
                    ct_anime_page = ct_anime_page + 1      

            ct_page = ct_page + 1
            ct_anime_total = ct_anime_total + ct_anime_page
            if ct_anime_page == 0:
                break
            
            print("")
            print("")
            print("***************** " + str(ct_anime_page) + " animes descobertos nesta pagina *****************")
            print("")
            print("***************** " + str(ct_anime_total) + " animes descobertos ao todo *****************")
            print("")
            print("")       

            pass
        except:
            print("**")
            print("error/final : page " + str(ct_page))
            print("**")
            break
elif condition == "1":  #get anime list from txt
    print("condition 1")
    f = open('animeslist.txt', 'r')
    for line in f:
        animes_list.append(line)
        ct_anime_total = ct_anime_total + 1
    f.close 

    f_2 = open('animeslist_updt.txt', 'r')
    for line in f_2:
        animes_list_updt.append(line)
    f_2.close
else: 
    print("input invalido")
    quit()            


for anime in animes_list: #  get ep lists for each anime listed
    ct_print_t = ct_print_t + 1
    driver.get(anime)
    driver.implicitly_wait(1)
    
    element_title = driver.find_element_by_xpath(xpath_ani_title) # title
    html_content = element_title.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    anime_title = soup.find('h1').contents[0]                     

    ct_desc_p = 1
    anime_desc = ""
    while 1 == 1:
        try:    
            xpath_ani_desc_ct = xpath_ani_desc + "[" + str(ct_desc_p) + "]"     # description
            desc = driver.find_element_by_xpath(xpath_ani_desc_ct).text       
            if desc != "":
                anime_desc = anime_desc + desc
            ct_desc_p = ct_desc_p + 1
            pass
        except:
            
            break    

    element_tag = driver.find_element_by_xpath(xpath_ani_tags)        # tags
    html_content = element_tag.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser') 
    anime_tag_list = []
    for a in soup.find_all('a'):
        anime_tag_list.append(a.text)

    element_img = driver.find_element_by_xpath(xpath_ani_img)        # cover
    anime_cover = element_img.get_attribute('src')

    element_ep = driver.find_element_by_xpath(xpath_ani_eps)       # ep list
    html_content = element_ep.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')   
    anime_ep_list = []    
    try:
        for link in soup.find_all('a'):
            token = link.get('href')
            ep_url = str(token)    
            driver.get(ep_url)

            try:
                element = driver.find_element_by_xpath(xpath_url)
                anime_ep_list.append([element.get_attribute('src')])
            except:
                element = driver.find_element_by_xpath(xpath_url_2) 
                html_content = element.get_attribute('outerHTML')
                soup = BeautifulSoup(html_content, 'html.parser')
                for link in soup.find_all('a'):
                    #print(link.get('href'))
                    anime_ep_list.append(link.get('href')) 

            #print(element.get_attribute('src'))     
            ct_ep = ct_ep + 1
            

        dict_anime = {'titulo': anime_title ,'capa': anime_cover , 'descricao': anime_desc, 'tags': anime_tag_list, 'episodios': anime_ep_list}
        anime_pack.append(dict_anime)
                  

 
    except Exception as e:
        error_list.append(anime_title)
        print("ERRO : \n" + e)

        pass


    ct_anime_proc = ct_anime_proc + 1
    print("***********************************************************************")
    print("* Ultimo capturado: " + anime_title + " // Total : " + str(ct_anime_proc) + " capturados")
    print("***********************************************************************")
    print("Lista de erros:" + str(len(error_list)) + " itens.")
    print(error_list)
    print("***********************************************************************")


#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************


for anime in animes_list_updt: #  get ep lists for each anime listed
    ct_print_t = ct_print_t + 1
    driver.get(anime)
    driver.implicitly_wait(1)
    
    element_title = driver.find_element_by_xpath(xpath_ani_title) # title
    html_content = element_title.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    anime_title = soup.find('h1').contents[0]                     

    ct_desc_p = 1
    anime_desc = ""
    while 1 == 1:
        try:    
            xpath_ani_desc_ct = xpath_ani_desc + "[" + str(ct_desc_p) + "]"     # description
            desc = driver.find_element_by_xpath(xpath_ani_desc_ct).text       
            if desc != "":
                anime_desc = anime_desc + desc
            ct_desc_p = ct_desc_p + 1
            pass
        except:
            
            break    

    element_tag = driver.find_element_by_xpath(xpath_ani_tags)        # tags
    html_content = element_tag.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser') 
    anime_tag_list = []
    for a in soup.find_all('a'):
        anime_tag_list.append(a.text)

    element_img = driver.find_element_by_xpath(xpath_ani_img)        # cover
    anime_cover = element_img.get_attribute('src')

    element_ep = driver.find_element_by_xpath(xpath_ani_eps)       # ep list
    html_content = element_ep.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')   
    anime_ep_list = []    
    try:
        for link in soup.find_all('a'):
            token = link.get('href')
            ep_url = str(token)    
            driver.get(ep_url)

            try:
                element = driver.find_element_by_xpath(xpath_url)
                anime_ep_list.append([element.get_attribute('src')])
            except:
                element = driver.find_element_by_xpath(xpath_url_2) 
                html_content = element.get_attribute('outerHTML')
                soup = BeautifulSoup(html_content, 'html.parser')
                for link in soup.find_all('a'):
                    #print(link.get('href'))
                    anime_ep_list.append(link.get('href')) 

            #print(element.get_attribute('src'))     
            ct_ep = ct_ep + 1
            

        dict_anime = {'titulo': anime_title ,'capa': anime_cover , 'descricao': anime_desc, 'tags': anime_tag_list, 'episodios': anime_ep_list}
        anime_pack_updt.append(dict_anime)
                  

 
    except Exception as e:
        error_list.append(anime_title)
        print("ERRO : \n" + e)

        pass


    ct_anime_proc = ct_anime_proc + 1
    print("***********************************************************************")
    print("* Ultimo capturado: " + anime_title + " // Total : " + str(ct_anime_proc) + " capturados")
    print("***********************************************************************")
    print("Lista de erros:" + str(len(error_list)) + " itens.")
    print(error_list)
    print("***********************************************************************")


anime_pack_cat = {'todos': anime_pack ,'recentes': anime_pack_updt}
anime_pack_final = {'categorias:': anime_pack_cat}
js = json.dumps(anime_pack_final)
with codecs.open('inject.json', 'a', encoding='utf-8') as fp:
    fp.write(js)


# timer
finish = time.time()
exec_time_s = finish - start
exec_time_m = exec_time_s / 60

print("***********************************************************************")
print("* ARQUIVO GRAVADO! // Tempo decorrido: " + str(exec_time_m) + " minutos.")
print("* " + str(ct_anime_proc) + " animes capturados, totalizando " + str(ct_ep) + " episódios.")
print("***********************************************************************")

driver.quit()