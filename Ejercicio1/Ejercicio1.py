# -*- coding: latin-1 -*-
abecedario = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")
def cifradoCesar(mensaje,clave):
    result = ""
    mensajeMinus = mensaje.lower()
    for caracter in mensajeMinus:
        if caracter not in abecedario:
            result += caracter
        else:
            posicion = abecedario.index(caracter)
            result += abecedario[(posicion+clave)%len(abecedario)]

    return result