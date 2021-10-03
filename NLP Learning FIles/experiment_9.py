#Counting POS tags

from collections import Counter
import nltk
text="Data science is the field of study that combines domain expertise, programming skills, and knowledge of mathematics and statistics to extract meaningful insights from data."
lower_case=text.lower()
tokens=nltk.word_tokenize(lower_case)
tags=nltk.pos_tag(tokens)
counts=Counter(tag for word,tag in tags)
print(counts)

'''
#Frequency method
import nltk
text="Data science is the field of study that combines domain expertise, programming skills, and knowledge of mathematics and statistics to extract meaningful insights from data."
words=nltk.tokenize.word_tokenize(text)
fd=nltk.FreqDist(words)
fd.plot()
'''