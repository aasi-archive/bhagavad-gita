import urllib.request
import os

gita_verses_per_chapter = {
    1: 47,
    2: 72,
    3: 43,
    4: 42,
    5: 29,
    6: 47,
    7: 30,
    8: 28,
    9: 34,
    10: 42,
    11: 55,
    12: 20,
    13: 35,
    14: 27,
    15: 20,
    16: 24,
    17: 28,
    18: 78
}

MP3_STORE_DIR = './build/recitation/'

def GenerateMP3URL(chapter, verse):
    chapter_fixed = str(chapter).zfill(2)
    verse_fixed = str(verse).zfill(2)
    return f'https://www.geetachanting.net/bvg/audio/x0001/{chapter_fixed}/bvg{chapter_fixed}v{verse_fixed}.mp3'

for chapter in range(1, 18+1):
    max_verses = gita_verses_per_chapter[chapter]
    for verse in range(1, max_verses+1):
        url = GenerateMP3URL(chapter, verse)
        file = os.path.join(MP3_STORE_DIR, f'{chapter}_{verse}.mp3')
        print(f"Downloading {url}...")
        if(os.path.exists(file)):
            continue
        else:
            urllib.request.urlretrieve(url, file)
