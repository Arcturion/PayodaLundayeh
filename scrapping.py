from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

site = urlopen("https://www.bmkg.go.id/satelit/satelit.bmkg?Sat=0&id=3").read()
#http://www.bom.gov.au/australia/charts/viewer/index.shtml?type=mslp-precip&tz=UTC&area=Ind&model=G&chartSubmit=Refresh+View
#http://www.bom.gov.au/australia/charts/viewer/index.shtml?type=mslp-precip&tz=UTC&area=Ind&model=G&chartSubmit=Refresh+View
soup = BeautifulSoup(site, 'html.parser')

images = []
images = soup.findAll('img')
link = "tes"

for image in images:
	target = image.get('src')
	target = str(target)
	if(target[8:16] == "inderaja"):
		link = target

print(link)

response = requests.get(link)
foo = Image.open(BytesIO(response.content)).resize((1000,1000))
print(foo.size)
bg = foo.convert('RGB')


bg.save("D:\prajab\Aktualisasi\wik\es1.jpg",optimize=True,quality=85)