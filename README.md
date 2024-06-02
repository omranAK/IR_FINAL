IR_Python project is python project for search engine  .
# Provide this cores :
1- [Main.py] contains end-points: 
    -	@app.post("/api/user_query")
    -	@app.post("/api/match_to_cluster")
    -	@app.post("/api/embedding_match")

2- [service.py] contains the following services in the order: 
  processing a query and then calling the cosine similarity function on the processed queries vector and the documents vectors te optain the right answers :
    -	Match.
    -	Match to clusters.
    -	Embedding match.

3- [Text_processing.py] conatins the main pre-processing functions
  	• Reading dataset
	  • Normalization 
    • Converting to lowercase 
  	• Removing URLs
    • Removing punctuation
    • Converting numbers to words or deleting digits
    • Tokenization 
    • Correct query
    • Removing stop words
    • Stemming 

4- [Vectorization.py] contains:
    • TFIDFvectorizer
    • CosineSimilarity
5- [Dataset_one.ipynb] : pre-processing the first dataset and then vectorising then clustering it and finally performing word embedding on it.
6- [Dataset_two.ipynb] : pre-processing the second dataset and then vectorising then clustering it and finally performing word embedding on it.
7- [Evaluatetion.py] : contains the following functions :
    • Making  a golden standard (dictionary) out of QRELs  
    •	Key : query id.
    • Value : relevant documents ids.
    • Pre-processing QRELs .
    • Looping through the query_ids (the dictionary):
    • Getting the cleaned query and vectorising it.
    • Getting the relevant documents using the dictionary.
    • Calculating the cosine similarity between the query vector and each vector of our TFIDF matrix.
    • Ranking the results.
    • Calculating precision@10.
    • Calculating recall@10.
    • Calculating average precision.
    • Calculating reciprocal rank.
    • Calculate mean average precision. 
    • Calculate mean reciprocal rank.
    • Calculate average precision.
    • Calculate average recall.

8- [Evaluate_dataset_one.ipynb]: evaluating the first dataset before and after clustering
9- [Evaluate_dataset_two.ipynb]: evaluating the second dataset before and after clustering
10- [Tfidf_output] : folder containing the results of tfidf vectorization on both datasets
11- [queries]: folder containing the results of tfidf vectorization on both dataset quieries files
# Features

1- [Clustering.py]  : contains the following functions :
    • Clustering . 
    • Match .
    • Get_docs_of_one_cluster.
    • Cos_simi .
2- [Clustering_output]  : contains the output of clustering both datasets
    • Clustered documents.
    • Clustering image.
3- [Embedding.py]  : contains the following functions:
    • Embedding
    • Cos_similarity
4- [Embedding_output] : contains the output of word embedding both datasets
    • Embedded documents.
    • Embedded queries.  

### Clone the Repository

1. Open your terminal or command prompt.

2. Use the following command to clone the ProjectName repository:

git clone https://github.com/omranAK/IR_FINAL.git
