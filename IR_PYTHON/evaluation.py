from textProcessing import *
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter
import numpy as np
import main
import pandas as pd
import pickle
from num2words import num2words

class evaluation():
    
    def golden_standard(path):
        data = pd.read_json(path_or_buf=path, lines=True)
        output = {}
        for key, values in data['answer_pids'].items():
            values_list = [value for value in values]
            output[str(key)] = values_list
        return output
    
    
    def calculate_average_precision(model_output, gold_standard):
        ap_num = 0
        counter= 0
        for k in range(10):
            
            pred_set = set(model_output[:k+1])
            precision_at_k = len(pred_set & set(gold_standard)) / (k+1)
            # print("precision@" + str(k) +  ": " + str(precision_at_k))
            
            if k < len(model_output) and model_output[k] in gold_standard:
                rel_k = 1
                counter += 1
            else:
                rel_k = 0
            ap_num += precision_at_k * rel_k
        if counter == 0: 
            return 0  
        else:
            ap_at_k = ap_num / counter
        
        return ap_at_k
    
    
    
    def calculate_recall_at_k(model_output, gold_standard):
        counter= 0
        for k in range(10):
            if k < len(model_output) and model_output[k] in gold_standard:
                counter += 1
            
        return counter/len(gold_standard)
    
    
    
    def calculate_reciprocal_rank(model_output, gold_standard):
        reciprocal_rank = 0
        index = 1 
        for item in model_output:
            if item in gold_standard:
                reciprocal_rank = 1/ index
                break
            index += 1
        return reciprocal_rank