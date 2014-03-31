#Author:  Qian Ding & Tigran Hakobyan 

# Determines the 3 countries with the most tweets that were not retweeted. 


import sys
import json
import codecs

def getTopTreeCountries (filename):
	
	# Opens the file to read.
	fp = file (filename, "r")
	
	# Creates a list of lines. 
	lines = fp.readlines()
	d = {}
	for eachLine in lines:	
		try:
			# Each lines is a tweet. 
			tweet = json.loads(eachLine)
			p = {}
			p = None
			# If tweet doesn't contain 'place' field
			# we ignore the tweet and go to the next tweet.  
			if not 'place' in tweet:
				pass
			else:
				# Saves 'retweeted' and 'retweet_count' fields.
				retweeted  = tweet['retweeted']
				retweetCount = tweet['retweet_count']
				
				# If tweet neven been retweeted and the count
				# of retweets is zero, we continue. 
				if retweeted == False and retweetCount == 0:
					p = tweet ['place']
					# Double checks to make sure 'place' is not None
					# in the tweet.
					if p != None:
						# Saves the country of the tweet.
						country  = p['country']
						# If the dictionary doens't contain a 
						# value with country key, we put it into 
						# the dictionary with value = 1.   
						if country not in d:		
							d[country] = 1
						else:
							# If it contains, then we increment the value 
							# for that country. 
							tempValue = d.get(country)
							tempValue = tempValue + 1
							d[country] = tempValue
				else:
					pass
					
		except ValueError:
			pass
			print "error has ocurred"
	
	# Sorts the dictionary items by value (value is the count) in reversed order.
	topTree  = sorted(d.iteritems(), key = lambda x : x[1], reverse = True)
	
	print ("These are the 3 countries with the most tweets that were not retweeted: ")
	print
	print ("1. " + topTree[0][0] + " : " + str(topTree[0][1]) + " tweets" )
	print ("2. " + topTree[1][0] + " : " + str(topTree[1][1]) + " tweets" )
	print ("3. " + topTree[2][0] + " : " + str(topTree[2][1]) + " tweets" )
	print

def main():
	getTopTreeCountries (sys.argv[1])

if __name__ == '__main__':
    main()