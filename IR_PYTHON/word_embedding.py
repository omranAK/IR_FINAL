from operator import itemgetter

import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity

from textProcessing import *
from vectorization import *
import pickle

nlp = spacy.load("en_core_web_lg")

class word_embedding():
    
     
    
    
    def embedding (dsPath, queryPath, path1 , ds_num):
        
        documents = pd.read_csv(dsPath ,encoding='utf-8' ,sep='\t')
        # documents = textProcessing.ds_pre_processing(path)
        vectors = [nlp(doc).vector for doc in documents['text']]
        pickle.dump(vectors, open(path1 + "embedded_docs" + ds_num + ".pickle", "wb"))
        
        #qry

        queries = pd.read_csv(queryPath ,encoding='utf-8' ,sep='\t')
        vectors = [nlp(qry).vector for qry in queries['text']]
        pickle.dump(vectors, open(path1 + "embedded_queries" + ds_num + ".pickle", "wb"))



    def cos_similarity(docs_path,processed_query):
        
        docs = pickle.load(open(docs_path, "rb"))
        # nlp = spacy.load("en_core_web_lg")
        query_vector =[nlp(str(processed_query)).vector]
        
        cosin=[]
        cos=cosine_similarity(docs,query_vector).flatten()
        map=dict()
        for x in range(cos.size):
            map[cos[x]]=x

        myKey = list(map.keys())
        myKey.sort(reverse=True)
        for i in range(10):
            cosin.append(map.get(myKey[i]))
        
        
        
        return cosin


