#Problema 2: Conocer si un número es par o no 

#Funcion Principal

def main():
    try:
        numero = int(input("Escriba algún número: "))
    except ValueError:
        print ("Caracter inválido, ingrese un número entero")
        main()

    bandera = validacion(numero)
    if bandera: 
        print("El número ingresado es par :D")
    else:
        print("El número ingresado es impar :P")


#Revision par o impar
def validacion(numero):
    return(bool(numero % 2==0))

main()