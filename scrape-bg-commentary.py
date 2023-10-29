import requests
import re
from gita2html import gita_verses_per_chapter

def GetCommentary(chapter, verse):
    url = f'https://www.bhagavad-gita.org/Gita/verse-{str(chapter).zfill(2)}-{str(verse).zfill(2)}.html'

    r = requests.get(url)
    html = r.text

    pattern_madhavacharya = r'<center>Madhvacarya\'s Commentary</center>(.*?)</div>'
    pattern_kesava = r'<center>Kesava Kasmiri\'s Commentary</center>(.*?)</div>'
    pattern_ramanuja = r'<center>Ramanuja\'s Commentary</center>(.*?)</div>'

    # Use re.search to find the matching text
    default_cmnt = 'No commentary available.'

    try:
        match = re.search(pattern_madhavacharya, html, re.DOTALL)
        madhava_cmnt = match.group(1)
    except:
        madhava_cmnt = default_cmnt

    try:
        match = re.search(pattern_kesava, html, re.DOTALL)
        kesava_cmnt = match.group(1)
    except:
        kesava_cmnt = default_cmnt

    try:
        match = re.search(pattern_ramanuja, html, re.DOTALL)
        ramanuja_cmnt = match.group(1)
    except:
        ramanuja_cmnt = default_cmnt

    return {'kesava': kesava_cmnt, 'ramanuja': ramanuja_cmnt, 'madhava': madhava_cmnt}

for chapter in range(1, 18+1):
    for verse in range(1, gita_verses_per_chapter[chapter]+1):
        print(f"Writing commentary for {chapter}.{verse}")
        cmnt = GetCommentary(chapter, verse)
        for philosopher in cmnt.keys():
            with open(f'./build/commentary/{philosopher}/{chapter}.{verse}.txt', 'w', encoding='utf-8') as f:
                f.write(cmnt[philosopher])
                f.close()
