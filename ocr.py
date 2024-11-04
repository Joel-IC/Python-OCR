import cv2
import easyocr
from matplotlib import pyplot as plt
import numpy as np

ruta_imagen = "placa.jpg"

lector = easyocr.Reader(["es"])

resultados = lector.readtext(ruta_imagen)

fuente = cv2.FONT_HERSHEY_SIMPLEX

imagen = cv2.imread(ruta_imagen)


for resultado in resultados:
    arr_izq = tuple(resultado[0][0]) 
    abj_der = tuple(resultado[0][2])
    texto = resultado[1]
    print (texto)
    cv2.rectangle(imagen,arr_izq,abj_der,(0,225,0),1)
    cv2.putText(imagen,texto,arr_izq,fuente,0.40,(0,255,0),1,cv2.LINE_AA)

plt.imshow(imagen)
plt.show()


