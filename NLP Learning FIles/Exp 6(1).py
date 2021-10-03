import nltk
import matplotlib.pyplot as plt

sentence = "NLP is broadly defined as the automatic manipulation of natural language by software."
grammar = (r"""
  NP:
    {<.*>+}          # Chunk everything
    }<VBD|IN>+{      # Chink sequences of VBD and IN
  """)
chunkParser = nltk.RegexpParser(grammar)
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
tagged
tree = chunkParser.parse(tagged)
for subtree in tree.subtrees():
    print(subtree)
print(tree.draw())