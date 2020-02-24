'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
character_list = []
with open('dictionary.txt') as f:
    word_list = [x.strip() for x in f]

for word in word_list:
    character_list.append(len(word))
max_letters = max(character_list)
for i in word_list:
    if len(i) == 28:
        print("The longest word in this dictionary is", i + ", which has", max_letters, "letters.")


# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


alice_in_wonderland = open("AliceInWonderLand.txt")
word_list = []
for word in alice_in_wonderland:
    words = split_line(word.strip())
    for word in words:
        word_list.append(word.upper())
lens_words = []
for word in word_list:
    lens_words.append(len(word))

print("There are", len(word_list), "words in Alice in Wonderland and the average word in Alice in Wonderland is", sum(lens_words)/len(lens_words), "letters long.")

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_count = 0
for i in range(len(word_list)):
    if word_list[i].upper() == "ALICE":
        alice_count += 1
print("The name Alice appears", alice_count, "times")

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
# make a list of all 7 letter words (list comprehension)
# if len = 7, list.append
print(len(word_list))
print(word_list)
seven_letter_list = [x.upper() for x in word_list if len(x) == 7]
count_list = [word_list.count(x) for x in seven_letter_list] # something wrong here
print(count_list)
print(seven_letter_list)
print(max(count_list))

print(seven_letter_list[count_list.index(max(count_list))])



# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
cheshire_count = 0
cat_count = 0
cheshirecat_count = 0
for i in range(len(word_list)):
    if word_list[i].upper() == "CHESHIRE":
        cheshire_count += 1
    if word_list[i].upper() == "CAT":
        cat_count += 1
    if word_list[i].upper() == "CHESHIRE" and word_list[i + 1].upper() == "CAT":
        cheshirecat_count += 1

print("The word cheshire appears", cheshire_count, "times")
print("The word cat appears", cat_count, "times")
print("The phrase cheshire cat appears", cheshirecat_count, "times")


