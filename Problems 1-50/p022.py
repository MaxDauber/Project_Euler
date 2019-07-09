'''
Using names.txt a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
from string import ascii_uppercase


def get_score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))

with open('p022_names.txt') as file:
    name_list = file.read().split(',')
    name_list.sort()
    print(sum(num * get_score(word) for num, word in enumerate(name_list, 1)))