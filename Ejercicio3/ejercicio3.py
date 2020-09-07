#Problema 4 Decuento del producto

# Funcion principal
def main():

    print("Bienvenido")
    precioP=float(input("Ingrese el precio del producto:"))

    if precioP>0:
        diaS=str(input("Ingrese el día de la Semana. Recuerde que:Lunes:l, Martes:m, Miércoles: M, Jueves: j, Viernes: v, Sábado: s, Domingo: d \nDia: "))
       
        if diaS=="l" or diaS=="m" or diaS=="M" or diaS=="j" or diaS=="v" or diaS=="s" or diaS=="d":
            valorD= float(calcularDescuento(precioP,diaS))
            valorT= precioP - valorD
            print("El valor de descuento es de: "+ str(valorD)+ " por lo que eñ valor total es: " + str(valorT))
        else:
            print("Lo sentimos, el día que ingreso no es admitido")
            print("Intente de nuevo desde el comienzo")
            main()

    else:
        print("Lo sentimos, el precio del producto debe ser mayor a cero")
        print("Intente de nuevo")
        main()

# Calculo Descuento
def calcularDescuento(precioP,diaS):
    if diaS == "l":
        return precioP*0.1
    elif diaS == "m":
        return precioP*0.05 
    elif diaS == "M":
        return precioP*0.03 
    elif diaS == "j" or diaS=="d":
        return precioP*0.01 
    elif diaS == "v":
        return precioP*0.07 
    else:
        return 0




main()