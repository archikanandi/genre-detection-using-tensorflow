import nltk

with open("booksummaries.txt","r",encoding= 'utf8', errors='ignore') as f:
	contents= f.readlines()

count=0

for con in contents:
	fi=con.find('{')
	li=con.find('}')
	if fi==-1:
		count+=1
		continue
	metadata=con[0:fi]
	metadata_list=metadata.split('\t')
	try:
		print(metadata_list[2])
	except:
		pass
	#print(metadata_list)
	genre_info=con[fi:li+1]
	summary=con[li+1:]
	#print(metadata)

print(count)
'''
token= nltk.word_tokenize(text)

print(token)

tag = nltk.pos_tag(token)

print(tag)

attribute= nltk.chunk.ne_chunk(tag)

print(attribute)'''