import urllib.request
import http.cookiejar

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

webURLprefix = "https://www.nrc.gov/reading-rm/doc-collections/event-status/event/2017/2017"
webURLsuffix = "en.html"

date = input("Enter date in MMDD format: ")
datestring = str(date)
fullurl = webURLprefix + datestring + webURLsuffix

try:
    infile = opener.open(fullurl, timeout=15)
    newpage = infile.read().decode('utf-8')

except:
    newpage = ""
    print("We have an error")

if newpage.find("INDIAN POINT") >- 1:
    print("Indian Point found")
else:
    print("Indian Point not found")

print("Done")
