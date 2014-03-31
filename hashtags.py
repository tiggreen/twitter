#Author:  Qian Ding & Tigran Hakobyan 

# Determines the top 10 hashtags.


import sys
import json
import codecs

def getTopTenHashtags (filename):

	fp = file (filename, "r")
	lines = fp.readlines()
	d = {}
	for eachLine in lines:	
		try:
			tweet = json.loads(eachLine)
			# If tweet doesn't contain 'entities' field
			# we ignore the tweet and go to the next tweet.
			if not 'entities' in tweet:
				pass
			else:
				entities  = tweet['entities']
				# 'hashtags' is list a in 'entities' field of
				# tweet.
				if not 'hashtags' in entities:
					pass	
				else:
					hashtags = entities['hashtags']
					# If hashtags is empty we can ignore the current tweet.
					if not hashtags:
						pass
					else:
						# Tweet can contain multiple hashtags.
						for hsh in hashtags:
							# In this program we assume that 
							# hashtags are not case sensitive. 
							txt = hsh['text'].lower()
							if txt not in d:
								d[txt] = 1
							else:
								tempValue = d.get(txt)
								tempValue = tempValue + 1
								d[txt] = tempValue
		except ValueError:
			pass
			print "error has ocurred"
	# Sorts the dictionary items by value (value is the hashtag's count) in reversed order.
	topTree  = sorted(d.iteritems(), key = lambda x : x[1], reverse = True)
	
	print ("These are the top ten hashtags: ")
	print
	i = 1;
	for e in topTree[:10]:
		print (str(i) + ". " + e[0])
		i = i + 1
	print

def main():
	getTopTenHashtags (sys.argv[1])

if __name__ == '__main__':
    main()