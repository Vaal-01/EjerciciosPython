#Problema 3: El primer y último carácter.

#Funcion Principal
def main():
   
        palabra=str(input("Escriba alguna palabra: "))
        print(caracteres(palabra))
        print("Hasta Luego!")


#Revision primer y ultimo caracter 
def caracteres(palabra):
    primero = palabra[0]
    ultimo = palabra[len(palabra)-1]
    return ("El primer caracter es: " + primero + " y el último es: " + ultimo)


main()
