import requests
import csv
from bs4 import BeautifulSoup as bs

url = 'https://www.classcentral.com/'
headers={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
    "cookie": "PHPSESSID=d53heq69mhua6p56pnk5n7guug"

}

onelevelDeepUrls=[]
response = requests.get(url, headers=headers)

htmlresponse = response.content

soup = bs(htmlresponse, "html.parser")

for a in soup.find_all(href=True):
     onelevelDeepUrls.append(a['href'])

with open("filename.csv", mode='w', newline='') as file:
     writer = csv.writer(file)
     for row in onelevelDeepUrls:
        writer.writerow([row])
     
   





