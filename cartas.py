# -*- coding: cp1252 -*-
from random import *
def mazo():
    return sample([(x,y) for x in['A','J','Q','K']+range (2,11) for y in ['picas','trebol','diamantes','corazon']],52)

def jugar(mazo):
    #barajaInicial(mazo)
    #juegoJugador([mazo[0],mazo[1]], [mazo[2],mazo[3]], mazo[4:])
    juegoJugador([(2,'corazon'),(4,'diamantes')], [(3,'corazon'),(3,'diamantes')], mazo[4:])
    
   #el juego inicia con el jugador  
def juegoJugador(cartasJugador, cartasCasa, mazo):
    mostrarCartas(cartasJugador)
    print "Su puntaje es: "
    #Se calcula el puntaje del jugador
    print calcularMano(ordenarMano(cartasJugador),0)
    if(calcularMano(ordenarMano(cartasJugador),0)<=21):
        #Se solicita si desea seguir jugando, si no, juega la casa
        if(raw_input("¿Quiere carta?") == "y"):        
            juegoJugador(repartirCarta(cartasJugador, mazo), cartasCasa, mazo[1:])
        else:
            juegoCasa(cartasJugador,cartasCasa,mazo)
    else:
        print "PERDISTE"

#La casa juega automaticamente                
def juegoCasa(cartasJugador,cartasCasa,mazo):
    mostrarCartas(cartasCasa)
    print "El puntaje de la Casa es: "
    print calcularMano(ordenarMano(cartasCasa),0)

    if(calcularMano(ordenarMano(cartasCasa),0)==calcularMano(ordenarMano(cartasJugador),0)):
        print "EMPATE"
        if((empate(cartasJugador,0) == empate(cartasCasa,0)) or (empate(cartasJugador,0) < empate(cartasCasa,0))):
            print "GANA LA CASA"
        else:
            print "GANA EL JUGADOR"

    #Calcula si la casa tiene menor puntaje que el jugador    
    elif(calcularMano(ordenarMano(cartasCasa),0)<calcularMano(ordenarMano(cartasJugador),0)):
        juegoCasa(cartasJugador, repartirCarta(cartasCasa, mazo), mazo[1:])

    #si la casa sobrepasa los 21 puntos, gana el jugador       
    elif(calcularMano(ordenarMano(cartasCasa),0)>21):
       print "GANA EL JUGADOR"

    else:
        print "GANA LA CASA"

def empate(mano, cantidad):
        if (mano[0][1]=='diamantes' or mano[0][1]=='corazon'):
            if mano[1:] != []:
                return empate(mano[1:], cantidad + 1)
            else:
                return cantidad+1      
        
    

#Calcula el puntaje 
def calcularMano(mano, puntaje):
    if mano == []:
        return puntaje
    #si sale un A asigna 1 u 11 dependiendo del puntaje
    if mano[0][0] == 'A':
        if mano[1:] == [] and puntaje + 11 <= 21:
            return calcularMano(mano[1:], puntaje + 11)
        return calcularMano(mano[1:], puntaje + 1)
    if mano[0][0] == 'J' or mano[0][0] == 'Q' or mano[0][0] == 'K':
        return calcularMano(mano[1:], puntaje + 10)
    return calcularMano(mano[1:], puntaje + mano[0][0])

#Suma una nueva carta a la mano 
def repartirCarta(cartas, mazo):    
   return cartas+[mazo[0]]

#Muestra las cartas de la mano
def mostrarCartas(cartas):
    print cartas        
    
def barajaInicial(mazo):
    for x in range(0,51):    
        print mazo[x]

def ordenarMano(mano):
    return manoNum(mano)+manoInvert(manoAlfa(mano))


def manoNum(mano):
    if(mano!=[]):
        mano.sort()
        for x in mano:
            if(type(x[0]) is not int):
                return mano[:mano.index(x)]
            else:
                return mano
    else:
        return []
        
def manoAlfa(mano):
    if(mano!=[]):
        mano.sort()
        for x in mano:
            if(type(x[0]) is not int):
                return mano[mano.index(x):]
            else:
                return []
    else:
        return []
def manoInvert(mano):
    if(mano!=None):
        mano.sort(reverse=True)
    return mano

jugar(mazo())
