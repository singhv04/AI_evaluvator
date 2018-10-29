# AI_evaluvator
AI which will be able to check the brief answers.

Tools used:
-bit-bucket iscnlp tagger and tokenizer.:https://bitbucket.org/iscnlp/
-gensim

Approach used:
The ground truth answers of all the questions is already stored.It is found that accuarcy increases effectively if we provide two ground answers for each question. Then the system will be able to check the answers provided later. The approach used here is Latent Semantic Indexing or Latent Semantic Analysis.

Latent Semantic Analysis:

This approach takes advantage of implicit higher order structure in the association of terms with documents i.e. semantic structure in order to improve the detection of relevant documents on the basis of terms found in queries.

Its a mathematical technique called SVD(Singular Value Decomposition) to identify patterns in the relationship between the terms and concepts contained in an unstructured collection of text.
Basically based on the principle that words that are used in the same contexts tend to have similar meanings.


Why didn't i used NLTK similarity metrix approach?
As it has some drawbacks which drastically affects the results.
-Wordnet has some issues with computing the similarity between adjectives and adverbs.
-some wordnet similarity measures misbehave.

