IR_Python project is python project for search engine  .
# Provide this cores :
**1**.[Main.py] contains end-points: <br/>
       &nbsp-@app.post("/api/user_query")<br/>
       &nbsp-@app.post("/api/match_to_cluster")<br/>
       &nbsp -@app.post("/api/embedding_match")<br/>

**2**- [service.py] contains the following services in the order: <br/>
  processing a query and then calling the cosine similarity function on the processed queries vector and the documents vectors te optain the right answers :<br/>
    -	Match.<br/>
    -	Match to clusters.<br/>
    -	Embedding match.<br/>

**3**- [Text_processing.py] conatins the main pre-processing functions<br/>
    • Reading dataset<br/>
    • Normalization <br/>
    • Converting to lowercase <br/>
    • Removing URLs<br/>
    • Removing punctuation<br/>
    • Converting numbers to words or deleting digits<br/>
    • Tokenization <br/>
    • Correct query<br/>
    • Removing stop words<br/>
    • Stemming <br/>

**4**- [Vectorization.py] contains:<br/>
    • TFIDFvectorizer<br/>
    • CosineSimilarity<br/>
**5**- [Dataset_one.ipynb] : pre-processing the first dataset and then vectorising then clustering it and finally performing word embedding on it.<br/>
**6**- [Dataset_two.ipynb] : pre-processing the second dataset and then vectorising then clustering it and finally performing word embedding on it.<br/>
**7**- [Evaluatetion.py] : contains the following functions :<br/>
    • Making  a golden standard (dictionary) out of QRELs  <br/>
    •	Key : query id.<br/>
    • Value : relevant documents ids.<br/>
    • Pre-processing QRELs .<br/>
    • Looping through the query_ids (the dictionary):<br/>
    • Getting the cleaned query and vectorising it.<br/>
    • Getting the relevant documents using the dictionary.<br/>
    • Calculating the cosine similarity between the query vector and each vector of our TFIDF matrix.<br/>
    • Ranking the results.<br/>
    • Calculating precision@10.<br/>
    • Calculating recall@10.<br/>
    • Calculating average precision.<br/>
    • Calculating reciprocal rank.<br/>
    • Calculate mean average precision. <br/>
    • Calculate mean reciprocal rank.<br/>
    • Calculate average precision.<br/>
    • Calculate average recall.<br/>

**8**- [Evaluate_dataset_one.ipynb]: evaluating the first dataset before and after clustering<br/>
**9**- [Evaluate_dataset_two.ipynb]: evaluating the second dataset before and after clustering<br/>
**10**- [Tfidf_output] : folder containing the results of tfidf vectorization on both datasets<br/>
**11**- [queries]: folder containing the results of tfidf vectorization on both dataset quieries files<br/>
# Features

1- [Clustering.py]  : contains the following functions :<br/>
    • Clustering . <br/>
    • Match .<br/>
    • Get_docs_of_one_cluster.<br/>
    • Cos_simi .<br/>
2- [Clustering_output]  : contains the output of clustering both datasets<br/>
    • Clustered documents.<br/>
    • Clustering image.<br/>
3- [Embedding.py]  : contains the following functions:<br/>
    • Embedding<br/>
    • Cos_similarity<br/>
4- [Embedding_output] : contains the output of word embedding both datasets<br/>
    • Embedded documents.<br/>
    • Embedded queries.  <br/>

### Clone the Repository<br/>

1. Open your terminal or command prompt.<br/>

2. Use the following command to clone the ProjectName repository:<br/>

git clone https://github.com/omranAK/IR_FINAL.git<br/>
