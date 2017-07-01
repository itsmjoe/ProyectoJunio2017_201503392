from NodoListaDoble import NodoListaDoble
from graphviz import Digraph
import commands
g = Digraph('g', filename='ListaDoble', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})
class ListaDoble():
	"""docstring for ListaDobleEnlazada"""    
    	def __init__(self):
                self.primero=None
                self.ultimo=None

        def Vacio(self):
            if self.primero==None:
                return True
            else:
                return False
           
        def DameUsuario(self,nombre):
            temp=self.primero
            recorrer=True
            while(recorrer):
                if temp.NombreOponente==nombre:
                    return temp
                else:
                    if temp==self.ultimo:
                        recorrer=False
                    else:
                        temp=temp.siguiente

        def MostrarPrimero(self):
            print(self.primero.NombreOponente)

        def InsertarPrimero(self,NombreUsuario,NombreOponente,TirosL,TirosA,TirosF,estadojuego,danio):
            nuevo = NodoListaDoble(NombreUsuario,NombreOponente,TirosL,TirosA,TirosF,estadojuego,danio)        
            if self.Vacio()==True:
                self.primero=self.ultimo=nuevo                
            else:
                nuevo.siguiente=self.primero
                self.primero.anterior=nuevo
                self.primero=nuevo
            

        def InsertarUltimo(self,elemento,pasw):
            nuevo= NodoListaDoble(elemento)
            if self.Vacio():
                self.primero=self.ultimo=nuevo
            else:
                self.ultimo.siguiente=nuevo
                nuevo.anterior=self.ultimo
                self.ultimo=nuevo
        def EliminarPrimero(self):
            if self.Vacio()==True:
                print("La lista se encuentra vacia, no se pueden eliminar elementos.")
            elif self.primero==self.ultimo:
                self.primero=None
                self.ultimo=None
                print("Elemento eliminado, la lista se encuentra vacia.")
            else:
                temp=self.primero
                self.primero=self.primero.siguiente
                self.primero.anterior=None
                temp=None
                print("Elemento eliminado.")
        def EliminarUltimo(self):
            if self.Vacio()==True:
                print("La lista se encuentra vacia, no se pueden eliminar elementos.")
            elif self.primero==self.ultimo:
                self.primero=None
                self.ultimo=None
                print("Elemento eliminado, la lista se encuentra vacia.")
            else:
                temp=self.ultimo
                self.ultimo=self.ultimo.anterior
                self.ultimo.siguiente=None
                temp=None
                print("Elemento eliminado.")

        def MostrarPrimeroUltimo(self):
            if self.Vacio()==True:
                print("Lista vacia.")
            else:
                texto=""
                recorrer=True
                temp=self.primero
                #print("----------------> Ultimo a primero")
                while (recorrer):
                    #print(temp.DameValor())                    
                    if self.primero==self.ultimo:
                        print(temp.NombreOponente)
                        recorrer=False
                    elif temp==self.ultimo:
                        #print(temp.siguiente.DameValor())
                        texto=texto+" -> " + temp.NombreOponente
                        #texto=texto+" -> " + temp.siguiente.DameValor()   
                        recorrer=False
                    else:
                        if temp==self.primero:
                            texto=temp.NombreOponente
                        else:
                            texto=texto+" -> " + temp.NombreOponente
                        temp=temp.siguiente
                print(texto)

        def Enlazar(self):
            if self.primero!=None:
                self.ultimo.siguiente=self.primero
                self.primero.anterior=self.ultimo
        

        def MostrarUltimoPrimero(self):
            if self.Vacio()==True:
                print("Lista vacia.")
            else:
                recorrer=True
                texto=""
                temp= self.ultimo
                #print("----------------> Primero a ultimo")
                while (recorrer):
                    #print(temp.DameValor())
                    if self.primero==self.ultimo:
                        print(temp.NombreOponente)
                        recorrer=False
                    elif temp==self.primero:
                        #print(temp.anterior.DameValor())
                        texto=texto+" -> "+temp.NombreOponente
                        #texto=texto+" -> "+temp.anterior.DameValor()
                        recorrer=False
                    else:
                        if temp==self.ultimo:
                            texto=temp.NombreOponente
                        else:
                            texto=texto +" -> "+temp.NombreOponente
                        temp=temp.anterior
                print(texto)

        def Graficar(self):
            temporal = self.primero
            while temporal != None:
                if temporal.siguiente != None:
                   g.edge((temporal.NombreOponente), temporal.siguiente.NombreOponente)
                   g.edge(temporal.siguiente.NombreOponente,temporal.NombreOponente)
                temporal = temporal.siguiente

            g.view()
