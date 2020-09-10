#Problema 7 Población

#Funcion principal
def main():
    
    print("Año donde en el cual la población del país B supera el de A: "+str(calcularaño()))

#Fucnion calcular año
def calcularaño():
    año=2019
    A=35000000 
    aumentoA=0.2
    B=19900000 
    aumentoB=0.3
    paso = 1
    while (A>B):
       paso += 1
       A=A*(10+aumentoA)
       B=B*(10+aumentoB)
       año=año+1
    return año

main()