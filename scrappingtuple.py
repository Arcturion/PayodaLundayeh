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
im = Image.open(BytesIO(response.content))
print(im.size)
#im = foo.convert('RGB')

pix_val = list(im.getdata())  # get pixel value in RGB format

a = [x for sets in pix_val for x in sets] #Convert list of tuples into one list 

myRoundedList =  [round(x,-1) for x in a]  #Round integers to nearest 10

if im.mode in("RGBA","p"):

	b=[tuple(myRoundedList[i:i+4]) for i in range(0, len(myRoundedList), 4)]  #Group list to a tuple of 4 integers

elif im.mode in("RGB"):

	b=[tuple(myRoundedList[i:i+3]) for i in range(0, len(myRoundedList), 3)]   #Group list to a tuple of 3 integers
   
list_of_pixels = list(b)

im2 = Image.new(im.mode, im.size) #Create a new image 

im2.putdata(list_of_pixels) #put image data into the new image 

im2.save("D:\prajab\Aktualisasi\wik\es1.png","PNG")
#im2.save("D:\prajab\Aktualisasi\wik\es1.jpg","JPEG", optimize=True,quality=85)