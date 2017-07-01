from graphviz import Digraph
from NodoArbolBinario import NodoArbolBinario
g = Digraph('g', filename='ArbolUsuariosESpejo', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})
class ArbolBinario:
	"""docstring for ArbolBinario"""
	def __init__(self):
		self.raiz=None

	def ArbolVacio(self):
		if self.raiz==None:
			return True
		else:
			return False

	def Insertar(self,elemento,passw,estado):
		nuevo= NodoArbolBinario(elemento,passw,estado)
		contador=0
		if self.raiz==None:
			self.raiz=nuevo
		else:
			aux=self.raiz
			padre=None
			while  aux!=None:
				padre=aux
				if str(nuevo.dato)>=str(aux.dato):
					contador+=1
					aux=aux.hijoderecho
				else:
					contador+=1
					aux=aux.hijoizquierdo
			if str(nuevo.dato)>=str(padre.dato):
				padre.hijoderecho=nuevo
				#print padre.dato+'->'+elemento
				g.node(padre.dato,str(padre.dato)+ " "+str(padre.passw) +" "+str(padre.estado))
				g.node(padre.hijoderecho.dato,str(padre.hijoderecho.dato)+ " "+str(padre.hijoderecho.passw) +" "+str(padre.hijoderecho.estado))
				g.edge(padre.dato,padre.hijoderecho.dato)
				#g.edge(padre.hijoderecho.dato,padre.dato)
			else:
				padre.hijoizquierdo=nuevo
				#print padre.dato+'->'+elemento
				g.node(padre.dato,str(padre.dato)+ " "+str(padre.passw) +" "+str(padre.estado))
				g.node(padre.hijoizquierdo.dato,str(padre.hijoizquierdo.dato)+ " "+str(padre.hijoizquierdo.passw) +" "+str(padre.hijoizquierdo.estado))
				g.edge(padre.dato,padre.hijoizquierdo.dato)

	def MostrarPreorden(self,elemento):
		#print("Elementos en preorden")
		if  elemento!=None:
			print(elemento.dato)	
			self.MostrarPreorden(elemento.hijoizquierdo)
			self.MostrarPreorden(elemento.hijoderecho)

	def MostrarPostorden(self,elemento):
		#print("Elementos en postorden")
		if elemento!=None:
			self.MostrarPostorden(elemento.hijoizquierdo)
			self.MostrarPostorden(elemento.hijoderecho)
			print(elemento.dato)

	def MostrarInorden(self,elemento):
		#print("Elementos en inroden")
		if elemento!=None:
			self.MostrarInorden(elemento.hijoizquierdo)
			print(elemento.dato)
			self.MostrarInorden(elemento.hijoderecho)

	def DameRaiz(self):
		return self.raiz

	def BuscarNodo(self,elemento):
		aux=self.raiz
		if self.ArbolVacio()!=True:
			while aux.dato!=elemento:
				#print(aux.dato +" | buscar |"+ elemento)
				if (elemento<=aux.dato):
					aux=aux.hijoizquierdo
				else:
					aux=aux.hijoderecho
				if aux==None:
					return None
		return aux

	def CrearReporte2(self):
		pass


	def CrearReporte(self):
		g.view()
		return "True"

	def Eliminar(self, NodoArbolBinario):
		aux=self.raiz
		padre=self.raiz
		existehiz=True
		while aux.dato!=NodoArbolBinario.dato:
			padre=aux
			if NodoArbolBinario.dato<aux.dato:
				existehiz=True
				aux=aux.hijoizquierdo
			else:
				existehiz=False
				aux=aux.hijoderecho
			if aux==None:
				return False

		if aux.hijoizquierdo==None and aux.hijoderecho==None:
			if aux==self.raiz:
				self.raiz=None
			elif existehiz:
				padre.hijoizquierdo=None
			else:
				padre.hijoderecho=None
		elif aux.hijoderecho==None:
			if aux==self.raiz:
				self.raiz=aux.hijoizquierdo
			elif existehiz:
				padre.hijoizquierdo=aux.hijoizquierdo
			else:
				padre.hijoderecho=aux.hijoizquierdo
		elif aux.hijoizquierdo==None:
			if aux==self.raiz:
				self.raiz=aux.hijoderecho
			elif existehiz:
				padre.hijoizquierdo=aux.hijoderecho
			else:
				padre.hijoderecho=aux.hijoizquierdo
		else:
			reemplazo=self.ObteneReemplazo(aux)
			if aux==self.raiz:
				self.raiz=reemplazo
			elif existehiz:
				padre.hijoizquierdo=reemplazo
			else:
				padre.hijoderecho=reemplazo
			reemplazo.hijoizquierdo=aux.hijoizquierdo

	def Modificar(self,elemento,contra,usuario,estado):
		if elemento!=None:			
		        elemento.dato=usuario
		        elemento.passw=contra
		        elemento.estado=estado

	def ObteneReemplazo(self,elemento):
		reemplazoPadre=elemento
		reemplazo=elemento
		auxi=elemento.hijoderecho

		while auxi!=None:
			reemplazoPadre=reemplazo
			reemplazo=auxi
			auxi=auxi.hijoizquierdo

		if reemplazo!=elemento.hijoderecho:
			reemplazoPadre.hijoizquierdo=reemplazo.hijoderecho
			reemplazo.hijoderecho=elemento.hijoderecho

		print("El nodo reemplazado es "+ str(reemplazo.dato))
		return reemplazo