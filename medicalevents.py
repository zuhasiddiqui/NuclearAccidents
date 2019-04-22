import urllib.request
import http.cookiejar

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

webURLprefix = "https://www.nrc.gov/reading-rm/doc-collections/event-status/event/"
webURLsuffix = "en.html"
outfilename = "medicalevents.csv"

targetstring = "35.3045(a)"

for year in range(2017, 2018):
    yearstring = str(year)
    for month in range(1, 13):
        if (month < 10):
            monthstring = "0"+str(month)
        else:
            monthstring = str(month)
        for day in range(1, 32):
            medicalcount = 0
            if (day < 10):
                daystring = "0"+str(day)
            else:
                daystring = str(day)
            fullurl = webURLprefix + str(year) + "/" + str(year) + str(month) + str(day) + webURLsuffix

            try:
                infile = opener.open(fullurl, timeout=15)
                outfile = open(outfilename, "w", encoding='utf-8')
                newpage = infile.read().decode('utf-8')
            # except:
                # newpage = ""
                # print("We have an error")

            for line in newpage:
                medicalcount = medicalcount + 1
                if line.find("35.3045(a)")>-1:
                    medicalcount = medicalcount + 1
                    print("year" + "," + "monthstring" + "," + medicalcount, file=outfile)

print("Done")
infile.close()
outfile.close()
