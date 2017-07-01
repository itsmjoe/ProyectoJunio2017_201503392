from NodoMatrizDispersa import NodoMatrizDispersa
class MatrizDispersa(object):
	"""docstring for MatrizDispersa"""
	def __init__(self):
		self.m=None
		self.Nivel1=None
		self.Nivel2=None
		self.Nivel3=None
		self.Nivel4=None

	def CrearMatriz(self,f,c):
		#print(str(f) + " " + str(c))
		self.m=NodoMatrizDispersa(0,0,0)
		self.m.siguientefila=self.m
		self.m.siguientecol=self.m
		i=1
		q=self.m
		while (i<=f):
			nuevo=NodoMatrizDispersa(0,i,0)
			q.siguientefila=nuevo
			nuevo.siguientecol=nuevo
			q=nuevo
			i+=1
		q.siguientefila=self.m
		#print(str(self.m.dato))
		i=1
		q=self.m
		#print(str(q.dato)+" antes de while")
		while (i<=c):
			nuevo=NodoMatrizDispersa(0,0,i)
			q.siguientecol=nuevo
			nuevo.siguientefila=nuevo
			q=nuevo
			i+=1
		q.siguientecol=self.m

	def Arriba(self,f,c):
		aux=self.m.siguientecol
		while (aux.col!=c):
			aux=aux.siguientecol
		aux1=aux.siguientefila
		aux2=aux1.siguientefila
		while (aux1.fila<f and aux2.fila!=0):
			aux=aux1
			aux1=aux1.siguientefila
			aux2=aux2.siguientefila
		if (aux1.fila<f):
			return aux1
		else:
			return aux

	def Izquierda(self,f,c):
		aux=self.m.siguientefila
		while aux.fila!=f:
			aux=aux.siguientefila

		aux1=aux.siguientecol
		aux2=aux1.siguientecol
		while (aux1.col<0 and aux2.col!=0):
			aux	=aux1
			aux1=aux1.siguientecol
			aux2=aux2.siguientecol
		if aux1.col<c:
			return aux1
		else:
			return aux

	def InsertarMatriz(self,dato,f,c):
		q=self.Arriba(f,c)
		p=self.Izquierda(f,c)
		nuevo=NodoMatrizDispersa(dato,f,c)
		nuevo.siguientefila=q.siguientefila
		q.siguientefila=nuevo
		nuevo.siguientecol=p.siguientecol
		p.siguientecol=nuevo


	def Insertar(self,columna,fila,tipo,modo,direccion):
		columna=self.DameColumna(columna)
		if tipo==1:
			self.Nivel1.InsertarMatriz("s",fila,columna)
		elif tipo==2:
			if fila==1:
				fila=fila+1
			if modo==1:
				self.Nivel2.InsertarMatriz("a",fila-1,columna)
				self.Nivel2.InsertarMatriz("a",fila,columna)
				self.Nivel2.InsertarMatriz("a",fila+1,columna)
				self.Nivel2.InsertarMatriz("a",fila+2,columna)
				self.Nivel2.InsertarMatriz("a",fila,columna+1)
				self.Nivel2.InsertarMatriz("a",fila,columna-1)
			elif modo==2:
				self.Nivel2.InsertarMatriz("a",fila,columna)
				self.Nivel2.InsertarMatriz("a",fila+1,columna)
				self.Nivel2.InsertarMatriz("a",fila,columna-1)
			else:
				print("Modo de avion no encontrado.")
		elif tipo==3:
			if fila==1:
				fila=fila+1
			if direccion==1:#horizonatal
				columna=columna+1
				for x in range(modo):
					self.Nivel3.InsertarMatriz("B",fila,columna)
					columna-=1
			elif direccion==2:#vertical
				fila=fila-1
				for x in range(modo):
					self.Nivel3.InsertarMatriz("B",fila,columna)
					fila+=1
		elif tipo==4:
			if fila==1:
				fila=fila+1
			if direccion==1:#horizonatal
				columna=columna+1
				for x in range(modo):
					self.Nivel4.InsertarMatriz("S",fila,columna)
					columna-=1
			elif direccion==2:#vertical
				fila=fila-1
				for x in range(modo):
					self.Nivel4.InsertarMatriz("S",fila,columna)
					fila+=1

	def DameColumna(self,letra):
		col=ord(letra)
		return (col-64)				

	def InsertarNave(self,columna,fila,nivel,modo,direccion):
		if nivel==1: # satelites
			#buscar el nivel de satelites alv
			self.InsertarMatriz("sat",fila,columna)
		elif nivel==2: #aviones
			if modo==1:
				pass
				#self.InsertarMatriz(8,f,c)
			elif modo==2:
				pass			
			else:
				print("Modo de avion no encontrado.")
		elif nivel==3: #barcos
			if modo==1:
				#self.InsertarMatriz(8,f,c)
				if direccion==1: #vertical
					#self.InsertarMatriz(8,f,c)
					pass
				elif direccion==2:
					pass
				else:
					print("Direccion de barco no encontrada")
			elif modo==2:
				if direccion==1: #vertical
					#self.InsertarMatriz(8,f,c)
					pass
				elif direccion==2:
					pass
				else:
					print("Direccion de barco no encontrada")
			elif modo==3:
				if direccion==1: #vertical
					#self.InsertarMatriz(8,f,c)
					pass
				elif direccion==2:
					pass
				else:
					print("Direccion de barco no encontrada")
			else:
				print("Modo de barco no encontrado.")
		elif nivel==4: #submarinos
		 	if modo==1:
		 		if direccion==1: #vertical
					#self.InsertarMatriz(8,f,c)
					pass
				elif direccion==2:
					pass
				else:
					print("Direccion de barco no encontrada")
				#self.InsertarMatriz(8,f,c)
			elif modo==2:
				if direccion==1: #vertical
					#self.InsertarMatriz(8,f,c)
					pass
				elif direccion==2:
					pass
				else:
					print("Direccion de barco no encontrada")
			elif modo==3:
				if direccion==1: #vertical
					#self.InsertarMatriz(8,f,c)
					pass
				elif direccion==2:
					pass
				else:
					print("Direccion de barco no encontrada")
			else:
				print("Modo de submarino no encontrado.")


	def Imprimir(self,M):
		o=NodoMatrizDispersa(0,0,0)
		nca=ncc=nt=0
		e=NodoMatrizDispersa(0,0,0)
		aux=M.siguientecol
		print(" "+str(M.dato)+" |"),
		while aux.col!=M.col:
			print(""+str(aux.col)+" |"),
			aux=aux.siguientecol
		print("")
		aux=M.siguientefila
		while aux.fila!=M.fila:
			print(" "+str(aux.fila)	+" |"),
			o=aux
			e=aux.siguientecol
			while (o!=e):
				nc=e.col
				nt=nc
				nf=e.fila
				if nf==nca:
					nc=nc-ncc
				for x in xrange(1,nc):
					print("  |"),
				print(str(e.dato)+" |"),
				e=e.siguientecol
				nca=nf
				ncc=nt
			print(" ")
			aux=aux.siguientefila





