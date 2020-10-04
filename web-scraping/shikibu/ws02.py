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
url = "https://www.animesking.com/category/animes/"
xpath_ani = "//div[@class ='listagem row']"
xpath_ani_title = "//div[@class='fakeInfos']"
xpath_ani_desc = "//div[@class='cAniInfosSinopse']//p"
#xpath_ani_tags = "//div[@class='genxed']"
xpath_ani_img = "//div[@class='cSingleCapa']/img"
xpath_ani_eps = "//div[@class='tab_content']"
xpath_tabs = "//ul[@class='tabs']"
xpath_url = "//div[@class='um_terco']"
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

def format_token(token):
    p_ini = token.split('.php?')
    print("----p_ini   " + p_ini)
    
    return f_token


def start(): 
    condition = input("Usar txt [1]     Capturar [2]")

    if condition == "2":
        print("condition 2")

        #url_2 = "https://animesonline.ru/anime/?status=&type=&order=update"
        #driver.get(url_2)
        #driver.implicitly_wait(1)
        #element = driver.find_element_by_xpath(xpath_ani)
        #html_content = element.get_attribute('outerHTML')
        #soup = BeautifulSoup(html_content, 'html.parser')

        #with codecs.open('animeslist_updt.txt', 'a', encoding='utf-8') as fpli_2:
        #    for link in soup.find_all('a'):
        #        animes_list_updt.append(link.get('href')) 
        #        fpli_2.write(link.get('href') + "\n")                

        while 1 == 1: #get anime list
            
            try:    

                if ct_page > 1:
                    url = "https://www.animesking.com/category/animes/page/" + str(ct_page) + "/"
                    
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

        #f_2 = open('animeslist_updt.txt', 'r')
        #for line in f_2:
        #    animes_list_updt.append(line)
        #f_2.close
    else: 
        print("input invalido")
        quit()   

    return


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

    #element_tag = driver.find_element_by_xpath(xpath_ani_tags)        # tags
    #html_content = element_tag.get_attribute('outerHTML')
    #soup = BeautifulSoup(html_content, 'html.parser') 
    #anime_tag_list = []
    #for a in soup.find_all('a'):
    #    anime_tag_list.append(a.text)

    element_img = driver.find_element_by_xpath(xpath_ani_img)        # cover
    anime_cover = element_img.get_attribute('src')


    element_ep = driver.find_element_by_xpath(xpath_tabs)       # ep list
    html_content = element_ep.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')  

    ct_tb = 1
    season_list = []
    anime_ep_list = []
    anime_ep_list_fnl = [] 
    anime_ep_filtros = []   

    for tab in soup.findAll('a'):
        tab_title = tab.text
        print("--------TAB               " + tab_title)
        element_ep = driver.find_element_by_xpath(xpath_url + "[" + str(ct_tb) + "]")       
        html_content = element_ep.get_attribute('outerHTML')
        soup = BeautifulSoup(html_content, 'html.parser')  

        for strong in soup.findAll('strong'):
            strong_content = strong.text
            print("--------STRONG               " + strong_content)

            for link in soup.find_all('a'):
                token = link.get('href')
                print("-------TOKEN    " + token)
                







                ep_url = str(token)    
                driver.get(ep_url)

                element = driver.find_element_by_xpath(xpath_url) 
                html_content = element.get_attribute('outerHTML')
                soup = BeautifulSoup(html_content, 'html.parser')
                for link in soup.find_all('a'):
                    print(link.get('href'))
                    anime_ep_list.append(link.get('href')) 

                #print(element.get_attribute('src'))     
                ct_ep = ct_ep + 1    

            dict_lng = { strong_content : anime_ep_list }
            anime_ep_list_fnl.append(dict_lng)

        dict_ep = { tab_title : anime_ep_list_fnl }
        anime_ep_filtros.append(dict_ep)

    dict_anime = { 'titulo': anime_title ,'capa': anime_cover , 'descricao': anime_desc, 'episodios': anime_ep_filtros }
    anime_pack.append(dict_anime)
        
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



# timer
finish = time.time()
exec_time_s = finish - start
exec_time_m = exec_time_s / 60

print("***********************************************************************")
print("* ARQUIVO GRAVADO! // Tempo decorrido: " + str(exec_time_m) + " minutos.")
print("* " + str(ct_anime_proc) + " animes capturados, totalizando " + str(ct_ep) + " episódios.")
print("***********************************************************************")

driver.quit()