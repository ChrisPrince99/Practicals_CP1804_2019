"""this is a collection of words of nice words this is a fun thing it is"""

text = input("?")
word_dictionary = {v: k for k, v in enumerate(text.split(" "))}
# word_dictionary = {v: k for k, v in enumerate(text.split(" "))}
word_counts = {word: count for word, count in enumerate(text.split(" ")) if count in word_dictionary}


print(word_dictionary, word_counts)
# max_length = 0
# for word in word_dictionary.values():
#     if len(word) > max_length:
#         max_length = len(word)
#
# print(max_length)

# print("{:{}} = {}".format(x, y, z))
