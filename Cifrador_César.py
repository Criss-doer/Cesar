from typing import *

ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '
LONGITUD_ALFABETO = len(ALFABETO)


def cifrar(mensaje:str,d = dist)->str:
    pasos = 0
    punto_inicio = 0
    mensaje_cifrado=''
    for letra in mensaje.upper():
        if letra in ALFABETO:

            punto_inicio = ALFABETO.find(letra)
            pasos = punto_inicio + d
            # print(pasos)
            # while pasos > LONGITUD_ALFABETO:
            # pasos -= LONGITUD_ALFABETO
             pasos = pasos % LONGITUD_ALFABETO
        mensaje_cifrado += ALFABETO[pasos]
    return mensaje_cifrado

def creaCifrador(dist:int)->Callable:
    def cifrador(mensaje:str) -> str:
        return cifrar(mensaje, dist)
    return cifrador
    

def creaParCesar(dist:int)->Tuple[Callable,Callable]:
    def cifrador(mesanje: str) -> str:
        return cifrar(mensaje, dist)
    
    def descifrador(mensaje:str) -> str:
        return cifrar(mensaje, -dist)
    
    return cifrador, descifrador

assert cifrar("zig", 3) == "BLJ"
assert cifrar("blj", -3) == "ZIG"

cifrador2 = creaCifrador(2)
assert cifrador2("A Z") == "CBA"

cifra2, descifra2 = creaParCesar = creaParCesar(2)
assert cifra2("A Z") == "CBA"
assert descifra2("CBA") == "A Z"