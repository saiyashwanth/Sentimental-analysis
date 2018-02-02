import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize

stop_words = set(stopwords.words("english"))
f = open("text3.txt","r")  
neg = open("negative_words.txt","r")
posi = open("positive_words.txt","r")

positive = {}
negative = {}
frequency= {}

total_value =0.00;

def opposite(line):
	global total_value
	for word in line.split(' '):
		if word in positive:
			total_value = total_value - 2*positive[word]
		elif word in negative:
			total_value = total_value - 2*negative[word]


for line in posi:
	for word in word_tokenize(line):
		positive[word] = 1

for line in neg:
	for word in word_tokenize(line):
		negative[word] = -1

for line in f:						
	for word in line.split(' '):
		if word =='not':
			opposite(line)

	for word in word_tokenize(line):                   
		if word in stop_words:
			continue
		word.lower()                                
		if word not in frequency:									
			frequency[word] = 1										
		else:													
			frequency[word] += 1

for word in frequency:
	if word in positive:
		total_value = total_value + frequency[word]
	elif word in negative:
		total_value = total_value - frequency[word]

if total_value > 0:
	print("The product is good")
	print(total_value)
else:
	print("The product is not good")
	print(total_value)
