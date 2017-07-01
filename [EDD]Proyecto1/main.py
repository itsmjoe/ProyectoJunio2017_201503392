from flask import Flask,request,Response
from ArbolBinario import ArbolBinario
from ListaDoble import ListaDoble
from MatrizDispersa import MatrizDispersa
AB=ArbolBinario()
LD=ListaDoble()
app = Flask("EDD_codigo_ejemplo")


@app.route("/IniciarUsuario",methods=["POST"])
def IniciarSesion():
	var1=str(request.form["usuario"])
	var2=str(request.form["contra"])
	#print(var1+" "+var2)
	nodo=AB.BuscarNodo(var1)
	if nodo!=None:
		if nodo.dato==var1 and nodo.passw==var2:
			nodo.estado=1
			nodo.ListaJuegos=ListaDoble()
			nodo.MatrizDispersa=MatrizDispersa()
			print("Usuario valido.")
			return 'True'
	else:
		print("El usuario no existe.")
		return 'False'
	
@app.route("/ArbolEspejo",methods="POST")
def ArbolEspejo():
	AB.CrearReporte()
	return "reporte"

@app.route("/IngresarUsuario",methods=["POST"])
def IngresarUsuario():
	var1=str(request.form["usuario"])
	var2=str(request.form["contra"])
	var3=str(request.form["estado"])
	#print(var1+" "+var2)
	nodo=AB.BuscarNodo(var1)
	if nodo==None:
		AB.Insertar(var1,var2,var3)
		user=AB.BuscarNodo(var1)
		user.ListaJuegos=ListaDoble()
		user.MatrizDispersa=MatrizDispersa()
		print(var1+" insertado "+var2)
	else:
		print("El usuario ya existe.")
	return 'True'

@app.route("/IngresarJuego",methods=["POST"])
def IngresarJuego():
	var1=str(request.form["usuario"])
	var2=str(request.form["oponente"])
	var3=str(request.form["lanzados"])
	var4=str(request.form["acertados"])
	var5=str(request.form["fallados"])
	var6=str(request.form["estadojuego"])
	var7=str(request.form["danio"])
	user=AB.BuscarNodo(var1)#verificar si existe el usuario y oponente y que ambos esten conectados
	opo=AB.BuscarNodo(var2)
	#user.ListaJuegos=ListaDoble()
	if user!=None and opo!=None:
		user.ListaJuegos.InsertarPrimero(var1,var2,var3,var4,var5,var6,var7)
		print(var1 +" "+ var2)
		#user.ListaJuegos.MostrarPrimeroUltimo()
		return 'Truell'
	else:
		print "Un usuario no existe."
		return "False"

@app.route("/IngresarJuegoActual",methods=["POST"])
def IngresarJuegoActual():
	var1=str(request.form["usuario"])
	var2=str(request.form["oponente"])
	var3=str(request.form["tamx"])
	var4=str(request.form["tamy"])
	var5=str(request.form["variante"])
	var6=str(request.form["tiempo"])
	var7=str(request.form["disparo"])
	var8=str(request.form["nrafagas"])
	#AB.MostrarInorden(AB.DameRaiz())
	#print(var1+" "+var2+" ---------------------------------")
	user2=AB.BuscarNodo(var2)
	user1=AB.BuscarNodo(var1)	
	#print(var1+" "+var2+ " | " + str(user1.dato)+ " "+ str(user2.dato))
	if user1!=None and user2!=None:
		user1.MatrizDispersa.Nivel1=MatrizDispersa()
		user1.MatrizDispersa.Nivel2=MatrizDispersa()
		user1.MatrizDispersa.Nivel3=MatrizDispersa()
		user1.MatrizDispersa.Nivel4=MatrizDispersa()
		user2.MatrizDispersa.Nivel1=MatrizDispersa()
		user2.MatrizDispersa.Nivel2=MatrizDispersa()
		user2.MatrizDispersa.Nivel3=MatrizDispersa()
		user2.MatrizDispersa.Nivel4=MatrizDispersa()
		user1.MatrizDispersa.Nivel1.CrearMatriz(int(var3),int(var4))
		user1.MatrizDispersa.Nivel2.CrearMatriz(int(var3),int(var4))
		user1.MatrizDispersa.Nivel3.CrearMatriz(int(var3),int(var4))
		user1.MatrizDispersa.Nivel4.CrearMatriz(int(var3),int(var4))
		user2.MatrizDispersa.Nivel1.CrearMatriz(int(var3),int(var4))
		user2.MatrizDispersa.Nivel2.CrearMatriz(int(var3),int(var4))
		user2.MatrizDispersa.Nivel3.CrearMatriz(int(var3),int(var4))
		user2.MatrizDispersa.Nivel4.CrearMatriz(int(var3),int(var4))
		user1.MatrizDispersa.Nivel1.Imprimir(user1.MatrizDispersa.Nivel1.m)
		print("Matriz dispersa creadaa.")
		return 'True'
	else:
		print("Matriz dispersa no creadaa.")
		return 'False'

@app.route("/IngresarNaves",methods=["POST"])
def IngresarNaves():
	var1=str(request.form["usuario"])
	var2=str(request.form["col"])
	var3=str(request.form["fila"])
	var4=str(request.form["nivel"])
	var5=str(request.form["modo"])
	var6=str(request.form["dir"])
	user=AB.BuscarNodo(var1)
	if user!=None:
		user.MatrizDispersa.Insertar(var2,int(var3),int(var4),int(var5),int(var6))
		#user.MatrizDispersa.Nivel4.Imprimir(user.MatrizDispersa.Nivel4.m)
		return "True"
	else:
		print("Usuario no encontrado.")
		return "False"

@app.route("/RegistrarUsuario",methods=["POST"])
def Registrar():
	var1=str(request.form["usuario"])
	var2=str(request.form["contra"])
	var3=str(request.form["contra2"])
	#print(var1+" "+var2+ " "+var3)
	nodo=AB.BuscarNodo(var1)
	if nodo==None:
		if var2==var3:
			AB.Insertar(var1,var2,0)
			user=AB.BuscarNodo(var1)
			user.ListaJuegos=ListaDoble()
			user.MatrizDispersa=MatrizDispersa()
			AB.MostrarInorden(AB.DameRaiz())
			return 'True'
	else:
		print("El usuario ya existe.")
		return 'False'
	
if __name__=="__main__":
	app.run(debug=True,host='0.0.0.0')