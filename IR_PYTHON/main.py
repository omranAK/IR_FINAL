from fastapi import FastAPI,Body,Request
from service import *
import pickle
from pydantic import BaseModel
from paths import *

class userQuery(BaseModel):
    ds_num: int
    qry : str

app = FastAPI()

@app.get("/")
def root():
    return "Hello world!!!!"

 

@app.post("/api/user_query")

async def user_query(userQuery : userQuery):
    #process query - get processed dataset - cosine sim - return cosine sim
    if userQuery.ds_num == 1:
        ds_path = paths.dataset_one_collection
        model_path = paths.dataset_one_model
        matrix_path = paths.dataset_one_tfidf_matrix
    elif userQuery.ds_num == 2:
        ds_path = paths.dataset_two_collection
        model_path = paths.dataset_two_model
        matrix_path = paths.dataset_two_tfidf_matrix
    
    response = service.match(ds_path, userQuery.qry,  model_path, matrix_path)  
    return response 



@app.post("/api/match_to_cluster")

async def match_to_clusters(userQuery : userQuery):
    
    if userQuery.ds_num == 1:
        ds_path = paths.dataset_one_collection
        model_path = paths.dataset_one_model
        matrix_path = paths.dataset_one_tfidf_matrix
        clusters_path = paths.clustered_dataset_one
    elif userQuery.ds_num == 2:
        ds_path = paths.dataset_two_collection
        model_path = paths.dataset_two_model
        matrix_path = paths.dataset_two_tfidf_matrix
        clusters_path = paths.clustered_dataset_two
    response = service.match_to_clusters(ds_path, userQuery.qry, model_path, matrix_path, clusters_path)
    
    return response

def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()


@app.post("/api/embedding_match")
async def embedding_match(userQuery : userQuery):
    
    if userQuery.ds_num == 1:
        ds_path = paths.dataset_one_collection
        embd_path = paths.embedded_dataset_one  
    elif userQuery.ds_num == 2:
        ds_path = paths.dataset_two_collection
        embd_path = paths.embedded_dataset_two
        
    response = service.embedding_match(ds_path, userQuery.qry, embd_path)
    
    return response