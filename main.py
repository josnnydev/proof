import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get('https://parascrapear.com/')
soup = BeautifulSoup(url.text,"html.parser")
blockquote_items = soup.find_all('blockquote') 

autores = []
categorias = []
frases = []

for blockquote in blockquote_items:
    autor = blockquote.find(class_='author').text
    categoria = blockquote.find(class_='cat').text
    frase = blockquote.find('q').text
    autores.append(autor)
    categorias.append(categoria)
    frases.append(frase)

    #print(autor, categoria, frase)

mi_dict = {'autor':autores,'categoria':categorias,'frase':frases}
df_frases = pd.DataFrame(mi_dict)
df_frases.to_csv('frases.csv')


   