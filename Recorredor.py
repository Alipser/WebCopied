import os
from bs4.formatter import HTMLFormatter
from bs4 import BeautifulSoup
import CreatedT




files_from_folder = r"C:\Users\Alipser\Desktop\Novia\Scrap\Prueba"
destination_language = 'hi'



  

def recorredor(path):
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith('.html'):
            htmlWalker(path, filename)
        elif (os.path.isdir(os.path.join(path, file))):
                new_Path = os.path.join(path, file)
                recorredor(new_Path)

class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v

def htmlWalker(files_from_folder, filename, destination_language="hi"):
    with open(os.path.join(files_from_folder, filename), encoding='utf-8') as html:
                soup = BeautifulSoup(html.read(), 'html.parser')
                hola=soup.find_all(True)
                whattags = []
                for everyTag in hola:
                        whattags.append(everyTag.name)
                        
                whattags = set(whattags)
                print(whattags)
                excludetags = {"html", "table",  "aside", "ul", "body", "footer", "header", "head", "style", "script",  "noscript", "img", }
                for everyTag in whattags.difference(excludetags):
                        for everyresult in soup.findAll(everyTag, text=True):  
                                try:
                                    print(everyresult.text)
                                    CreatedT.translate(everyresult,destination_language)
                                except: 
                                    pass
                
                for span in soup.find_all("span"):
                      CreatedT.translate(span,destination_language)
                      
            
                soup = soup.encode(formatter=UnsortedAttributes()).decode('utf-8')
                new_filename = f'{filename.split(".")[0]}.html'
                with open(os.path.join(files_from_folder, new_filename), 'w', encoding='utf-8') as html:
                        html.write(soup)
                        
                
                
                

recorredor(files_from_folder)



  
 
  