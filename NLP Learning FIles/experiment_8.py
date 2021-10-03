from nltk.corpus import wordnet
#Finding different definitions and checking meaning of those for the word play.

#Finding details of word 'Fun'
word = wordnet.synsets("Fun")
print(word.names())
print(word.definition())
print(word.examples())