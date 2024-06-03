from textProcessing import *
from vectorization import *
from clustering import *
from word_embedding import *
import json 

class service() :
    
    def match (ds_path, query:str, model_path, docs_path):
        processed_qry = textProcessing.qry_pre_processing(query)
        qry = []

        for i in processed_qry:
            i=' '.join(i)
            qry.append(i)
            
        docs = calculate_simi(qry, model_path, docs_path)
        
        response = service.get_docs(ds_path,docs)
            
        return response
    
    
    def match_to_clusters(ds_path, query:str, model_path, matrix_path, clusters_path):
        processed_qry = textProcessing.qry_pre_processing(query)
        qry = []

        for i in processed_qry:
            i=' '.join(i)
            qry.append(i)
            
        docs = clustering.match(qry, model_path, matrix_path, clusters_path)
        
        response = service.get_docs(ds_path,docs)
            
        return response
    
    
    def embedding_match(ds_path, query:str, docs_path):
        
        processed_qry = textProcessing.qry_pre_processing(query)
        qry = []

        for i in processed_qry:
            i=' '.join(i)
            qry.append(i)
            
        docs = word_embedding.cos_similarity(docs_path,qry)
        
        response = service.get_docs(ds_path,docs)
        
        return response
        
        
    def get_docs(ds_path,docs):
        raw_data = textProcessing.readDataset(ds_path)
        raw_data.columns =['text']
        
        response = []
        
        for doc in docs: 
            response.append({'doc_id':int(doc),'text':raw_data['text'][doc]})
        
        return response
