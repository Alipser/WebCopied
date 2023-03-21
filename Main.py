import Crawler
import CreatedT


from bs4 import BeautifulSoup as bs
from bs4.formatter import HTMLFormatter

import requests

#Recolección del Body

 

with open("./index.html", "r", encoding="utf-8") as file:
    html = file.read()
    soup = bs(html, "html.parser")
    cuerpo = soup.find("body")
    CreatedT.translate(cuerpo, "hi")
    
        
   

# Guardar los cambios en el archivo HTML
