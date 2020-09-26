import nltk
import json
from nltk.stem import LancasterStemmer

lancaster=LancasterStemmer()

with open("booksummaries.txt","r",encoding= 'utf8', errors='ignore') as f:
    contents= f.readlines()

books=[]
test_books=[]

count=0

for con in contents:
    fi=con.find('{')
    li=con.find('}')
    if fi==-1:
        count+=1
        dats=con.split('\t')
        test={}
        test['metadata']=dats[0:-1]
        test['summary']=dats[-1]
        test_books.append(test)
        continue
    metadata=con[0:fi]
    metadata_list=metadata.split('\t')
    #try:
        #print(metadata_list[2])
    #except:
        #pass
    #print(metadata_list)
    genre_info=con[fi:li+1]

    summary=con[li+1:]
    book_dict={}
    book_dict['genre']=genre_info
    book_dict['summary']=summary
    book_dict['metadata']=metadata
    books.append(book_dict)


#print(books.shape,test_books.shape)
x_train=[]
y_train=[]
summary_list=[]
all_labels=[]
count2=0
for book in books:
    try:
        data=book['summary'] 
        words=nltk.word_tokenize(data)
        words_from_summary=[lancaster.stem(i) for i in words]
        summary_list.append(words_from_summary)
        tagged_words=nltk.pos_tag(words)
        labels=json.loads(book['genre']).values()
        all_labels.extend(labels)
    except:
        #print(book[metadata][2])
        count2+=1
    
    #print(tagged_words, labels)


print(count,count2)
