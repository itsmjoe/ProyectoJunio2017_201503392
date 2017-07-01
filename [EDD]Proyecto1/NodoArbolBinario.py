class NodoArbolBinario:
	"""docstring for NodoArbolBinario"""
	def __init__(self,elemento,passw,estado):
		self.dato=elemento  
		self.passw=passw
		self.estado=estado
		self.ListaJuegos=None	
		self.hijoizquierdo=None
		self.hijoderecho=None
		self.MatrizDispersa=None

	def DameDato(self):
		return self.dato