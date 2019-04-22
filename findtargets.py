import urllib.request
import http.cookiejar

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

webURLprefix = "https://www.nrc.gov/reading-rm/doc-collections/event-status/event/2017/2017"
webURLsuffix = "en.html"
outfilename = "output.txt"

target = input("Enter target string")
targetstr = str(target)

for month in range(1, 13):
    if (month <= 9):
        monthstring = "0"+str(month)
    else:
        monthstring = str(month)
    for day in range(1, 32):
        if (day <= 9):
            daystring = "0"+str(day)
        else:
            daystring = str(day)

    datestring = monthstring + daystring
    fullurl = webURLprefix + datestring + webURLsuffix

    try:
        infile = opener.open(fullurl, timeout=15)
        outfile = open(outfilename, "w", encoding='utf-8')
        newpage = infile.read().decode('utf-8')
    except:
            newpage = ""
            print("We have an error")
    if newpage.find(targetstr) >- 1:
        print(datestring, file=outfile)

print("Done")
