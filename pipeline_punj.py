
# coding: utf-8

# In[69]:


import nltk
import re
from nltk import word_tokenize
from guess_language import guessLanguage
from nltk.corpus import indian
from nltk.tag import tnt


# In[81]:


def pipelineforpunjabi():
    f= open("/home/akanksha/samplepunjabifile", "r")
    f=f.read()
    p = re.compile("[(,।):\-''?``''\"]")             #punctuation removal
    f1 = p.sub("",f)
    tok= word_tokenize(f1)       #tokenization
    print(" Tokens: \n")
    print(tok)
    my_dict={}
    for x in tok:
        my_dict[x]=guessLanguage(x)      #language detection
    print(my_dict)
    f2= open("/home/akanksha/stopwordspun", "r")        #stopwords removal
    stopwords = [x.strip() for x in f2.readlines()]
    filtered_sentence = []

    for w in tok:
        if w not in stopwords:
            filtered_sentence.append(w)
    print("\n")
    print(" Stop words Removed: \n")
    print(filtered_sentence)
    print("\n")
    print(" After Stemming: \n")
    stemmed=[]
    for word in filtered_sentence:             #stemming
        if len(word) > 2:
            if word.endswith(u"ਆਂ" ):
                if word.endswith(u"ੀਆਂ" ):
                    word1 = re.sub(""u"ੀਆਂ""$",'ੀ', word)   
                    #break
                elif word.endswith(u"ਿਆਂ" ):
                    word1 = re.sub(""u"ਿਆਂ""$",'ੇ', word)   
                elif word.endswith(u"ੂਆਂ" ):
                    word1 = re.sub(""u"ੂਆਂ""$",'ੂ', word)      
            if word.endswith(u"ਾਂ" ):
                if word.endswith(u"ਵਾਂ" ):
                    word1 = re.sub(""u"ਵਾਂ""$",'', word)    
                elif word.endswith(u"ਾਂ" ):
                    word1 = re.sub(""u"ਾਂ""$",'', word)     
            if word.endswith(u"ੀਏ" ):
                word1 = re.sub(""u"ੀਏ""$",'ੀ', word)    
            if word.endswith(u"ੀਓ" ):
                word1 = re.sub(""u"ੀਓ""$",'ੀ', word)    
            if word.endswith(u"ਉਣ" ):
                word1 = re.sub(""u"ਉਣ""$",'', word) 
            if word.endswith(u"ੋਂ" ):
                word1 = re.sub(""u"ੋਂ""$",'', word) 
            if word.endswith(u"ੇ" ):
                word1 = re.sub(""u"ੇ""$",'ਾ', word) 
            if word.endswith(u"ੋ" ):
                word1 = re.sub(""u"ੋ""$",'', word) 
            if word.endswith(u"ਿਓ" ):
                word1 = re.sub(""u"ਿਓ""$",'ਾ', word)    
        
        stemmed.append(word)
    print(stemmed)
    my_dict1={}
    for i in stemmed:
        with open("/home/akanksha/punjabi_tagging") as openfile:      #POS tagging
            for line in openfile:
                
                for part in line.split():
                    part1 = part.split('_', 1)[0]
                    #print(part1)

                    if i == part1:

                        #print(i)
                        #print (part)
                        my_dict1[part.split('_', 1)[0]]=part.split('_', 1)[1]
                        break #this 1 indicates limit on number of splits
                    else:
                        my_dict1[i]='UNKNOWN'


    print(" POS tagging: \n")
    print(my_dict1)
    lisst = my_dict1.items()
    grammar="Chunk:{<N_NN>+<PSP>}"       #CHUNKING
    parser=nltk.RegexpParser(grammar)
    output=parser.parse(lisst)
    print("Chunking: \n")
    print(output)


# In[82]:


pipelineforpunjabi()

