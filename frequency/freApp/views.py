from django.shortcuts import render
from .forms import *
from .models import *
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Create your views here.

#######url#######

def frequency(request):
    return render(request,'index.html')

def results(request):

    ###for save url link
    u=request.POST.get("nl")
    s=freq(ulink=u)
    s.save()

    ###procesing
    url=str(request.POST["ul"])

    r = requests.get(url)#put into the container
    htmlContent = r.content

    soup=BeautifulSoup(htmlContent,'html.parser')

    #para=soup.find_all('p')#find all paragraph

    text=soup.get_text(strip=True)

    #word=word_tokenize(text) ##convert into word-token comma separetd
    #cts=nltk.FreqDist(word)

    text2=re.sub("[^A-Za-z]+"," ",text)

    ###counter for count top ten frequent word after removing common words
    # word_counts=Counter(text2)
    # top_ten=word_counts.most_common(10)

    file=open('templates/1-1000.txt','r')####open 1000 common words file
    con=file.read()
    file.close()

    clean=[word for word in text2.split() if word not in con]

    # stop_words=set(stopwords.words(con))
    # filteredlist=[]
    # words=text2.split()
    #
    # for w in words:
    #     if w not in stop_words:
    #         filteredlist.append(w)




    # filteredlist=[]
    # conlen=len(con.split())
    # for i in range(len(text2.split())):
    #     for j in range(conlen):
    #         if text2.split()[i]!=con.split()[j] and j==conlen-1:
    #             filteredlist.append(text2.split()[i])

    ##counter for count top ten frequent word after removing common words
    word_counts=Counter(clean)
    top_ten=word_counts.most_common(10)


    return render(request,'result.html',{'url0':top_ten[0],
                                         'url1':top_ten[1],
                                         'url2': top_ten[2],
                                         'url3': top_ten[3],
                                         'url4': top_ten[4],
                                         'url5': top_ten[5],
                                         'url6': top_ten[6],
                                         'url7': top_ten[7],
                                         'url8': top_ten[8],
                                         'url9': top_ten[9]})




