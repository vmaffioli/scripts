from ws03 import *

a = load_list(url.anime_list)
to_json = scraping(a)
with open(fl.inject, 'w', encoding='utf-8') as jp:
    js = json.dumps(to_json)
    jp.write(js)
msg_end_exec()
exit()