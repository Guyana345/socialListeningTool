#http://ajax.googleapi.com/ajax/services/search/web?v=1.0&q=
import urllib
import json

examplesearch ='stamford'
encoded = urllib.quote (exampleSearch)

rewData = urllib.urlopen('http://ajax.googleapi.com/ajax/services/search/web?v=1.0&q='+encoded).read()

jsonData = json.loads(rawData)
searchResults = jasonData['responseData']['results']

for er in searchResults:
	title =er['title']
	link = er['url']
	print title
	print link 
	print '''


	   '''
