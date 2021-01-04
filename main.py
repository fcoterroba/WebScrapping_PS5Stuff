from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime

now = datetime.now()

def MediaMarkt():

    print (f"Precios MediaMarkt -- {now.date()} {now.time()}")
    mando = 'https://www.mediamarkt.es/es/product/_mando-sony-ps5-dualsense%E2%84%A2-wireless-controller-blanco-1487502.html'
    mandoOnURL = urllib.request.urlopen(mando)
    mandoSoup = BeautifulSoup(mandoOnURL, 'html.parser')
    for i in mandoSoup.find('div', {'class':'big'}):
        print(f"El mando cuesta {i}€")
    juego = 'https://www.mediamarkt.es/es/product/_ps5-marvel-s-spider-man-miles-morales-1487492.html'
    juegoOnURL = urllib.request.urlopen(juego)
    juegoSoup = BeautifulSoup(juegoOnURL, 'html.parser')
    for j in juegoSoup.find('div', {'class':'big'}):
        print(f"El juego cuesta {j}€")

if __name__ == '__main__':
    MediaMarkt()
