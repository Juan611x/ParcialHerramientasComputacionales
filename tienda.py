producto = {
    "JugoHit" : ["210",2500],
     "Cafe"    : ["200",1500],
     "Gaseosa" : ["129", 3000],
     "Te"      : ["180",1800],
     "Perro"   : ["300",3000],
     "Hambueguersa" : ["320",5000],
     "Pizza"   : ["330",4000]
}

def tienda():

    cedula = str(input("Digite su cédula: "))
    rol = str(input("¿Es estudiante o maestro? "))

    print("¿que producto desea comprar? y ¿Que cantidad?, digite el nombre y la cantidad")
    print("los productos disponibles son: ")
    for i in producto: 

        print(i, "" , producto[i][1] )

    op = True

    precio = 0

    lista = []

    while op == True:

        compra = str(input()).split()

        if compra[0] in producto:

            if rol == "estudiante" or rol == "Estudiante":

                precio = precio + ((producto[compra[0]][1]-producto[compra[0]][1]*(50/100))*int(compra[1])) 
                lista.append(producto[compra[0]][0])
            else:

                precio = precio + ((producto[compra[0]][1]-producto[compra[0]][1]*(20/100))*int(compra[1]))
                lista.append(producto[compra[0]][0])

        
        else:

            print("No se encuentra el producto")


        SioNo = str(input("¿Desea comprar algo más? "))
        
        if SioNo == "Si" or SioNo == "si":

            op = True
        
        else:

            op = False
        

    print("El ",rol, "con cedula ", cedula,", ", "Debe pagar ",precio,"por el producto ", end = ' ')

    for x in lista:

        print(x, end=' ')

    print(" ")


tienda()
