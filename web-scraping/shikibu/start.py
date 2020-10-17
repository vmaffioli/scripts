from ws import *

a = load_list(url.anime_list)
to_json = scraping(a)
with open(fl.inject, 'w', encoding='utf-8') as jp:
    js = json.dumps(to_json)
    jp.write(js)
jp.close    
with open(fl.error_out, 'w', encoding='utf-8') as jp:
    for anime in fl.error_list:
        jp.write(anime)    
jp.close    
msg_end_exec()
exit()