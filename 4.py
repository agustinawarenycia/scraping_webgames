import requests
import lxml.html as html
import pandas as pd

def create_list():
    titles=[]
    total_titles=[]
    resultados = obtain_titles(0)
    titles.append(resultados[0])

    totales=int(resultados[1])
    actual=int(resultados[2])

    cant_de_bucles=totales/90

    for i in range(int(cant_de_bucles)):
        title_new=obtain_titles(int(actual))
        titles.append(title_new[0])
        actual=title_new[2]
    for title in titles:
        for i in title:
            total_titles.append(i)
    return total_titles


def obtain_titles(contador):
    
    
    url_padre='https://www.microsoft.com/es-ar/store/top-paid/games/pc?skipitems='+str(contador)
    print(f"URL: {url_padre}")
    juegos = "//li[@class='col mb-4 px-2']/div/@data-bi-prdname"
    cantidad_juegos_locator="//span[@id='status-msg-1'][1]/text()"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    

    #url_new=url_padre.replace('value', '0')
    r = requests.get(url_padre, headers=headers)
    # Decodificamos el contenido de la respuesta para obtener el HTML
    home=r.content.decode('utf-8')
    # Transformamos el texto plano de HTML en un documento de HTML
    parser=html.fromstring(home)


    # Titulos de los juegos
    titulos=parser.xpath(juegos)
    # Logica para obtener la cantidad de juegos
    cantidad=parser.xpath(cantidad_juegos_locator)
    split_cantidad=cantidad[0].split(' ')
    cantidad=split_cantidad[8]
    faltantes=split_cantidad[6]  

   
    return [titulos,cantidad,faltantes]

if __name__ == '__main__':
   si = create_list()
   #cantidad de elementos en la lista si
   print(f"Cantidad de juegos{len(si)}")
   print(si)