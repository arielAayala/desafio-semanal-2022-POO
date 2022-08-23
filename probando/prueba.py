import requests
import cv2
from fractions import Fraction


url = "https://fondosmil.com/fondo/29363.jpg"
def calcularRatio(url):
    img_data = requests.get(url).content
    with open('image.jpg', 'wb') as archivo:
        archivo.write(img_data)

    img = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)
    
    height = img.shape[0]
    width = img.shape[1]

    ratio = str(Fraction(width,height))
    if "/" in ratio:
        ratio = ratio.replace("/", ":")
    else:
        ratio += ":1"
    print(ratio)
calcularRatio(url)