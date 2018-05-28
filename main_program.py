
# coding: utf-8

# In[21]:


import numpy as np
import nltk
import re
from nltk import word_tokenize, sent_tokenize
from tkinter.filedialog import askopenfilename
from nltk.util import ngrams as nltk_ngrams
from guess_language import guessLanguage
from tkinter import *
from PIL import ImageTk, Image
import sys
           
window = Tk()
window.title("Document Similarity Checker")
window.geometry('700x600')
window.configure(background='white')
window.resizable(width=False, height=False)


# In[22]:


def process1(file):
    with open(file,"r") as f:
        text=f.read()
        text=re.sub('।',' ।',text)
        
        lang=guessLanguage(text)
        if (lang!='pa'):
            er="Error: Doc is of a language other than punjabi"
            print(er)
            lb5=Label(window,text=er)
            lb5.place(x=35,y=450)
            sys.quit()  
    #**********************************STOP WORD REMOVAL & PUNCTUATION REMOVAL***************************
    p = re.compile("[\.(,।)\-''?``''\"]")
    f1 = p.sub(" ",text)

    tok= word_tokenize(f1)

    f2= open("/home/simar/Downloads/stopwordspun", "r")
    stopwords = [x.strip() for x in f2.readlines()]
    filtered_sentence = []

    for w in tok:
        if w not in stopwords:
            filtered_sentence.append(w)

    #print("STOP WORD & PUNCTUATION REMOVAL\n")
    #print(filtered_sentence)


    #*******************************Rule based STEMMING***********************************************
   
    def generate_stem_words(word):
        if len(word) > 2:
            if word.endswith(u"ਆਂ" ):
                if word.endswith(u"ੀਆਂ" ):
                    word = re.sub(""u"ੀਆਂ""$",'ੀ', word)   #kudiyaan
                    #break
                elif word.endswith(u"ਿਆਂ" ):
                    word = re.sub(""u"ਿਆਂ""$",'ੇ', word)   #bachcheyan
                elif word.endswith(u"ੂਆਂ" ):
                    word = re.sub(""u"ੂਆਂ""$",'ੂ', word)      #LADDUAN
            if word.endswith(u"ਾਂ" ):
                if word.endswith(u"ਵਾਂ" ):
                    word = re.sub(""u"ਵਾਂ""$",'', word)    #duaavaan
                elif word.endswith(u"ਾਂ" ):
                    word = re.sub(""u"ਾਂ""$",'', word)     #taaraan
            if word.endswith(u"ੀਏ" ):
                word = re.sub(""u"ੀਏ""$",'ੀ', word)    #kudiye
            if word.endswith(u"ੀਓ" ):
                word = re.sub(""u"ੀਓ""$",'ੀ', word)    #kudio
            if word.endswith(u"ਉਣ" ):
                word = re.sub(""u"ਉਣ""$",'', word) #banaaun
            if word.endswith(u"ੋਂ" ):
                word = re.sub(""u"ੋਂ""$",'', word) #bazaaron
            if word.endswith(u"ੇ" ):
                word = re.sub(""u"ੇ""$",'ਾ', word) #kutte
            if word.endswith(u"ੋ" ):
                word = re.sub(""u"ੋ""$",'', word) #hasso
            if word.endswith(u"ਿਓ" ):
                word = re.sub(""u"ਿਓ""$",'ਾ', word)    #bacheyo
        return(word)

    #print("\nStemming \n")
    word_list=[]
    for w in filtered_sentence:
        word_list.append(generate_stem_words(w))

    count=nltk.defaultdict(int)
    for w in word_list:
        count[w] +=1
    
    return count;


# In[23]:


def process2(file):
    with open(file,"r") as f:
        text=f.read()
        lang=guessLanguage(text)
        if (lang!='pa'):
            er="Error: Doc is of a language other than punjabi"
            print(er)
            lb4=Label(window,text=er)
            lb4.place(x=365,y=450)
            sys.quit()        
    #text=re.sub('।',' ।',text)
    #**********************************STOP WORD REMOVAL & PUNCTUATION REMOVAL***************************
    p = re.compile("[\.()\-''?``''\"]")
    f1 = p.sub(" ",text)
    #f1=text
    tok= sent_tokenize(f1)
    #print(tok)

    f2= open("/home/simar/Downloads/stopwordspun", "r")
    stopwords = [x.strip() for x in f2.readlines()]
    filtered_sentence = []

    for w in tok:
        m=w.rsplit(' ')
        for i in m:
            if i not in stopwords:
                filtered_sentence.append(i)

    #print("STOP WORD & PUNCTUATION REMOVAL\n")
    #print(filtered_sentence)


    #*******************************Rule based STEMMING***********************************************
   
    def generate_stem_words(word):
        if len(word) > 2:
            if word.endswith(u"ਆਂ" ):
                if word.endswith(u"ੀਆਂ" ):
                    word = re.sub(""u"ੀਆਂ""$",'ੀ', word)   #kudiyaan
                    #break
                elif word.endswith(u"ਿਆਂ" ):
                    word = re.sub(""u"ਿਆਂ""$",'ੇ', word)   #bachcheyan
                elif word.endswith(u"ੂਆਂ" ):
                    word = re.sub(""u"ੂਆਂ""$",'ੂ', word)      #LADDUAN
            if word.endswith(u"ਾਂ" ):
                if word.endswith(u"ਵਾਂ" ):
                    word = re.sub(""u"ਵਾਂ""$",'', word)    #duaavaan
                elif word.endswith(u"ਾਂ" ):
                    word = re.sub(""u"ਾਂ""$",'', word)     #taaraan
            if word.endswith(u"ੀਏ" ):
                word = re.sub(""u"ੀਏ""$",'ੀ', word)    #kudiye
            if word.endswith(u"ੀਓ" ):
                word = re.sub(""u"ੀਓ""$",'ੀ', word)    #kudio
            if word.endswith(u"ਉਣ" ):
                word = re.sub(""u"ਉਣ""$",'', word) #banaaun
            if word.endswith(u"ੋਂ" ):
                word = re.sub(""u"ੋਂ""$",'', word) #bazaaron
            if word.endswith(u"ੇ" ):
                word = re.sub(""u"ੇ""$",'ਾ', word) #kutte
            if word.endswith(u"ੋ" ):
                word = re.sub(""u"ੋ""$",'', word) #hasso
            if word.endswith(u"ਿਓ" ):
                word = re.sub(""u"ਿਓ""$",'ਾ', word)    #bacheyo
        return(word)

    #print("\nStemming \n")
    word_list=[]
    for w in filtered_sentence:
        word_list.append(generate_stem_words(w))

    return word_list


