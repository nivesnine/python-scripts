#!/usr/bin/python
import urllib
import re
import sys

page = "http://" + str(sys.argv[1])

webPage = urllib.urlopen(page).read()

def strip_links(page, links):
    linkStart = page.find("<a ")
    if linkStart == -1:
        return links
    linkStop = page.find('>',linkStart)
    links.append(page[linkStart+3:linkStop])
    page = page[linkStop:]
    return strip_links(page, links)

foundLinks = strip_links(webPage, links=[])

for link in foundLinks:
    match = re.search(r'href=[\'"]?([^\'" >]+)', link)
    if match:
	    print(match.group(0)[6:])