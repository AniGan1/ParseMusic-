from bs4 import BeautifulSoup
import requests, json

def get_id_song(song):
    try:
      url = f"https://www.shazam.com/services/amapi/v1/catalog/ru/search?types=songs,artists&term={song}&limit=1"
      page = requests.get(url)
      page = page.content.decode('utf8')
      page = json.loads(page)
      page = page['results']['songs']['data'][0]['id']
    except:
      page = False
    
    return page 
    
def get_text_song(song):
    if(get_id_song ):
        song_text =get_id_song(song)
        url =  "https://www.shazam.com/ru-ru/song/"+ song_text
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            Lyrics = soup.find('div', class_='Text-module_text-gray-900__Qcj0F Text-module_fontFamily__cQFwR Text-post-module_size-base__o144k Text-module_fontWeightNormal__kB6Wg')  
            print(Lyrics.text)
        except:
            print("Текст не прикреплен к песне")
    else:
        print("Песня не найдена")

if(__name__ == "__main__"):
    name_text = input('Введите текст песни:')
    get_text_song(name_text)