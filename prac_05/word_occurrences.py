"""this is a collection of words of nice words this is a fun thing it is"""

words_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = words_to_count.get(word, 0)
    words_to_count[word] = frequency + 1

words = list(words_to_count.keys())
words.sort()

print(words_to_count)

max_length = 0
for word in words_to_count:
    if len(word) > max_length:
        max_length = len(word)
for word in words_to_count:
    print("{:{}} = {}".format(word, max_length, words_to_count[word]))

# word_dictionary = {v: k for k, v in enumerate(text.split(" "))}
# # word_dictionary = {v: k for k, v in enumerate(text.split(" "))}
# word_counts = {word: count for word, count in enumerate(text.split(" ")) if count in word_dictionary}
#
#
# print(word_dictionary, word_counts)
