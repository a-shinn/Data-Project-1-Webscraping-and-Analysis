import pandas as pd
import bs4 as bs
import requests
import re

webpage = requests.get('https://www.animanga.com/scripts/textesgb/eva1.html')
soup = bs.BeautifulSoup(webpage.text, 'html.parser')
page_text = soup.get_text()

#------------------

regex = re.compile(r"(?m).+:[^*#:]+\n")

line = re.findall(regex,page_text)

#------------------

word_filter = ['Neon','Episode','Email','Nadia','http'] # list of words to filter out translator notes, using words not used in the actual scripts
result = [x for x in line if not any(s in x for s in word_filter)] # list of each distinct line in the episode
# result = [x for x in line if 'Neon' not in x] # list of each distinct line in the episode


character_lines = {}

# iterating through each line of text, creating a key and word count
# if character not already in character_lines, otherwise adding to the existing entry
for text in result:
    character_name = re.findall('[^:#]*',text)[0] # regex to pull the name of the character speaking
    word_count_line = len(text.split())-1
    if character_name in character_lines:
        character_lines[character_name][0] += 1
        character_lines[character_name][1] += word_count_line
    else:
        character_lines[character_name] = [1,word_count_line]

print(character_lines)
print()
print(result[0])

# matches = re.finditer(regex, page_text)
# for matchNum, match in enumerate(matches, start=1):
#
#     print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
#                                                                         end=match.end(), match=match.group()))