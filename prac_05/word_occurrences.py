"""
CP1404 WORD OCCURRENCES
By Samantha Martin
I did look at the solutions to assist in some parts that
I found difficult to understand.
"""

WORD_COUNT = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        WORD_COUNT[word] += 1
    except KeyError:
        WORD_COUNT[word] = 1

words = list(WORD_COUNT.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, longest_word, WORD_COUNT[word]))