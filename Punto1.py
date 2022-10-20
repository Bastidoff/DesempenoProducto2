
def crearCiclista(nombre,edad,pais,equipo,tiempo):
    ciclista={
        'nombre':nombre,
        'edad':edad,
        'pais':pais,
        'equipo':equipo,
        'tiempo':tiempo
    }

    return ciclista


def calcularMenorTiempo(listaCiclistas):
    ciclistasOrdenados = sorted(listaCiclistas, key=lambda ciclista: ciclista['tiempo'])

    return ciclistasOrdenados[0]


listaCiclistas=[]
eleccionUsusario=1
while eleccionUsusario != 0: 
    
    print ("0 para salir: ")
    print ("1 agregar cilcista: ")
    print ("2 ver resultados: 1")
    eleccionUsusario = int(input("dijita una opcion"))
    if eleccionUsusario ==1:
        nombre=input("ingrese el nombre del ciclista: ")   
        edad=int(input("edad del cilcista: "))
        pais=input("pais del ciclista: ")
        equipo=input("equipo del ciclista: ")
        tiempo=float(input("tiempo del ciclista: "))
        cilcista=crearCiclista(nombre,edad,pais,equipo,tiempo)
        listaCiclistas.append(cilcista)
    elif eleccionUsusario ==2:
        
        if listaCiclistas ==[]:
            print("lista vacia ingrese datos de cilcistas")
        else:
            cilcistaGanador=calcularMenorTiempo(listaCiclistas)


            print(f'el Ciclista con menor tiempo es: {cilcistaGanador}')

    elif eleccionUsusario ==0:
        break

    else:
        print('dijite un numero correcto')    





