import nltk
import pandas as pd
import re
from nltk.corpus import words
#import string
#import spacy
from nltk.metrics.distance  import edit_distance
#from gensim.parsing.preprocessing import remove_stopwords
from io import StringIO
from nltk.tokenize import RegexpTokenizer, TreebankWordTokenizer, TweetTokenizer, TreebankWordDetokenizer
#from nltk.tokenize import word_tokenize
from nltk.corpus   import stopwords
from nltk.stem     import PorterStemmer
from num2words import num2words
from nltk.stem import WordNetLemmatizer
#from functools import reduce


class textProcessing():
    #normalize
    #Converting to lowercase
    #Removing URLs
    #Removing non-word and non-whitespace 
    #Removing digits OR convert digits to words and clean unwanted numeric charcters
    #Tokenization
    #Stopword Removal
    #Stemming
    #

    def readDataset(path : str):
        return pd.read_csv(path ,encoding='utf-8' ,sep='\t')
    
    def normalization(text):
        text = text.replace(r'$', ' dollar ', regex=True)
        text = text.replace(r'%', ' percent ', regex=True)
        return text
    
    
    def toLowercase(text):
        text = text.apply(lambda x: x.lower() if isinstance(x, str) else x)
        return text
    
    
    def delete_url(text):
        text = text.replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
        return text
    

    def delete_punctuation(text):
        text = text.replace(r'[^\w\s]', '', regex=True)
        return text
    
    
    def delete_numbers(text):
        text = text.replace(r'[0-9]+', '', regex=True)
        return text
    
    def convertNumToWords(text):
        words = []
        for word in text.split():
            if word.isdigit():
                if word == '¹':
                    word = word.replace('¹', '1')  # Replace superscript '¹' with '1'
                elif word == '²':   
                    word = word.replace('²', '2')
                elif word == '³':   
                    word = word.replace('³', '3') 
                elif word == '⁴':   
                    word = word.replace('⁴', '4')  
                elif word == '⁵':   
                    word = word.replace('⁵', '5') 
                elif word == '⁶':   
                    word = word.replace('⁶', '6')
                elif word == '⁷':   
                    word = word.replace('⁷', '7')
                elif word == '⁸':   
                    word = word.replace('⁸', '8')
                elif word == '⁹':   
                    word = word.replace('⁹', '9')
                elif word == '⁶₄':   
                    word = word.replace('⁶₄', '64')   
                elif word == '①':   
                    word = word.replace('①', '1')
                elif word == '②' :   
                    word = word.replace('②' , '2')
                elif word == '③' :   
                    word = word.replace('③' , '3')
                elif word == '➀':   
                    word = word.replace('➀', '1') 
                elif word == '➁':   
                    word = word.replace('➁', '2')
                elif word == '➂':   
                    word = word.replace('➂', '3')
                elif word == '➃':   
                    word = word.replace('➃', '4')
                elif word == '➄':   
                    word = word.replace('➄', '5')
                elif word == '➅':   
                    word = word.replace('➅', '6')
                elif word == '➆':   
                    word = word.replace('➆', '7')
                elif word == '➇':   
                    word = word.replace('➇', '8')
                elif word == '4²':   
                    word = word.replace('4²', '42')
                elif word == '20²':   
                    word = word.replace('20²', '202')
                elif word == '100²':   
                    word = word.replace('100²', '1002')
                elif word == '2²':   
                    word = word.replace('2²', '22')
                elif word == '3²':   
                    word = word.replace('3²', '32')
                elif word == '10²':   
                    word = word.replace('10²', '102')
                elif word == '180⁰':   
                    word = word.replace('180⁰', '180')
                elif word == '1²2²3²':   
                    word = word.replace('1²2²3²', '122232')
                elif word == '³₂':   
                    word = word.replace('³₂', '32')
                elif word == '⁶₂':   
                    word = word.replace('⁶₂', '62')
                elif word == '⁹₂':   
                    word = word.replace('⁹₂', '92')
                elif word == '⁷₂':   
                    word = word.replace('⁷₂', '72')
                elif word == '⁵₂':   
                    word = word.replace('⁵₂', '52')
                elif word == '²₄':   
                    word = word.replace('²₄', '24')
                elif word == '⁴₄':   
                    word = word.replace('⁴₄', '44')
                elif word == '³₁':   
                    word = word.replace('³₁', '31')
                elif word == '⁴₃':   
                    word = word.replace('⁴₃', '43')
                elif word == '⁹₈':   
                    word = word.replace('⁹₈', '98')
                elif word == '⁸¹₆₄':   
                    word = word.replace('⁸¹₆₄', '8164')
                elif word == '⁵₄':   
                    word = word.replace('⁵₄', '54')
                elif word == '³₄':   
                    word = word.replace('³₄', '34')
                elif word == '¹⁰₉':   
                    word = word.replace('¹⁰₉', '109')
                elif word == '⁴₆':   
                    word = word.replace('⁴₆', '46')
                elif word == '¹²2':   
                    word = word.replace('¹²2', '122')
                elif word == '¹²2¹²':   
                    word = word.replace('¹²2¹²', '12212')
                elif word == '2³':   
                    word = word.replace('2³', '23')
                elif word == '2¹¹²':   
                    word = word.replace('2¹¹²', '2112')
                elif word == '0125²':   
                    word = word.replace('0125²', '01252')
                elif word == '15²':   
                    word = word.replace('15²', '152')
                elif word == '25²':   
                    word = word.replace('25²', '252')
                elif word == '41021000²':   
                    word = word.replace('41021000²', '410210002')
                elif word == '0205²':   
                    word = word.replace('0205²', '02052')
                elif word == '14²':   
                    word = word.replace('14²', '142')
                elif word == '¹₁₆':   
                    word = word.replace('¹₁₆', '116')
                elif word == '³₈':   
                    word = word.replace('³₈', '38')
                elif word == '47³⁴':   
                    word = word.replace('47³⁴', '4734')
                elif word == '81¹²':   
                    word = word.replace('81¹²', '8112')
                elif word == '3³⁴':   
                    word = word.replace('3³⁴', '334')
                elif word == '240230²':   
                    word = word.replace('240230²', '2402302')
                elif word == '01²':   
                    word = word.replace('01²', '012')
                elif word == '32²':   
                    word = word.replace('32²', '322')
                elif word == '254²':   
                    word = word.replace('254²', '2542')
                elif word == '8661¹':   
                    word = word.replace('8661¹', '86611')
                elif word == '43¹':   
                    word = word.replace('43¹', '431')
                elif word == '75²':   
                    word = word.replace('75²', '752')
                elif word == '4²2000':
                    word =  word.replace('4²2000','42000')
                elif word == '2³8':
                    word = word.replace('2³8','28')
                elif word == '3³27':
                    word = word.replace('3³27','327')
                elif word == '3²2000':
                    word = word.replace('3²2000','32000')
                elif word == '6³':
                    word = word.replace('6³','6')
                elif word == '10³':
                    word = word.replace('10³','10')
                # elif word == '3³27':
                #     word = word.replace('3³27','327')
                # elif word == '3³27':
                #     word = word.replace('3³27','327')
                # elif word == '3³27':
                #     word = word.replace('3³27','327')                    
                    
                word = num2words(int(word))
            elif re.match(r'^\d+/\d+$', word):
                numerator, denominator = map(int, word.split('/'))
                word = f"{num2words(numerator)} over {num2words(denominator)}"
            words.append(word)
        return ' '.join(words)


    def delete_dates_and_times(text):
        text = text.replace(r'\b\d{1,4}[-/]\d{1,2}[-/]\d{1,4}\b|\b\d{1,2}[-/]\d{1,2}[-/]\d{1,4}\b|\b\d{1,2}:\d{1,2}(:\d{1,2})?( [APMapm]+)?\b', '', regex=True)
        return text

    
        
    def tokenize_and_remove_stopwords(text):
        stop_words = set(stopwords.words('english'))
 
        tokenizer = TweetTokenizer()
        token=tokenizer.tokenize(text)

        filtered_sentence = []
 
        for w in token:
            if w not in stop_words:
                filtered_sentence.append(w)
        
        return filtered_sentence
    
    def correct_query(text):
        correct_words = words.words() 
        correct = []
        for word in text: 
            temp = [(edit_distance(word, w), w) for w in correct_words if w[0] == word[0]] 

            if temp:
                word1 = sorted(temp, key=lambda val: val[0])[0][1]
                correct.append(word1)
            else:
                # Handle the case when temp is empty (no correct words found)
                correct.append(word)  # Add the original word without correction
        return correct


    def stemming(tokenized_text):
        stemmer = PorterStemmer()
        after_stemming = [stemmer.stem(word) for word in tokenized_text]  
        return after_stemming
    
    
    
    def lemmatization(steemed):
        wnl = WordNetLemmatizer()
        after_lemma = [wnl.lemmatize(word) for word in steemed]  
        return after_lemma
    
    
    
    def ds_pre_processing1(path):

        text = textProcessing.readDataset(path)
        text.columns=['text']
        text=text['text']
        text = textProcessing.normalization(text)
        text = textProcessing.toLowercase(text)
        text = textProcessing.delete_url(text)
        text = textProcessing.delete_punctuation(text)
        text = textProcessing.delete_dates_and_times(text)
        #text =  textProcessing.delete_numbers(text)
        text = text.apply(textProcessing.convertNumToWords)
        text = text.apply(textProcessing.tokenize_and_remove_stopwords)
        text = text.apply(textProcessing.stemming)
        return text
    
    
    def ds_pre_processing2(path):

        text = textProcessing.readDataset(path)
        text.columns=['text']
        text=text['text']
        text = textProcessing.normalization(text)
        text = textProcessing.toLowercase(text)
        text = textProcessing.delete_url(text)
        text = textProcessing.delete_punctuation(text)
        text = textProcessing.delete_dates_and_times(text)
        text =  textProcessing.delete_numbers(text)
        #text = text.apply(textProcessing.convertNumToWords)
        text = text.apply(textProcessing.tokenize_and_remove_stopwords)
        text = text.apply(textProcessing.stemming)
        return text
    
    def qry_pre_processing(query):
        query = ''' h
                '''+query
        StringData = StringIO(query)
        text = pd.read_csv(StringData, sep =";")
        text.columns = ['text']
        text=text['text']
        text = textProcessing.normalization(text)
        text = textProcessing.toLowercase(text)
        text = textProcessing.delete_url(text)
        text = textProcessing.delete_punctuation(text)
        text = textProcessing.delete_dates_and_times(text)
        text = text.apply(textProcessing.convertNumToWords)
        text = text.apply(textProcessing.tokenize_and_remove_stopwords)
        text = text.apply(textProcessing.correct_query)
        text = text.apply(textProcessing.stemming)
        return text
    