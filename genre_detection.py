import nltk
import json

with open("booksummaries/booksummaries.txt","r",encoding= 'utf8', errors='ignore') as f:
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

all_labels=[]
count2=0
for book in books:

    data=book['summary'] 
    words=nltk.word_tokenize(data)
    tagged_words=nltk.pos_tag(words)
    try:
        labels=json.loads(book['genre']).values()
    except:
        #print(book[metadata][2])
        count2+=1
    all_labels.extend(labels)
    #print(tagged_words, labels)


print(count,count2)
