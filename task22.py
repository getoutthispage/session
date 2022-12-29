import collections

text = 'It is often the case that the meaning of the text is not important'
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)
input()