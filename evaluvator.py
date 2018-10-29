#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:42:07 2018

@author: vaibhav
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:13:40 2018

@author: vaibhav
"""

#question-answer
q1="What is Inexhaustible Natural Resource?"
a1="The resources which are present in unlimited quantity in nature and are not likely to be exhausted by human activities are known as Inexhaustible Resources. For Example: Sunlight, air"

a2="It is a natural resource that will never run out so if we take advantage of the greatest natural resources will not be depleted and will continue to exist, such as water, sunlight, tidal energy, ocean energy and wind energy."

#importing tokenizer,tagger,parser,stemmer
from isc_tokenizer import Tokenizer
tk = Tokenizer(lang='en')

from isc_tagger import Tagger
tagger = Tagger(lang='eng')

"""
from __future__ import unicode_literals
from isc_parser import Parser
parser = Parser(lang='eng')
"""

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from nltk.corpus import wordnet 

#stemming
bag_of_words=[]
w=re.sub('[^a-zA-Z]', ' 'or',',a1)
temp1=w.split()
for k in range(0,len(temp1)):
    if temp1[k] not in bag_of_words:
        bag_of_words.append(temp1[k])
ground_stem=[ps.stem(word) for word in temp1 if not word in set(stopwords.words('english'))]

w=re.sub('[^a-zA-Z]', ' 'or',',a2)
print(w)
temp=w.split()
print(temp)
try_1=[ps.stem(word) for word in temp if not word in set(stopwords.words('english'))]



#semantic similarity
from gensim import corpora,models, similarities

d=[ground_stem,try_1]
dictionary = corpora.Dictionary(d)
dictionary.save('deerwester.dict')  # store the dictionary, for future reference
print(dictionary)

print(dictionary.token2id)


print(try_1)

test="Inexhaustible resources are resources that will never run out.Examples:geothermal sources,wind energy.A renewable resource is a natural resource with the ability of being replaced through biological or other natural processes and replenished with the passage of time. Renewable resources are part of our natural environment and form our eco-system."
w=re.sub('[^a-zA-Z]', ' 'or',',test)
temp1=w.split()
testx=[ps.stem(word) for word in temp1 if not word in set(stopwords.words('english'))]


corpus = [dictionary.doc2bow(text) for text in d]
corpora.MmCorpus.serialize('deerwester.mm', corpus)  # store to disk, for later use
print(corpus)


dictionary = corpora.Dictionary(d)
dictionary.save('deerwester.dict')  # store the dictionary, for future reference
print(dictionary)
print(dictionary.token2id)



corpus = [dictionary.doc2bow(text) for text in d]
corpora.MmCorpus.serialize('deerwester.mm', corpus)  # store to disk, for later use
print(corpus)


import os

if (os.path.exists("deerwester.dict")):
    dictionary = corpora.Dictionary.load('deerwester.dict')
    corpus = corpora.MmCorpus('deerwester.mm')
    print("Used files generated from first tutorial")
else:
    print("Please run first tutorial to generate data set")

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

corpus_lsi = lsi[corpus_tfidf]

lsi.print_topics(2)



new_vec = dictionary.doc2bow(testx)
print(new_vec)
vec_lsi = lsi[new_vec]
print(vec_lsi)


for doc in corpus_lsi: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
    print(doc)

index = similarities.MatrixSimilarity(lsi[corpus])
index.save('deerwester.index')

index = similarities.MatrixSimilarity.load('deerwester.index')

sims = index[vec_lsi] # perform a similarity query against the corpus
print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples

sims = sorted(enumerate(sims), key=lambda item: -item[1])

print('SIMILARITY')
print(sims)



#rewarding marks
reward=0
print(sims)
print(type(sims))
for i in range(0,len(sims)):
    match_percent = sims[i]
    check=(match_percent[1])
    if check>.65:
        index=match_percent[0]
        print(index)
        print(d[index])
        reward=reward+2
        print(reward)
    elif check>.55:
        index=match_percent[0]
        print(index)
        print(d[index])
        reward=reward+1.5
        print(reward)
    if len(test)>20:
        reward=reward+.5
        print(reward)
    if reward>6:
        reward=6
        print(reward)
            
reward=reward/2
print(reward)

print('Reward:',reward)
