import nltk


DATA = open("Text.txt",'r',encoding="utf8").read().split(".")

for SENTENCE in DATA:
	TOKENS = nltk.word_tokenize(SENTENCE)
	SPEECH = [e[1] for e in nltk.pos_tag(TOKENS)]


	print(SENTENCE,SPEECH)
	print()