import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize

stop_words = set(stopwords.words("english"))
f = open("text3.txt","r")                                #reading file which contain reviews of customer



index = {}                                                #declaring dictionary which will contain  
											              #our indexed words
index['love'] = 5
index['good'] = 4
index['best'] = 5
index['better'] = 2
index['worst'] = -5
index['bad'] = -4
index['amazing'] = 5
index['enjoying'] = 3
index['sexy'] = 4
index['worthful'] = 3
index['beautiful'] = 3
index['happy'] = 5
index['unhappy'] = -4
index['lame'] = -5
index['well'] = 2
index['satisfied'] = 2
index['waste'] = -4
index['champion'] = 5
index['ground-breaking'] = 5
index['cheap'] = -3
index['cheated'] = -3
index['duplicate'] = -4
index['foulty'] = -4
index['poor'] = -5
index['awful'] = -3
index['fake'] = -4
index['cheapest'] = -4
index['nice'] = 3
index['stopped'] = -3

total_value = 0.00;
deno=0.01
do_not = "don't"
mean = 0.00

def opposite(line):                                   #to handle case like not good, don't recommended      
	for word in line.split(' '):
		if word in index:
			global total_value
			total_value = total_value - 2*index[word]
		
                                      
freq = {}                                                       #declaring a dictionary  

for line in f:											        #reading one line at a time
	for word in word_tokenize(line):                               #spliting the words from line
		if word in stop_words:
			continue
		word.lower()
#		if word == 'not' or word == do_not:
#			opposite(line)                                
		if word not in freq:									#
			freq[word] = 1										#
		else:													#counting frequency of a words
			freq[word] += 1										#



for word in freq:                                                #this will calculate how many times index words 
	if word in index:                                            #are repeated and as per that it calculate the points for the product
		total_value=total_value + index[word]*freq[word]
		deno= deno + 5*freq[word];
	
mean = total_value/deno;                                         # here we are calculating the mean value;

if mean<0:														#if mean value is +ve the product is good else
	print("Product not Good")									#the product is not good
	print(mean)
else:
	print("product is Good ")
	print(mean)

