import sys
import gensim
import logging
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.corpora import Dictionary
from nltk.stem.porter import PorterStemmer

# specify number of topics here
#num_topics = [1, 2, 3, 4, 5]
num_topics = [6, 7, 8, 9, 10]

# Open and read data
docs = []
f = open("songs/songs_data.dat", 'r')
for line in f:
    # remove newline
    line = line[:-1]
    docs.append(line) # each song is a document
f.close()

# Lemmatize the data (replaces stemming)
lemmatizer = WordNetLemmatizer()
totalDocs = len(docs)
for i in range(totalDocs):
    docs[i] = [lemmatizer.lemmatize(token) for token in docs[i].split()]

# Create dictionary representation of data
dictionary = Dictionary(docs)
# Vectorize data
corpus = [dictionary.doc2bow(doc) for doc in docs]
corplen = len(corpus)

print('Number of unique tokens: %d' % len(dictionary))
print('Number of documents: %d' % len(corpus))

# Run and train LDA model for each number of topics
LDA = gensim.models.ldamodel.LdaModel
for ntopics in num_topics:
    print("running LDA for " + str(ntopics) + " topics")
    # Run for 100 iterations
    lda_model = LDA(corpus, num_topics=ntopics, id2word = dictionary, passes=100)
    #lda_model.print_topics(num_topics=ntopics[k], num_words=20))
    output_topics_file = open("outputs/" + str(ntopics) + "_topics.txt",'w+')
    with output_topics_file as topics_file:
        # save topics data
        topics = lda_model.show_topics(num_topics=ntopics, num_words=20)
        for topic in topics:
             # each element is a 2-tuple: [topic id, word distribution]
            topics_file.write('Topic ' + str(topic[0]) + '\n')
            topics_file.write(str(topic[1]))
            topics_file.write('\n\n')
