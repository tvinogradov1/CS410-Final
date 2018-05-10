import string
import re
import enchant
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


stopwords = open("lemur-stopwords.txt", 'r').read().split()
lemmatizer = WordNetLemmatizer()
d = enchant.Dict("en_US")

def removeStopWords(file_in, file_out):
    idx = 0;
    num_songs = 0
    with open(file_in,'r') as inFile, open(file_out,'w') as outFile:
        lines = inFile.readlines()
        num_songs += 1
        for line in lines: # each line in doc
            line = line.split()
            line = [lemmatizer.lemmatize(l) for l in line]
            if idx > 0 and len(line) != 0 and line[0] == '>':
                num_songs += 1
                outFile.write("\n") # new song
            idx += 1;
            clean_text = []
            for l in line:
                l = l.lower()
                # remove stopwords, short words, and redundant words
                if l not in stopwords and len(l) >= 3 and d.check(l):
                    # remove punctuation except apostrophes
                    l = re.sub("[^a-zA-Z' ]+", '', l)
                    clean_text.append(l.lower())
                    for item in clean_text:
                        outFile.write(item + " ")
        inFile.close()
        outFile.close()
    print("Number of songs parsed : " + str(num_songs))
