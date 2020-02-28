'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''
# Binary and linear are written as functions (5pts)
import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


with open('dictionary.txt') as dictionary:
    dictionary_list = [x.strip() for x in dictionary]

# Successful linear spellcheck (10pts)
def linear_search(key, dictionary):
    i = 0
    while i < (len(dictionary_list)) and key!= dictionary_list[i]:
        i += 1
    if i >= len(dictionary_list):
        print(key, "is not in the dictionary, it is in line", line_num)
print("Linear Search")
words = []
line_num = 0
file = open('AliceInWonderLand200.txt')
for line in file:
    line_num += 1
    line_text = line.strip().upper()
    line_words = split_line(line_text)
    for word in line_words:
        words.append(word)
        linear_search(word.upper(), dictionary_list)
file.close()

# Successful binary spellcheck (10pts)
def binary_search(key, dictionary):
   lower_bound = 0
   upper_bound = len(dictionary_list) - 1
   found = False
   while lower_bound <= upper_bound and not found:
       middle_pos = (lower_bound + upper_bound) // 2
       if dictionary_list[middle_pos] < key:
           lower_bound = middle_pos + 1
       elif dictionary_list[middle_pos] > key:
           upper_bound = middle_pos - 1
       else:
           found = True
   if not found:
       print(key, "is not in the dictionary, it is in line", line_num)
file = open('AliceInWonderland200.txt', 'r')
print("")
print("Binary Search")
line_num = 0
for line in file:
    line_num += 1
    line_text = line.strip().upper()
    line_words = split_line(line_text)
    for word in line_words:
        words.append(word)
        binary_search(word.upper(), dictionary_list)
file.close()
# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
