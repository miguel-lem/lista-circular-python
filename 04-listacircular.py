class Nodo:
    def __init__(self,dato):
        #creo la variable para el dato
        self.dato=dato;
        #creo una elemento de tipo nodo que se apunte a si mismo
        self.siguiente = self;

#creo la clase con la cual voy a realizar las funciones
class Listacircular:
    def __init__(self):
        #creo la variable de tipo clase que servira de referencia para los demas datos
        self.cola = None;

    #funcions para insertar datos
    def insertardatos(self,dato):
        #creamos el nodo
        nodo = Nodo(dato);
        #si esta vacia la lista le colocarmos en la cabeza y como we apunta por defecto a si misma no hay problema
        if(self.cola==None):
            self.cola=nodo;
        else:
            #de lo contrario si las cosas cambian, le decimos al nuevo en su sugiente que apunte al siguiente debeza
            nodo.siguiente = self.cola.siguiente;
            # y en la cabeza siguente que apunte al nuvo nodo
            self.cola.siguiente = nodo;

    #funcion para ocmprobar si existe un numero dentro de lal ista
    def existenumero(self,numero):
        if(self.cola == None):
            return 0;
        else:
            #cargamos los datos en una nueva lista
            self.auxiliar = self.cola.siguiente;
            #esta variable de aqui es porque no hay dowhile en python y le quiero simular
            paso=int(0);
            #porque si o si quiero que al menos se ejecute una vez
            while(paso!=1):
                if(self.auxiliar.dato==numero):
                    return 1;
                self.auxiliar = self.auxiliar.siguiente;
                #este if permite terminar la condicion del do while simulado
                if(self.auxiliar==self.cola.siguiente):
                    paso=1;
            return 0;


    #funcion para saber quien es el siguiente
    def cualessiguiente(self,dato):
        if(self.cola == None):
            print("la lista esta vacia");
        else:
            if(self.existenumero(dato)==1):
                #cargamos los datos en una nueva lista
                self.auxiliar = self.cola.siguiente;
                paso=int(0);
                while(paso!=1):
                    if(self.auxiliar.dato==dato):
                        print("la cola de la lista es: [",self.cola.dato,"]");
                        print("El siguiente de [",self.auxiliar.dato,"] es"" [",self.auxiliar.siguiente.dato,"]");
                        return;
                    self.auxiliar = self.auxiliar.siguiente;
                    if(self.auxiliar==self.cola.siguiente):
                        paso=1;
            print("no existe el numero que quieres buscar");
    
    #funcion para editar la lista
    def editar(self,numero,dato):
        nodo = Nodo(dato);
        if(self.cola == None):
            print("la lista esta vacia");
        else:
            if(self.existenumero(numero)==1):
                #cargamos los datos en una nueva lista
                self.auxiliar = self.cola.siguiente;
                paso=int(0);
                while(paso!=1):
                    #busco el numero dentro de la lista hasta cuando se parecen
                    if(self.auxiliar.dato==numero):
                        #reemplazo el dato
                        self.auxiliar.dato=nodo.dato;
                        return;
                    self.auxiliar = self.auxiliar.siguiente;
                    if(self.auxiliar==self.cola.siguiente):
                        paso=1;
            print("no existe el numero que quieres reemplazar");

    #funcion para medir el tamanio de la lista
    def tamanio(self):
        #esta variable es para ir acumulando segun gira el while
        contador=int(0);
        if(self.cola == None):
            return 0;
        else:
            self.auxiliar = self.cola.siguiente;
            paso=int(0);
            while(paso!=1):
                contador=contador+1;
                self.auxiliar = self.auxiliar.siguiente;
                if(self.auxiliar==self.cola.siguiente):
                    return contador;


    #funcion para aliminar elimentos e la lista
    def eliminar(self,numero):
        if(self.tamanio() == 0):
            print("la lista esta vacia");
        else:
            if(self.existenumero(numero)==1):
                #cargamos los datos en una nueva lista
                self.auxiliar = self.cola.siguiente;
                self.auxiliar2 = self.cola;
                contador=int(0);
                tamanio=self.tamanio();
                paso=int(0);
                while(paso!=1):
                    #el contador empieza a correr porque sera necesrio en caso de que se quiera eliminar la cola
                    contador=contador+1;
                    #busco el numero dentro de la lista hasta cuando se parecen
                    if(self.auxiliar.dato==numero):
                        #si lo encuentro, al que viene una posicion por detras le hago apuntar al siguiente del que viene adelante
                        self.auxiliar2.siguiente = self.auxiliar.siguiente;
                        #luego le coloco estos datos en el auxiliar para que se borre asi el otro lado
                        self.auxiliar=self.auxiliar2;
                        #si termina el trabajo ya que se salga
                        return;
                    if(contador==(tamanio-1)):
                        print("No te permito eliminar la cola porque es la referencia de todo")
                        return;
                    #le hago recorrer las posiciones una por detras
                    self.auxiliar2=self.auxiliar2.siguiente
                    #este siempre correra una posicion por delante
                    self.auxiliar = self.auxiliar.siguiente;
                    if(self.auxiliar==self.cola.siguiente):
                        paso=1;
            print("no existe el numero que quieres eliminar");

    #funcion para leer los datos almacenados
    def leerdatos(self):
        if(self.cola == None):
            print("la lista esta vacia");

        else:
            self.auxiliar = self.cola.siguiente;
            paso=int(0);
            while(paso!=1):
                print("[",self.auxiliar.dato,"] -->",end="");
                self.auxiliar = self.auxiliar.siguiente;
                if(self.auxiliar==self.cola.siguiente):
                    paso=1;



listacircular = Listacircular();
paso = True;
while(paso):
    print("");
    print("----------Opciones----------");
    print("1 para insertar datos en la lista");
    print("2 para conocer cua es el siguiente de un numero");
    print("3 para editar un numero");
    print("4 para eliminar un dato de la lista"),
    opcion = int(input("0 para salir del programa: "))
    if(opcion == 1):
        dato=int(input("1.1 ingrese el dato a la lista:"));
        listacircular.insertardatos(dato);
        print("");
        listacircular.leerdatos();
        print("");
    elif(opcion==0):
        paso = False;
    elif(opcion==2):
        dato=int(input("2.1 ingrese el dato de la lista que quiere revisar:"));
        listacircular.cualessiguiente(dato);
        print("");
    elif(opcion==3):
        numero=int(input("3.1 ingrese el dato de la lista que quiere cambiar:"));
        dato=int(input("3.2 ingrese el dato nuevo que ingresara en la lista"));
        listacircular.editar(numero,dato);
        listacircular.leerdatos();
        print("");
    elif(opcion==4):
        dato=int(input("4.1 ingrese el dato a eliminar en la lista"));
        listacircular.eliminar(dato);
        listacircular.leerdatos();
        print("");
    print("tamaño de la lista: ",listacircular.tamanio());
