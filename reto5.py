#Crea un programa que se encargue de calcular el aspect ratio de una 
# imagen a partir de una url.
#Url de ejemplo: https://www.jhstoys.com/uploads/6/1/3/7/61377571/s737619424575262359_p1042_i943_w894.jpeg
# Por ratio hacemos referencia por ejemplo a los '16:9' de una imagen de 1920*1080px.

import requests
import cv2
from fractions import Fraction


url = "https://www.jhstoys.com/uploads/6/1/3/7/61377571/s737619424575262359_p1042_i943_w894.jpeg"
def calcularRatio(url):
    img_data = requests.get(url).content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)

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