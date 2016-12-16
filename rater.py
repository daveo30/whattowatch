from mechanize import Browser
import json
import urllib2
import os


from os import walk
movies = []
for (dirpath, dirnames, filenames) in walk("/home/dojha/Videos"):
    movies.extend(dirnames)
    break
for movie in movies:
    print movie
    x=""
    curmovie= movie.replace(" ","+")
    for i in curmovie:
        if i=="." or i=="(" or i==")" or i=="," or i==":" or i==";" or i=="[":
            break
        x+=i
#req = urllib2.urlopen("http://www.omdbapi.com/?t=shawshank+redemption&y=&plot=short&r=json").read()
    try:
        req = urllib2.urlopen("http://www.omdbapi.com/?t="+x+"&y=&plot=short&r=json").read()
        moviedetjson=json.loads(req)
        print(moviedetjson['Title'])
        print(moviedetjson['imdbRating'])
    except:
        print "not found"
