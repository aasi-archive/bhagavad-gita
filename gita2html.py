import json
import jinja2
import os

gita_json = None

GITA_BUILD_DIR = './build/'

chapter_titles = {
    1: "Lamenting the Consequences of War",
    2: "The Way of Knowledge",
    3: "Action",
    4: "Action versus Inaction",
    5: "Renunciation",
    6: "Yoga",
    7: "Realisation of the Supreme",
    8: "The Way to the Supreme",
    9: "The Kingly Secret",
    10: "Glimpse of the Supreme",
    11: "The Cosmic Form of God",
    12: "Devotion",
    13: "The Cosmic Field",
    14: "Three Qualities of Nature",
    15: "The Supreme Spirit",
    16: "The Fall of Man",
    17: "Three Kinds of Men",
    18: "Liberation"
}

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

def ReplaceEnglishWithHindiNumbers(text):
    nummap = {"1": "१",
    "2": "२",
    "3": "३",
    "4": "४",
    "5": "५",
    "6": "६",
    "7": "७",
    "8": "८",
    "9": "९",
    "0": "०"
    } 

    for num in nummap:
        text = text.replace(num, nummap[num])
    return text

def ReplaceEnglishWithTamilNumbers(text):
    nummap = {  "1": "௧",
                "2": "௨",
                "3": "௩",
                "4": "௪",
                "5": "௫",
                "6": "௬",
                "7": "௭",
                "8": "௮",
                "9": "௯",
                "0": "०"
            }
    for num in nummap:
        text = text.replace(num, nummap[num])
    return text

def GitaGenerateChapterPath(chapter, prefix=GITA_BUILD_DIR):
    return os.path.join(prefix, f'{chapter}.html')

def GitaRenderChapter(chapter):
    chapter_integer = int(chapter)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    jinja2_env = jinja2.Environment(loader=templateLoader)
    page_template = jinja2_env.get_template('chapter.template.html')

    verses = []
    for verse in gita_json[chapter].keys():
        gita_json[chapter][verse]["verse_number"] = int(verse)
        gita_json[chapter][verse]["chapter_number"] = int(chapter)
        verses.append(gita_json[chapter][verse])
    
    for verse in verses:
        # Process the Sanskrit text, strip the leading newlines, replace the \n\ with <br>
        processed_sanskrit_text = ReplaceEnglishWithHindiNumbers((verse["text"].strip()).replace("\n\n", " <br> "))
        # Split the text by space
        sanskrit_words = processed_sanskrit_text.split(" ")
            
        for i in range(0, len(sanskrit_words)):
            word = sanskrit_words[i]

            if("<br>" not in word):
                # Put a <span> around every Sanskrit word, the learnsanskrit.cc link
                sanskrit_words[i] = f'<div class="sanskrit-word"><a href="https://www.learnsanskrit.cc/translate?search={word.split("।")[0]}" target="_blank">{word}</a></div>&nbsp;'

        verse["text"] = ''.join(sanskrit_words)
        verse["word_meanings"] = verse["word_meanings"].strip()
        verse["transliteration"] = verse["transliteration"].strip()
        verse["translation_hi"] = ((ReplaceEnglishWithHindiNumbers(verse["translation_hi"]).replace('--', '\u2014')).replace('-', '\u2014')).split(u'।।')[2]
        verse["translation_ta"] = ReplaceEnglishWithTamilNumbers(verse["translation_ta"])
    next_chapter_url = ""
    previous_chapter_url = ""

    if(chapter_integer < 18):
        next_chapter_url = GitaGenerateChapterPath(chapter_integer+1, prefix='')
    
    if(chapter_integer > 1):
        previous_chapter_url = GitaGenerateChapterPath(chapter_integer - 1, prefix = '')
    
    page_info = { "chapter": chapter,
                 "verses": verses,
                 "n_verses": gita_verses_per_chapter[chapter_integer],
                 "chapter_title": chapter_titles[chapter_integer].upper(),
                 "next_chapter_url": next_chapter_url,
                 "previous_chapter_url": previous_chapter_url
                }

    with open(GitaGenerateChapterPath(chapter), mode="w", encoding="utf-8") as page:
        page.write(page_template.render(page_info))
        page.close()
    
with open('gita.json', 'r', encoding='utf-8') as f:
    gita_json = json.loads(f.read())

for i in range(1, 18+1):
    GitaRenderChapter(str(i))
