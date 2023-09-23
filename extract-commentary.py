import re

with open('commentary.txt', encoding='utf-8') as f:
    commentary = f.read()

chapter_splitter = re.compile(r'^(\d+\.\d+)', flags=re.MULTILINE | re.DOTALL)

split_text = re.split(chapter_splitter, commentary)

i = 0
while i < len(split_text):
    i += 4
    verse_id = split_text[i-1]
    verse_content = split_text[i]
    with open(f'build/commentary/{verse_id}.txt', 'w', encoding='utf-8') as f:
        f.write(verse_content.replace('\n', '').strip())
        f.close()