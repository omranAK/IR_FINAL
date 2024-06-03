class paths():
    ir = "D:\\fifth\\ir"
    project = 'D:\\fifth\\final_ir_final\\ir_project'
    desktop = "D:\\fifth\\final_ir_final\\desktopFile"
    
    dataset_one_collection = ir + '\\lotte\\lifestyle\\dev\\collection.tsv'
    processed_dataset_one = desktop + '\\pre_processing.tsv'
    tfidf_output = project + '\\tfidf_output\\'
    dataset_one_question_forum = ir + "\\lotte\\lifestyle\\dev\\questions.forum.tsv"
    processed_question_forum_one = project + '\\queries\\processed_qrs.tsv'
    dataset_one_model = project + "\\tfidf_output\\model.pickle"
    dataset_one_tfidf_matrix = project + "\\tfidf_output\\tfidf_docs.pickle"
    kmeans_output = project + "\\clustering_output"
    embedding_output = project + '\\embedding_output\\'
    embedded_dataset_one = project + '\\embedding_output\\embedded_docs_1.pickle'
    dataset_one_qas_forum = ir + "\\lotte\\lifestyle\\dev\\qas.forum.jsonl"
    clustered_dataset_one = project + '\\clustering_output\\docs_matrix_after_kmeans.pickle'
    
    
    dataset_two_collection = ir + '\\lotte\\recreation\\dev\\collection.tsv'
    processed_dataset_two = desktop + '\\ds_2_pre_processing.tsv'
    dataset_two_question_forum = ir + "\\lotte\\recreation\\dev\\questions.forum.tsv"
    processed_question_forum_two = project + '\\queries\\ds_2_processed_qrs.tsv'
    dataset_two_model = project + "\\tfidf_output\\model_2.pickle" 
    dataset_two_tfidf_matrix = project + "\\tfidf_output\\tfidf_docs_2.pickle"
    dataset_two_qas_forum = ir + "\\lotte\\recreation\\dev\\qas.forum.jsonl"
    clustered_dataset_two = project + '\\clustering_output\\docs_matrix_after_kmeans_2.pickle'
    embedded_dataset_two= project + '\\embedding_output\\embedded_docs_2.pickle'