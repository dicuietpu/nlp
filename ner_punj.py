
# coding: utf-8

# In[1]:


import nltk
import re
from nltk import word_tokenize
f= open("/home/akanksha/samplepunjabifile", "r")
f=f.read()
p = re.compile("[(,।):\-''?``''\"]")
f1 = p.sub(" ",f)
tok= word_tokenize(f1)
print(tok)
print("\n")

    #**Prefix name rule*********
def NER(tok):
    names=[]
    fullname=""
    #tokens=['ਸਿੱਖਾਂ','ਪਹਿਲੇ','ਸ੍ਰੀ','ਕਰਤਾਰ','ਸਿੰਘ','ਸੋਢੀ','ਅਮ੍ਰਿਤਸਰ','ਆਏ','ਸਨ','ਸ਼੍ਰੀਮਤੀ','ਆਸ਼ਾ','ਰਾਨੀ','ਫਰੋਜ਼ਪੁਰ','ਆਏ','ਸਨ','ਜਲਾਲਾਬਾਦ','ਉਹਨਾਂ','ਦਾ','ਜਨਮ','ਪੰਜਾਬ','ਵਿਖੇ','ਹੋਇਆ']
    prefixlist=['ਸ','ਸ੍ਰੀ','ਸ੍ਰ','ਡਾ','ਇੰ','ਪ੍ਰੋ','ਪ੍ਰਿ','ਸ਼੍ਰੀਮਤੀ','ਸ਼੍ਰੀਮਾਨ','ਡਾ','ਸਵਾਮੀ','ਗੁਰੂ','ਸ਼੍ਰੀ','ਪੰਡਤ']
    middlename=['ਕੁਮਾਰ', 'ਲਾਲ', 'ਕੌਰ', 'ਸਿੰਘ', 'ਕੁਮਾਰੀ', 'ਚੰਦ', 'ਬਾਲਾ','ਰਾਨੀ','ਨਾਥ','ਬਾਈ','ਦੇਵ']
    lastname=['ਅੱਗਰਵਾਲ','ਅਰੋੜਾ','ਬਰਾੜ','ਸੰਧੂ','ਸਿੱਧੂ','ਗੋਇਲ','ਸ਼ਰਮਾ','ਯਾਦਵ','ਬੇਦੀ','ਸੋਢੀ','ਭੰਡਾਰੀ']
    #Organization= ['ਕੰਪਨੀ','ਕਮੇਟੀ','ਕਲੱਬ','ਦਲ','ਬੋਰਡ','ਿਵਭਾਗ','ਆਰਗੇਨਾਈਜੇਸ਼ਨ','ਐਸੋਸੀਏਸ਼ਨ','ਯੂਨੀਅਨ','ਸਮਿਤੀ']
    places=['ਨਗਰ' ,'ਪੁਰ','ਗੜ੍ਹ','ਸਰ']
    for i in range(0,len(tok)):
        for j in range(0,len(prefixlist)):
            if tok[i]== prefixlist[j]:
                fullname= tok[i]+' '+tok[i+1]
                if tok[i+1] in prefixlist:
                    fullname= fullname +' '+tok[i+2]
                    if tok[i+3] in middlename:
                        fullname= fullname +' '+ tok[i+3]
                #print(fullname)

                if tok[i+2] in middlename:
                    fullname= fullname +' '+ tok[i+2]
                    #print(fullname)

                    if tok[i+3] in lastname:
                        fullname= fullname +' '+ tok[i+3]
                        #print(fullname) 

        if fullname!= "":
            if fullname not in names:
                names.append(fullname)
        fullname =""
    fullname=""
    for i in range(0,len(tok)):
        if tok[i] in middlename:
            fullname= tok[i-1]+" "+tok[i]
                    #print(fullname)

        if fullname!= "":
            if fullname not in names:
                names.append(fullname)
        fullname =""
    print("Names: ")
    print(list(set(names)))
    #***************location detection***************************
    import re
    loc=[]
    for i in range(0,len(tok)):
        if tok[i].endswith(u"ਪੁਰ") or tok[i].endswith(u"ਗੜ੍ਹ") or tok[i].endswith(u"ਸਰ") or tok[i].endswith(u"ਬਾਦ"):
            loc.append(tok[i])
            #print(loc)
        if tok[i] == "ਵਿਖੇ":
            loc.append(tok[i-1])
        if tok[i].endswith(u"ਨਗਰ") and tok[i]!= "ਨਗਰ":
            loc.append(tok[i])
    print("Locations: ")
    print(list(set(loc)))
    #**************************** DATE detection ***************************
    #************************FINAL**************************************
    #import re
    date=[]
    tempstr=""
    months=['ਜਨਵਰੀ','ਫਰਵਰੀ','ਮਾਰਚ','ਅਪ੍ਰੈਲ','ਮਈ','ਜੂਨ','ਜੁਲਾਈ','ਅਗਸਤ','ਸਤੰਬਰ','ਅਕਤੂਬਰ','ਨਵੰਬਰ','ਦਸੰਬਰ','ਸਿਤੰਬਰ','ਦਿਸੰਬਰ','ਫ਼ਰਵਰੀ']
    #random=['ਉਸ','ਦਾ','ਜਨਮ','02','ਜਨਵਰੀ','1996','ਨੂੰ','ਹੋਇਆ','ਅਤੇ','ਉਸ','ਦਾ','ਵਿਆਹ','23','ਮਈ','2020','ਵਿਚ','ਹੋਇਆ','20','ਅਗਸਤ','ਵਿਚ','ਹੋਇਆ','ਨਵੰਬਰ','1998','ਵਿਚ','ਹੋਇਆ','ਦਸੰਬਰ','22','ਵਿਚ','ਹੋਇਆ','ਅਕਤੂਬਰ','23','1997']
    for k in range(0,len(tok)):
        if tok[k] in months:
            if re.match(r"\d{4}",tok[k+1]):     # janvari 1996
                if re.match(r"\d{1,2}",tok[k-1]):
                    tempstr= tok[k-1]+" "
                tempstr= tempstr+ tok[k]+" "+tok[k+1]    #21 janvari 1996


            elif re.match(r"\d{1,2}",tok[k+1]):      #janvari 21 
                tempstr= tok[k]+" "+tok[k+1]
                if re.match(r"\d{4}",tok[k+2]):    #janvari 21 1996
                    tempstr= tempstr+" "+tok[k+2]

            elif re.match(r"\d{1,2}",tok[k-1]):     #22 janvari 
                tempstr= tok[k-1]+" "+tok[k]

        if tempstr!= "":
            if tempstr not in date:
                date.append(tempstr)
        tempstr =""
    print ("Dates: ")
    print(list(set(date)))
    return

NER(tok)

