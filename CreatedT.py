
from googletrans import Translator


def translate(htmlNode, destination_language):
    translator = Translator()   
    for element in htmlNode.contents:
        if (isinstance(element, str)):
            try:
                
                element.replaceWith(translator.translate(element, dest=destination_language).text)
                print(element.replaceWith(translator.translate(element, dest=destination_language).text))
            except: 
                pass
        elif element != None:
            translate(element, destination_language)
                
        


                
        
       
