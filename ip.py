import urllib2
myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()
print myip
