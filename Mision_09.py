# Autor: Luis Armando Miranda Alcocer
# Misión 9: Ejercicio con listas

def extraerPares(lista1):
    listaPares=[]
    for dato in lista1: #Recorre uno por uno
        if dato%2 == 0 : #Si es divisible entre 2, y el residuo da cero, es par
            listaPares.append(dato) # Agrega a todos los pares
    return listaPares



def extraerMayoresPrevio(lista1):
    listaMayoresPrevio = [] #Se crea una nueva lista
    for dato in range(len(lista1)):  # Recorre uno por uno
        if lista1[dato] > lista1[dato-1]: #Si el dato de la lista (subindice) es mayor que el anterior, se agrega a la lista nueva
            listaMayoresPrevio.append(lista1[dato])
        else:   #Sino, pasa
            pass
    return listaMayoresPrevio



def intercambiarParejas(lista1):
    listaIntercambio = []  # Se crea una nueva lista
    sumaLista= len(lista1)
    if sumaLista%2 == 0:
        for dato in range(0,len(lista1),2):
            listaIntercambio.append(lista1[dato])
            return listaIntercambio
    else:
        pass
    return listaIntercambio


def intercambiarMM(lista1):
    minimo= min(lista1)     #Define el valor mínimo y máximo
    maximo= max(lista1)
    for datoMin in range(len(lista1)): #Se busca el índice del valor mínimo
        if lista1[datoMin]==minimo:
            i=datoMin   #Se le asigna un valor al índice del valor mínimo, como "i"
            for datoMax in range(len(lista1)): #Se busca el índice del valor máximo
                if lista1[datoMax]==maximo:
                    j=datoMax   #Se le asigna un valor al índice del valor máximo, "j"
    lista1.remove(maximo) #QUita los valores mínimos y máximos
    lista1.remove(minimo)
    lista1.insert(i, maximo) #Los intercambia por los lugares que tenían
    lista1.insert(j, minimo)
    #print(maximo,minimo) Pruebas
    #print(lista1)
    return lista1


def promediarCentro(lista1):
    listaNueva=lista1.copy()
    minimo = min(lista1)  # Define el valor mínimo y máximo
    maximo = max(lista1)
    for datoMin in range(len(lista1)):  # Se busca el índice del valor mínimo
        if lista1[datoMin] == minimo:
            i = datoMin  # Se le asigna un valor al índice del valor mínimo, como "i"
            for datoMax in range(len(lista1)):  # Se busca el índice del valor máximo
                if lista1[datoMax] == maximo:
                    j = datoMax  # Se le asigna un valor al índice del valor máximo, "j"
    # print(lista1[i], lista1[j]) Prueba
    listaNueva.remove(listaNueva[i]) #Quita los valores máximos y mínimos
    listaNueva.remove(listaNueva[j])
    suma= sum(listaNueva) #Para calcular promedio, suma los números de la lista
    total=len(listaNueva) #Calcula el total de datos
    promedio=suma/total #Calcula el promedio
    return promedio #Regresa el promedio


def calcularEstadistica(lista2):
    listaNueva=[] #Se crea nueva lista
    suma=sum(lista2) #Se calcula la suma y el total de datos
    total=len(lista2)
    mean= suma/total #Se saca el promedio
    for dato in lista2:
        a=(dato-mean)**2 #Se calcula la suma de datos menos el promedio al cuadrado de toda la lista
        listaNueva.append(a)#para procesarlo, lo guardo en una lista
    sumaDos=sum(listaNueva) #Sumo cada valor de la lista
    deviation=(sumaDos/(total-1))**(1/2) #Realizo la raíz para calcular la desviación
    #print(deviation)
    tupla=mean,deviation    #Creo la tupla con los dos valores
    return tupla


def calcularSuma(lista1):
    listaSin13=lista1.copy()
    for dato in lista1:
        if lista1[dato]==13:
            listaSin13.remove(lista1[dato-1])
            listaSin13.remove(lista1[dato+1])

    suma= sum(listaSin13)
    return suma



def main():
    lista1=[5,4,1,2,3,4,3,2,60,13]

    Pares=extraerPares(lista1)
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista", lista1, ", regresa ", Pares)
    print(" ")

    mayoresPrevio = extraerMayoresPrevio(lista1)
    print("Problema 2. Regresa una lista con los valores que sean mayores aun valor previo de la lista original.")
    print("Con la lista", lista1, ", regresa ", mayoresPrevio)
    print(" ")

    intercambio = intercambiarParejas(lista1)
    print("Problema 3. Regresa una lista con los valores que sean mayores aun valor previo de la lista original.")
    print("Con la lista", lista1, ", regresa ", intercambio)
    print(" ")

  ##  intercambioMM = intercambiarMM(lista1)
    print("Problema 4. Regresa una lista con los valores con el valor mayor y menor intercambiados de la lista original.")
    print("Con la lista original, regresa ", intercambiarMM(lista1))
    print(" ")

    promedioCentro = promediarCentro(lista1)
    print("Problema 5. Regresa el promedio centro.")
    print("Con la lista", lista1, ", regresa ", "%.2f" %promedioCentro)
    print(" ")

    lista2=[1,2,3,4,5,6]
    estadistica = calcularEstadistica(lista2)
    print("Problema 6. Regresa el promedio centro.")
    print("Si recibe", lista2, ", regresa ", estadistica)
    print(" ")

    sin13 = calcularSuma(lista1)
    print("Problema 7. Regresa sin 13.")
    print("Con la lista", lista1, ", regresa ", sin13)
    print(" ")

main()