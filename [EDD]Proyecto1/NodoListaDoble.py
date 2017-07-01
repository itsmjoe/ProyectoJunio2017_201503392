class NodoListaDoble():
	"""docstring for NodoListaDobleEnlazada"""
	def __init__(self, NombreUsuario, NombreOponente,TirosLanzados,TirosAcertados,TirosFallados,EstadoJuego,DanioRecibido):
		self.siguiente=None
		self.anterior=None
		self.NombreUsuario=NombreUsuario
		self.NombreOponente=NombreOponente
		self.TirosLanzados=TirosLanzados
		self.TirosAcertados=TirosAcertados
		self.TirosFallados=TirosFallados
		self.EstadoJuego=EstadoJuego
		self.DanioRecibido=DanioRecibido