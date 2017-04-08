import gensim
from gensim import corpora, models
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words

aic = open("an_inspector_calls.txt", "r").read().replace("\xc2", "").replace("\xe2", "").replace("\xef", "").decode('utf8', 'ignore')
aic_set = list(aic)
tokenizer = RegexpTokenizer(r'\w+')

raw = aic.lower()
tokens = tokenizer.tokenize(raw)

en_stop = get_stop_words('en')

stopped_tokens = [i for i in tokens if not i in en_stop]

p_stemmer = PorterStemmer()

texts = []
#textone = [p_stemmer.stem(i) for i in stopped_tokens]
textone = stopped_tokens
textone = list(set(textone))
texts.append(textone)
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=100)

print(ldamodel.print_topics(num_topics=20, num_words=3))
