import pandas as pd
import pickle
from textProcessing import *
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.cluster import KMeans




def tfidf(dsPath, queryPath, path1 , ds_num):
    
    ds = pd.read_csv(dsPath ,encoding='utf-8' ,sep='\t')
    #vectorizer = TfidfVectorizer(tokenizer=textProcessing.tokenize_and_remove_stopwords,lowercase=True,stop_words='english',ngram_range=(1, 1),min_df=5, max_df=0.7)
    vectorizer = TfidfVectorizer(tokenizer=textProcessing.tokenize_and_remove_stopwords,lowercase=True,stop_words='english',ngram_range=(1, 1),min_df=5, max_df=0.8)
    documents_matrix = vectorizer.fit_transform(ds['text'])

    pickle.dump(documents_matrix, open(path1 + "tfidf_docs" + ds_num + ".pickle", "wb"))

    pickle.dump(vectorizer, open(path1 + "model" + ds_num + ".pickle", "wb"))
    
    #qry

    qry = pd.read_csv(queryPath ,encoding='utf-8' ,sep='\t')

    queries_matrix = vectorizer.transform(qry['text'])
    pickle.dump(queries_matrix, open(path1 + "tfidf_queries" + ds_num + ".pickle", "wb"))
    
    
    



def calculate_simi(query,model_path,docs_path):
    
    vectorizer = pickle.load(open(model_path, "rb"))
    query_vector = vectorizer.transform(query)
    docs = pickle.load(open(docs_path, "rb"))

    cosin=[]
    cos=cosine_similarity(docs,query_vector).flatten()
    map=dict()
    for x in range(cos.size):
        map[cos[x]]=x

    myKey = list(map.keys())
    myKey.sort(reverse=True)
    if len(myKey) >= 10:
        for i in range(10):
            cosin.append(map.get(myKey[i]))
    else:
        # Handle the case where myKey has fewer than 10 elements
        for key in myKey:
            cosin.append(map.get(key))
    return cosin       



