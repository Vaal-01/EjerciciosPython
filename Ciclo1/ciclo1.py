#Problema 6 Palabra palíndroma 

# Funcion principal
def main():

    print("Bienvenido")
    cadena=str(input("Ingrese la palabra que desea comprobar:"))

    salida = verificarpalabraPalindroma(cadena)
    if salida: 
        print(cadena + " es una cadena de caracteres palindroma :D")
    else:
        print(cadena + " no es una cadena de caracteres palindroma :P")


#Verificar palindromo
def verificarpalabraPalindroma(cadena):
    indice =0
    final = len(cadena) - 1
    cadena2=''
    palindroma = False

    while (len(cadena) > indice) : 
        cadena2+=cadena[final]
        indice+=1
        final-=1
    if cadena == cadena2 :
           
        palindroma = True
      
    return palindroma


main()
