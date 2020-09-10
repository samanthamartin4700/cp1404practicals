"""
CP1404 WORD OCCURRENCES
By Samantha Martin
I did look at the solutions to assist in some parts that
i found difficult to understand.
"""

WORD_COUNT = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        WORD_COUNT[word] += 1
    except KeyError:
        WORD_COUNT[word] = 1

for word in words:
    print("{} : {}".format(word, WORD_COUNT[word]))