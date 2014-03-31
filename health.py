#Author:  Qian Ding & Tigran Hakobyan 

# Determines how many tweets mention something related to health.


import sys
import json
import codecs
from sets import Set

def getHealthTweets (filename):

	fp = file (filename, "r")
	lines = fp.readlines()
	d = {}
	cnt = 0 
	# A dictionary which contains health related words
	healthDict = Set(['health','hospital' 'medicine','medical', 'diagnostic',
	'disability', 'drug', 'epidemic', 'genetics', 'headache', 'healthy',
	'hygiene', 'hygienic', 'immunity', 'immunization', 'infection', 'breath', 'calorie', 
	'circulation', 'inherent', 'medication', 'muscle', 'nicotine', 'nutrition',
	'pharmacy', 'pregnancy', 'radiation', 'sex', 'skin', 'stress', 'symptom', 'therapy',
	'trauma', 'treatment','unhealthy', 'vaccination','virus', 'vitamin'
	 ])
	for eachLine in lines:	
		try:
			tweet = json.loads(eachLine)
			# if tweet doesn't contain 'text' field
			# we ignore the tweet. 
			if not 'text' in tweet:
				pass
			else:
				# Makes the text of a tweet lowercase.
				text  = tweet['text'].lower()
				# Creates a list of words from the text. 
				# Words are splitted by space. 
				textWords = text.split()
				
				# if the intersection of the health dictionary and the list of 
				# words of the tweet is not empty, we assume that tweet mentions
				# something related to health. 
				
				found = Set(textWords).intersection(healthDict)
				if found:
					cnt = cnt + 1
					
		except ValueError:
			pass
			print "error has ocurred"

	print ("Here is the count of tweets that mention something related to health: ")
	print(cnt)

def main():
	getHealthTweets (sys.argv[1])

if __name__ == '__main__':
    main()