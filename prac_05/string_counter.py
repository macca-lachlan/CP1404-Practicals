
string = str(input("Text: "))
words = string.split(' ')
words.sort()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

sorted_keys = []
longest_word = 0
for key in word_to_count:
    sorted_keys.append(key)
    if longest_word < len(key):
        longest_word = len(key)
sorted_keys.sort()

for word in sorted_keys:
    print("{:{}} : {}".format(word, longest_word,  word_to_count[word]))

