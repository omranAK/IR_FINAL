import pickle
import numpy as np
import pandas as pd
from textProcessing import *
from vectorization import *
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

class clustering():
    
    def clustering(k,dataset,docsPath,writing_path,img_writing_path):
        
        docs = pickle.load(open(docsPath, "rb"))
        text = textProcessing.readDataset(dataset)

        # Apply K-means
        kmeans = KMeans(n_clusters=k, random_state=0).fit(docs)
        
        pickle.dump(kmeans, open(writing_path, "wb"))

        text['cluster'] = kmeans.labels_
        
        rsult = [] 
        for index, row in text.iterrows():
            rsult.append(f"Document {index} is in cluster {row['cluster']}")
            print(f"Document {index} is in cluster {row['cluster']}")


        labels = kmeans.labels_
        
        # Apply dimensionality reduction 
        tsvd = TruncatedSVD(n_components=2).fit(docs)
        X_reduced = tsvd.transform(docs)

        kmeans = KMeans(n_clusters=k, random_state=0).fit(X_reduced)
        labels = kmeans.labels_ 

        fig, ax = plt.subplots(figsize=(8,6))
        for i in range(k):
            ax.plot(X_reduced[labels==i,0], X_reduced[labels==i,1], '.')

        ax.set_title(f'KMeans Clustering with k={k}')   
        ax.set_xlabel('SVD 1')
        ax.set_ylabel('SVD 2')
        fig.savefig(img_writing_path)
        
        return rsult
    
    
    def match(query, model_path, matrix_path, clusters_path):
        tfidf_matrix = pickle.load(open(matrix_path, "rb"))
        kmeans = pickle.load(open(clusters_path, "rb"))
        vectorizer = pickle.load(open(model_path,'rb'))
        
        #vectorize query
        query_vector = vectorizer.transform(query)
        
        #get query cluster
        query_cluster = kmeans.predict(np.array([query_vector.toarray().flatten()]))
        
        #get vectors
        cluster_labels = kmeans.labels_  
        cluster_indices = np.where(cluster_labels == query_cluster)[0]
        cluster_vectors = tfidf_matrix[cluster_indices]
        
        #get document vectors of the same cluster as query
        one_cluster_with_id = clustering.get_vectors_of_one_cluster(tfidf_matrix,kmeans,query_cluster[0])
        
        #cosine similarity
        docs = clustering.cos_simi(cluster_vectors,query_vector,one_cluster_with_id)
        
        return docs



    def get_vectors_of_one_cluster(tfidf_matrix,kmeans,query_cluster):
        df_matrix = pd.DataFrame(tfidf_matrix)

        cluster_map = pd.DataFrame()
        cluster_map['doc_id'] = df_matrix.index.values
        cluster_map['doc_vectors'] = df_matrix
        cluster_map['cluster'] = kmeans.labels_

        one_cluster = cluster_map[cluster_map.cluster == query_cluster]
        
        return one_cluster
    
    
    
    def cos_simi(cluster_vectors,query_vector,one_cluster_with_id):
        cos=cosine_similarity(cluster_vectors,query_vector).flatten()

        model_output = []
        map=dict()
        for x in range(cos.size):
            y=one_cluster_with_id['doc_id'].iloc[x]
            map[cos[x]]=y

        myKey = list(map.keys())
        myKey.sort(reverse=True)
        for i in range(10):
            model_output.append(map.get(myKey[i]))
        
        
        return model_output