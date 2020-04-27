from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
#import pandas as pd

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
counts=0
total=0
x=list()
for tag in tags:
    # Look at the parts of a tag
    #stuff=span.text
    #numlist.append(int(stuff))
    #print('TAG:',tag)
    #stuff=re.findall('[0-9]+',tag)
    counts=counts+1
    y=tag.contents[0]
    [x.append(t) for t in [int(num) for num in re.findall("[0-9]+",y)]]
    #z=int(x)
print("Count ",counts)
print("Sum ",sum(x))

#file={"values":x}
#files=pd.DataFrame(file)
    #for n in stuff:
        #numlist.append(int(n))
#print(x)
#print(numlist)
#print("count ",counts)
#print("Sum ",sum(numlist))
