import urllib.request
from urllib.request import Request
import json
import re
val = 0
mys = 0
ins = 0
pok = 0
cha = 0
countah = 0
after = ""
print("Running program... This might take a while")
while(countah<10):
    print(countah)
    try:
        url = 'https://www.reddit.com/r/singaporeraw/top/.json?t=all&limit=100&after=' + after
        request = Request(url)
        request.add_header('api-key', '200')
        response = urllib.request.urlopen(request)
        data = response.read()
        parsed_json = json.loads(data.decode('utf-8'))
        meh = parsed_json['data']['children']
        for i in range(len(meh)):
            try:
                for word in re.compile('\w+').findall(meh[i]['data']['title']):
                    word = word.lower()
                    if(word == 'lawrence'):
                        val += 1
                    if(word == 'indian' or word=='india'):
                        mys += 1
                    if(word == 'chinese' or word=='china'):
                        ins += 1
                    if(word == 'pokémon' or word == 'pokemon'):
                        pok += 1
                    if(word == 'malay' or word=='malaysia'):
                        cha += 1
            except:
                pass
        after = parsed_json['data']['children'][len(meh)-1]['data']['name']
        countah+=1
    except:
      # print('GG got rejected')
      pass
print("Lawrence: " + str(val) + "\nIndian: " + str(mys) + "\nChinese: " + str(ins) + "\nPokemon: " + str(pok) + "\nMalay: " + str(cha))
