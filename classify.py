import nltk

def find_structure(TEXT):
	TOKENS = nltk.word_tokenize(TEXT)
	SPEECH = [e[1] for e in nltk.pos_tag(TOKENS)]
	CUR_STRUCTURE = sorted(SPEECH)
	return CUR_STRUCTURE

def train(DATA,STRUCTURES):
	for SENTENCE in DATA:
		TOKENS = nltk.word_tokenize(SENTENCE)
		SPEECH = [e[1] for e in nltk.pos_tag(TOKENS)]
		CUR_STRUCTURE = sorted(SPEECH)

		works = False
		for STRUCTURE in STRUCTURES:
			if(str(CUR_STRUCTURE) == str(STRUCTURE)):
				STRUCTURES[str(STRUCTURE)].append(SPEECH)
				works = True

		if(not works):
			STRUCTURES[str(CUR_STRUCTURE)] = []
			STRUCTURES[str(CUR_STRUCTURE)].append(SPEECH)

	return STRUCTURES

def find(TEXT, STRUCTURES):
	CUR_STRUCTURE = find_structure(TEXT)

	return (STRUCTURES[str(CUR_STRUCTURE)])

DATA = open("Text.txt",'r',encoding="utf8").read().replace('"','').split(".")

STRUCTURES = train(DATA, {})

for e in STRUCTURES:
	print(e,STRUCTURES[e])

print(find("I strolled up",STRUCTURES))