# In[24]:


def cos_sim(a,b):
    sim=1-nltk.cluster.cosine_distance(a,b)
    return sim

def getSimilarity(dict1,dict2):
    all_words_list=[]
    for key in dict1:
        all_words_list.append(key)
    for key in dict2:
        all_words_list.append(key)
    all_words_list_size=len(all_words_list)
    
    v1=np.zeros(all_words_list_size, dtype=np.int)
    v2=np.zeros(all_words_list_size, dtype=np.int)
    i=0
    for (key) in all_words_list:
        v1[i]=dict1.get(key,0)
        v2[i]=dict2.get(key,0)
        i=i+1
    return cos_sim(v1,v2);


# In[25]:


def common_ngram_txt(tokens1,tokens2,size):
    #print('Checking ngram length {}'.format(size))
    ng1=set(nltk_ngrams(tokens1.split(), size))
    
    global len1
    len1=len(ng1)
    ng2=set(nltk_ngrams(tokens2.split(), size))
    len2=len(ng2)
    
    #print(len1)
    match=set.intersection(ng1,ng2)
   
    len3=len(match)
    #print('..found {}'.format(len(match)))
 
    return match


# In[26]:


text1=""
text2=""
from PIL import ImageTk, Image
def retrieve_input1():
    try:
        #Using try in case user types in unknown file or closes without choosing a file.
        name1 = askopenfilename(initialdir="/home/simar/Downloads",
                               filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                               title = "Choose a file"
                               )
        global text1
        text1=name1
        T1 = Text(window, height=7, width=20)
        T1.insert(END,text1)
        T1.place(x=50,y=210)
        lb3=Label(window,image=img1)
        lb3.place(x=100,y=270)

        print(name1)
        print("File 1 uploaded")
    
    except:
        print("No file exists")


def retrieve_input2():
    try:
        #Using try in case user types in unknown file or closes without choosing a file.
        name2 = askopenfilename(initialdir="/home/simar/Downloads",
                               filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                               title = "Choose a file"
                               )
        print(name2)
        global text2
        text2=name2
        T2 = Text(window, height=7, width=20)
        T2.insert(END,text2)
        T2.place(x=500,y=210)
        lb4=Label(window,image=img1)
        lb4.place(x=550,y=270)
        print(name2)
        print("File 2 uploaded")

    except:
        print("No file exists")

        
def show_result_sim(a,b):
    dict1=process1(a)
    dict2=process1(b)
    result= getSimilarity(dict1,dict2)
    result1=result*100
    print("Similarity = {}%".format(result1))
    lbl2 = Label(window, text="Similarity = {:0.5}%".format(result1), font=("Oswald", 15),bg='white')
    lbl2.place(x=90,y=450)
    
def show_result_plag(a,b):
    list1=process2(a)
    list2=process2(b)
    s1=""
    for i in list1:
        s1=s1+" "
        s1=s1+i
        
    s2=""
    for i in list2:
        s2=s2+" "
        s2=s2+i
    x=common_ngram_txt(s1,s2,size=5)
    acc= len(x)/len1*100
    print("Plagiarism = {:0.5}%".format(acc))
    lbl2 = Label(window, text="Plagiarism = {:0.5}%".format(acc), font=("Oswald", 15),bg='white')
    lbl2.place(x=390,y=450)


img=ImageTk.PhotoImage(Image.open("/home/simar/Downloads/pic01.png"))
lb1=Label(window,image=img)
lb1.pack()

lbl = Label(window, text="DOCUMENT SIMILARITY CHECKER", font=("Oswald", 20), bg='white')
lbl.place(x=160,y=50)

btn1 = Button(window, text="Upload Doc1", command=retrieve_input1, width=10, height=2, bg="lightskyblue",fg="white")
btn1.place(x=50, y=150)
btn1.config(font=('Oswald', 15, 'bold'))

img1=ImageTk.PhotoImage(Image.open("/home/simar/Downloads/pic6.jpg"))
#img1.resize(100,100)

btn2 = Button(window, text="Upload Doc2", command=retrieve_input2, width=10, height=2, bg="lightskyblue",fg="white")
btn2.place(x=500, y=150)
btn2.config(font=('Oswald', 15, 'bold'))


btn3 = Button(window, text="Check Similarity", command=lambda: show_result_sim(text1,text2), width=20, height=2, bg="dodgerblue",fg="white")
btn3.place(x=75, y=375)
btn3.config(font=('Oswald', 15, 'bold'))

btn4 = Button(window, text="Check Plagiarism", command=lambda: show_result_plag(text1,text2), width=20, height=2, bg="dodgerblue",fg="white")
btn4.place(x=365, y=375)
btn4.config(font=('Oswald', 15, 'bold'))


window.mainloop()

