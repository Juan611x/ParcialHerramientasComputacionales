# ParcialHerramientasComputacionales

## 1. ¿Qué problema es ?

es un problema que requiere de la creación de un software por medio de la escritura de código para resolver, facilitar y optimizar el funcionamiento del problema planteado en el enunciado, esto gracias a el uso de estructuras matemáticas para simular el comportamiento de la venta de productos en una tienda 

## 2. ¿Qué modelo computacional lo resuelve?

este problema es resuelto gracias a un modelo computacional matemático que realiza el calculo, que simula el comportamiento de la venta en una tienda como se puede aprecial en la linea de codigo.
```python
s = "Python syntax highlighting"

   precio = precio + ((producto[compra[0]][1]-producto[compra[0]][1]*(50/100))*int(compra[1])) 
   lista.append(producto[compra[0]][0])
   
   precio = precio + ((producto[compra[0]][1]-producto[compra[0]][1]*(20/100))*int(compra[1]))
   lista.append(producto[compra[0]][0])

```


## 3. ¿Qué recibe el algoritmo de entrada? y ¿Cuál sería su salida? 
_Entrada:_
```python
s = "Python syntax highlighting"

cedula = str(input("Digite su cédula: "))
rol = str(input("¿Es estudiante o maestro? "))   
##En esta parte lo que entra es el dato de la cédula y posteriormente el rol del usuario

        
compra = str(input()).split()
## en esta parte se pide el dato del nombre del producto que se va a comprar y la cantidad de este

SioNo = str(input("¿Desea comprar algo más? "))
##En esta parte se pide el dato que decide si el usuario desea comprar otro producto o desea finalizar la compra
```
_Salida:_
```python
s = "Python syntax highlighting"

   print("El ",rol, "con cedula ", cedula,", ", "Debe pagar ",precio,"por el producto ", end = ' ')

    for x in lista:

        print(x, end=' ')

    print(" ")
    ## esta parte del código lo que hace es arrojar como dato final un texto que integra el rol del usuario, su cédula, cuanto debe pagar y una 
    ##lista con los códigos de los productos seleccionados

```

## 4. ¿Cómo lo calcula?
```python
s = "Python syntax highlighting"

   producto = {
    "JugoHit" : ["210",2500],
     "Cafe"    : ["200",1500],
     "Gaseosa" : ["129", 3000],
     "Te"      : ["180",1800],
     "Perro"   : ["300",3000],
     "Hambueguersa" : ["320",5000],
     "Pizza"   : ["330",4000]
}
##Se define el deccionario "producto" que es donde se almacenan los productos disponibles y su respectivo código y precio

def tienda():

    cedula = str(input("Digite su cédula: "))
    rol = str(input("¿Es estudiante o maestro? "))
    ## Aquí pedimos por teclado los datos de cédula y rol que son parte de la entrada del problema

    print("¿que producto desea comprar? y ¿Que cantidad?, digite el nombre y la cantidad")
    print("los productos disponibles son: ")
    
    
    for i in producto: 

        print(i, "" , producto[i][1] )
    ##Este for sirve para imprimir los nombres de todos los productos seguidos de sus precios
    
    
    op = True

    precio = 0

    lista = []
    ##Definimos las varialbes: "op" que es una variable booleana que almacena True
    ##precio que es un contador que almacena el valor final a pagar 
    ##con el valor 0 al inicio, y por último "lista" que es donde guardaremos los codigos de los productos que compro para ser impresos al final.

    while op == True:
    ##El while lo usamos para que el ciente pueda registrar tantos productos como quiera, hasta que op sea False, en dicho caso se calcelara el ciclo
        compra = str(input()).split()
        ##Recibe el nombre del producto y la cantidad, estos datos se almacenan en una lista
        
        
        if compra[0] in producto:

            if rol == "estudiante" or rol == "Estudiante":

                precio = precio + ((producto[compra[0]][1]-producto[compra[0]][1]*(50/100))*int(compra[1])) 
                lista.append(producto[compra[0]][0])
            else:

                precio = precio + ((producto[compra[0]][1]-producto[compra[0]][1]*(20/100))*int(compra[1]))
                lista.append(producto[compra[0]][0])

        
        else:

            print("No se encuentra el producto")

        ## esta cadena de if's lo primero que hace es comprobar si el producto que el cliente desea comprar está en el diccionrio "producto", si no se encuentra 
        ##realiza un print con el mensaje "No se encuentra el producto", de lo contrario si está, revisa que rol fue digitado anteriormente y dependiendo de eso 
        ##realiza el calculo respectivo al precio del producto con su respectivo descuento, agregando el código del producto a "lista" para luego ser impreso
        
        SioNo = str(input("¿Desea comprar algo más? "))
        ##imprime le pregunta "¿Desea comprar algo más? " y guarda su respuesta
        if SioNo == "Si" or SioNo == "si":

            op = True
        
        else:

            op = False
        ##Si la respuesta guardada en "SioNo" es si, "op" es True ,de lo contrario si es no, entonces "op" es False y el ciclo while se rompera dejando de 
        ##registrar más productos
    print("El ",rol, "con cedula ", cedula,", ", "Debe pagar ",precio,"por el producto ", end = ' ')

    for x in lista:

        print(x, end=' ')

    print(" ")
    ##Para finalizar, se imprime el mensaje respectivo con los valores de las variables "rol", "cédula", y "precio" seguido de los 
    ##códigos de los productos registrados
```


## Contenido del repositorio
El repositorio solo contiene 3 archivos, uno es el archivo "README", donde procedemos a la explicación del código, el siguiente es un archivo ".txt", donde explicamos los errores que tuvimos y los posibles errores que podrían generarse junto con su posible corrección. Finalmente, el último archivo es el código de python que da solución al problema del enunciado.
