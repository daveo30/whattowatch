from mechanize import Browser
import json
import urllib2
print "Enter movie name"
movie = raw_input()
movie= movie.replace(" ","+")
#req = urllib2.urlopen("http://www.omdbapi.com/?t=shawshank+redemption&y=&plot=short&r=json").read()
req = urllib2.urlopen("http://www.omdbapi.com/?t="+movie+"&y=&plot=short&r=json").read()
moviedetjson=json.loads(req)
print(moviedetjson['Title'])
print(moviedetjson['imdbRating'])
