
import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
thebytes = response.read()
text = thebytes.decode(encoding="iso-8859-1")    
lista = []
import bs4
doc = bs4.BeautifulSoup(text, features="html.parser")
tabelle = doc.find_all("table")
tabella = tabelle[3]
for tr in tabella.contents[2:-2]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        sequenza = int(tds[0].get_text())
        sigla = tds[7].get_text()
        provincia = tds[1].get_text()
        residenti = int(tds[2].get_text().replace(".", ""))
        superfice = int(tds[4].get_text().replace(".", ""))
        densita = float(tds[5].get_text().replace(".", "").replace(",", "."))
        densita = round(densita, 2)
        densita2 = residenti / superfice
        densita2 = round(densita2, 2)
    
        if densita != densita2:
            differenza = densita - densita2 
        else:
            differenza = 0 
        differenza = round(differenza, 2)       
        lista.append([sequenza, sigla, provincia, residenti, superfice, densita, densita2, differenza])
import pandas as pd
df = pd.DataFrame(lista, columns=['Sequenza', 'Sigla', 'Provincia', 'Residenti', 'Superficie', 'Densità', 'Densità2', 'Differenza'])
df.to_csv("province.csv", index=False)