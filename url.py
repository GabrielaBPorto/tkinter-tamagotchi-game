import urllib2
page = urllib2.urlopen("https://www.youtube.com/").read()
print page