from NodoMatriz import NodoMatriz
from grafos import grafo
from ArbolAVL import ArbolAVL
from random import SystemRandom



class MatrizDispersa():
	def __init__(self):
		self.cabeza=None#Esta cabeza la utilizare para las cabeceras de empresas
		self.cabeza1 = None#Esta cabeza la utilizare para las cabeceras de departamentos
		self.tempid = None
		self.tempArbol = None
		self.tempArbol1 = None



	def insertar(self, valor):#Paso 1 Tiene todo que ver con las empresas (aqui se valida si existe, si va antes o despues); independientemente de lo 
	#									que se haga siempre se devuelve el nodo con el nombre del dominio recibido
		nodo = NodoMatriz()
		nodo.valor=valor
		aux = None#Esta variable me servira para retornar el nodo
		if self.cabeza is None:#No existe ninguna empresa, inserto la empresa en la cabeza, le asigno ese nodo a aux y lo retorno
			self.cabeza = nodo
			aux = self.cabeza
		else:
			temp = self.cabeza
			bandera = 0#Esta variable me indicara si el dominio se agrega al final de las demas empresas
			while (temp is not None):#While utilizado para recorrer de forma horizontal las empresas
				nombresEmpresas=[temp.valor, valor]
				nombresEmpresas.sort()
				if temp.valor == valor:#si la empresa recibida ya existe me limito solo a igualarlo a aux para ser posteriormente retornado
					aux = temp
					bandera = 1
					print("Esta empresa ya existe perro")
					break
				if (nombresEmpresas.index(temp.valor)==1):#Si el nodo en el que estoy es mayor al que recibi significa que deberia
													# insertar el nodo antes de este, por lo tanto lo hago y lo igualo a aux para ser retornado
					if temp == self.cabeza: #Si el nodo mayor es la cabeza se hace una operacion especial
						self.cabeza.anterior = nodo
						self.cabeza.anterior.siguiente = self.cabeza
						self.cabeza = nodo
						aux = self.cabeza
						print("Se cambio la cabeza")
					else: #Si el nodo mayor es cualquier otro diferente a la cabeza se hace lo siguiente
						temp.anterior.siguiente = nodo
						temp.anterior.siguiente.anterior = temp.anterior
						nodo.siguiente = temp
						temp.anterior = nodo
						aux = temp.anterior
						print("Se cambio nodo diferente a cabeza")
					bandera = 1
					break
				temp = temp.siguiente
			if bandera == 1 :#Bandera es igual a 1, significa que ya se creo el nodo, por lo tanto no se hace mas
				print("")
			else:# de lo contrario se agrega el dominio al final y se iguala a aux
				temp = self.cabeza
				while temp.siguiente is not None:
					temp = temp.siguiente
				temp.siguiente = nodo
				temp.siguiente.anterior = temp
				temp = temp.siguiente
				aux = temp
				print("Se ingreso al final")
		return aux

	def insertar1(self, valor):#Paso2 Tiene todo que ver con los departamentos (aqui se valida si existe, si va arriba o abajo); independientemente de lo 
	#									que se haga siempre se devuelve el nodo con el nombre del departamento recibido
		nodo = NodoMatriz()
		nodo.valor=valor
		aux = None#Esta variable me servira para retornar el nodo
		if self.cabeza1 is None:#Si no existe ningun departamento lo agrego a la cabeza
			self.cabeza1 = nodo
			aux = self.cabeza1
		else:
			temp = self.cabeza1
			bandera = 0#Me servira para saber si debo de ingresar el nodo al final
			while temp is not None:#utilizo este while para recorrer todos los nodos y validar algunos casos
				nombresDepartamentos=[temp.valor, valor]
				nombresDepartamentos.sort()
				if temp.valor == valor:#Si ya existe un nodo con el departamento recibido solo igualo el nodo a aux
					aux = temp
					bandera=1
					print("Este departamento ya existe perro")
					break
				if (nombresDepartamentos.index(temp.valor)==1):#Si existe algun nodo con inicial mayor al departamento recibido significa que el departamento recibido
													#deberia ir arriba
					if temp == self.cabeza1:#Si el departamento mayor es la cabeza se hace una operacion especial
						self.cabeza1.arriba = nodo
						self.cabeza1.arriba.abajo = self.cabeza1
						self.cabeza1 = nodo
						aux = self.cabeza1
						print("Se inserto en la cabeza")
					else:#de lo contrario se juega con los apuntadores para insertar el nodo enmedio
						temp.arriba.abajo=nodo
						temp.arriba.abajo.arriba= temp.arriba
						nodo.abajo = temp
						temp.arriba = nodo
						aux = temp.arriba
						print("Se inserto en cualquier otro lado")
					bandera =1
					break
				temp  = temp.abajo
			if bandera ==1:#Si entro en algunos casos ya no se hace nada
				print("")
			else:# de lo contrario se agrega al final y se asigna a aux para ser retornado
				temp = self.cabeza1
				while temp.abajo is not None:
					temp = temp.abajo
				temp.abajo = nodo
				temp.abajo.arriba= temp
				temp = temp.abajo
				aux = temp
				print("Se inserto al final")
		return aux

	def vis(self):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				print(temp.valor)
				temp = temp.siguiente#Para visualizar los departamentos
	def vis1(self):
		temp = self.cabeza1
		if(temp!=None):
			while(temp!=None):
				print(temp.valor)
				temp = temp.abajo#Para visualizar las empresas

	def insertarValor(self, x,valor,departamento,username,password,nombreCompleto):#Este metodo recibe el nodo empresa, el nombre del empleado, y el depto al que pertenece [Valor = username]
		#Utilizo este metodo para bajar desde la empresa y verificar donde ingresar el nodo con el nombre del empleado
		temp = NodoMatriz()#Este nodo me servira para bajar partiendo desde el nodo empresa recibido
		temp = x.abajo
		nodo = NodoMatriz()#Este nodo contendra todos los valores del empleado
		nodo.valor=valor
		nodo.empresa = x.valor
		nodo.departamento = departamento
		nodo.nombreUsuario = username
		nodo.password = password
		nodo.nombreCompleto = nombreCompleto
		aux = None#este nodo me servira para devolver el nodo de valores cuando se haya ingresado (o sea que ya tenga sus apuntadores verticales)
		bandera = 0
		if temp is None:#Si el nodo abajo del dominio es none se agrega y se iguala a aux
			x.abajo = nodo
			x.abajo.arriba = x
			aux = x.abajo
		else:
			while temp is not None:#uso este while para recorrer los empleados que existen en la empresa recibida
				nombresDepartamentos=[temp.departamento, departamento]
				nombresDepartamentos.sort()
				if temp.departamento == departamento:#Si existe un nodo con el departamento de mi nodo valor quiere decir que debo de enviarlo a atras
					if temp.atras is None:#Si 
						nodo.adelante = temp
						nodo.adelante.atras = nodo
						temp = temp.atras
					else:
						while temp.atras is not None:
							temp = temp.atras
						temp.atras = nodo
						temp.atras.adelante = temp
					bandera = 1
					break#--------------------------
				if (nombresDepartamentos.index(temp.departamento)==1): #Averiguo si deberia meter mi nodo valores antes de cualquier otro
					if temp == x:
						x.abajo = nodo
						x.abajo.arriba = x
						aux = x.abajo
					else:
						temp.arriba.abajo = nodo
						temp.arriba.abajo.arriba =temp.arriba
						nodo.abajo = temp
						temp.arriba = nodo
						aux = temp.arriba
					bandera = 1
					break
				temp = temp.abajo
			if bandera == 1:
				print("")
			else: #Si no entre a ningun caso entonces lo agrego al final de todos los correos del dominio recibido
				temp = x
				while temp.abajo is not None:
					temp = temp.abajo
				temp.abajo = nodo
				temp.abajo.arriba = temp
				temp = temp.abajo
				aux = temp
		return aux

	def unir(self,nodoDepartamento, NodoValores):#Este metodo lo utilizo para setear los apuntadores horizontales de mi nodo valores
	#									  por eso recibo como valores mi nodo letra y mi nodo valores(el cual ya tiene sus apuntadores verticales)
		if NodoValores != None:#Esta validacion la hago porque cuando agrego nodos atras de cualquier otro ya no retorno ese nodo porque ya tiene apuntadores
			bandera = 0
			print(nodoDepartamento)
			if nodoDepartamento.siguiente is None:#Si no existe ningun nodo siguiente al encabezado de la letra lo agrego ahi
				NodoValores.anterior = nodoDepartamento
				NodoValores.anterior.siguiente = NodoValores
			else:#Si ya existe algun nodo, entonces debo de recorre hacia la derecha para ver si el dominio de mi nodo valores va antes que otro 
			# nodo de valores porque su dominio es menor o si mi nodo valores va hasta de ultimo 
				temp = nodoDepartamento.siguiente
				#//--print("----------", temp.dominio, NodoValores.dominio,ord((temp.dominio)[0]), ord((NodoValores.dominio)[0]))
				while  temp is not None:#Para recorrer los nodos valores apuntados por el nodo depto
					nombresDepartamentos=[temp.valor, NodoValores.departamento]
					nombresDepartamentos.sort()
					if(nombresDepartamentos.index(temp.departamento)==1):#si algun departamento es mayor al de mi nodo valores lo agrego antes
					#if ord((temp.dominio)[0])> ord((NodoValores.dominio)[0]):
						temp.anterior.siguiente= NodoValores
						temp.anterior.siguiente.anterior= temp.anterior
						NodoValores.siguiente = temp
						temp.anterior = NodoValores
						bandera =1
						break
					temp = temp.abajo
				if bandera != 1:#Si ningun dominio era mayor entonces lo agrego al final de todos los nodos valores apuntados por ese nodo letra
					temp = nodoDepartamento.siguiente
					while temp.siguiente is not None:
						temp = temp.siguiente
					temp.siguiente = nodoDepartamento
					temp.siguiente.anterior = temp

	def visualizar1(self, aux):#Este metodo recibe un nodo dominio e imprime todos los hijos de es dominio
		print("---------------Visualizando horizontalmente-----")
		text = ""
		temp = aux.abajo
		while temp is not None:
			text += temp.anterior.valor+" | "+temp.valor+"\n"
			print(temp.anterior.valor," | ",temp.valor)
			if temp.atras != None:
				a=temp.atras
				while a != None:
					text += "---->"+a.valor+"\n"
					print("---->"+a.valor+"\n")
					a = a.atras
			temp = temp.abajo
		return text	

	def getCodigoGraphviz(self):
	 	 return "digraph grafica{\n" + "rankdir=TB;\n" + "node [shape = record, style=filled, fillcolor=seashell2];\n" + self.graficarMatriz() + "}\n"

	def graficarMatriz(self):
		texto =""
		tempDepartamento = self.cabeza1
		contador = 0
		while tempDepartamento != None:
			tempDepartamento.indice = contador
			texto += str(tempDepartamento.indice) +"[label =\"<C0>|" + tempDepartamento.valor + "|<C1>\"];\n"
			aux  = tempDepartamento.siguiente
			while aux!=None:
				contador+=1
				aux.arriba.indice = contador
				texto += str(aux.arriba.indice) +"[label =\"<C0>|" + aux.arriba.valor + "|<C1>\"];\n"
				contador +=1
				aux.indice = contador
				texto += str(aux.indice) +"[label =\"<C0>|" + aux.valor + "|<C1>\"];\n"
				aux = aux.siguiente
			contador += 1
			tempDepartamento = tempDepartamento.abajo
		tempDepartamento = self.cabeza1
		while tempDepartamento != None:
			if tempDepartamento.abajo != None:
				texto += str(tempDepartamento.indice) +"->"+str(tempDepartamento.abajo.indice)+";\n"
			if tempDepartamento != self.cabeza1:
				texto += str(tempDepartamento.indice) +"->"+str(tempDepartamento.arriba.indice)+";\n"
			aux  = tempDepartamento.siguiente
			while aux!=None:
				if aux.arriba.anterior != None:
					texto += str(aux.arriba.indice) +":C0->"+str(aux.arriba.anterior.indice)+":C1;\n"
					texto += str(aux.arriba.anterior.indice) +":C1->"+str(aux.arriba.indice)+":C0;\n"
				texto += str(aux.anterior.indice) +":C1->"+str(aux.indice)+":C0;\n"
				texto += str(aux.indice) +":C0->"+str(aux.anterior.indice)+":C1;\n"
				#texto += str(aux.indice)+"->"+str(aux.arriba.indice)+";\n"
				#texto += str(aux.arriba.indice)+"->"+str(aux.indice)+";\n"
				aux = aux.siguiente
			tempDepartamento = tempDepartamento.abajo
		return texto


	def iniciarSesion(self,empresa,departamento,username,password):
		bandera = 0
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username and temp.password == password):
							bandera= 1
							break
						temp = temp.atras
		return bandera#Verifica que los datos existan en la matriz

	def verificarExistencia(self,empresa,departamento,username,nombreCompleto):
		print("estoy verificando")
		bandera = 0
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					print("Match empresa")
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						print("Match departamento")
						break
					temp = temp.abajo
				if(temp!=None):
					print("PASE")
					while(temp!=None):
						#print(temp.nombreUsuario+" , "+username)
						if(temp.nombreUsuario==username or temp.nombreCompleto == nombreCompleto):
							bandera= 1
							print("Que hongos, porque no marca?")
							break
						temp = temp.atras
		return bandera#Verifica que no exista un usuario igual en la misma empresa y depto

	def insertarActivo(self,empresa,departamento,username,nombreActivo,descripcionActivo):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					print("Match empresa")
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						print("Match departamento")
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):
							print("Match Usuario")
							print(temp.empresa)
							print(temp.departamento)
							print(temp.nombreUsuario)
							print(temp.nombreCompleto)
							longitud = 18
							valores = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
							cryptogen = SystemRandom()
							p = ""
							while longitud > 0:
								p = p + cryptogen.choice(valores)
								longitud = longitud - 1
							print(p)
							if(temp.AVL==None):
								#print("Vacio")
								#temp.AVL ="Algo"
								arboltexto=ArbolAVL()
								arboltexto.insertar(p,nombreActivo,descripcionActivo)
								temp.AVL = arboltexto
								temp.AVL.inorden()
							else:
								temp.AVL.insertar(p,nombreActivo,descripcionActivo)
								temp.AVL.inorden()
								#print("Ya hay algo")
							break
						temp = temp.atras
	def listadoIds(self):
		texto =""
		tempEmpresa = self.cabeza
		while(tempEmpresa!=None):
			print(tempEmpresa.valor)
			aux =tempEmpresa.abajo
			if(aux!=None):
				while(aux != None):
					#print("--"+aux.departamento)
					#print("--"+aux.empresa)
					#print("--"+aux.valor)
					#print(self.obtenerIds("Usac","Ventas","Memo"))
					textoTemp = self.obtenerIds(aux.empresa,aux.departamento,aux.valor)
					if(textoTemp!="Usuario sin activos ingresados"):
						texto += textoTemp
					aux1 = aux.atras
					if(aux1!=None):
						while(aux1!=None):
							textoTemp1 = self.obtenerIds(aux1.empresa,aux1.departamento,aux1.valor)
							if(textoTemp1!="Usuario sin activos ingresados"):
								texto += textoTemp1
							aux1 = aux1.atras
					aux = aux.abajo
			tempEmpresa =  tempEmpresa.siguiente
		return texto
		
	def obtenerIds(self,empresa,departamento,username):
		print("Entre................ "+empresa+" | "+departamento+" | "+username)
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					print("Match empresa")
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						print("Match departamento")
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):

							if(temp.AVL==None):
								return "Usuario sin activos ingresados"
							else:
								temp.AVL.obtenerListaIds()
								print("Supuesto TAMAnio "+str(len(temp.AVL._Lista)))
								Lista = temp.AVL._Lista
								t=""
								for item in Lista:
									t+=item+","
								return t
							break
						temp = temp.atras

	def obtenerDatos(self,empresa,departamento,username,id):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					print("Match empresa")
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						print("Match departamento")
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):#------------------------------------
							if(temp.AVL==None):
								return "Usuario sin activos ingresados"
							else:
								temp.AVL.obtenerDatos(id)
								Lista = temp.AVL._auxNombreActivo+","+temp.AVL._auxDescripcion
								print(temp.AVL._auxNombreActivo)
								print("QUE COMIENZE EL JUEGO...")
								return Lista
								#--------------------------------------------------------------
							break
						temp = temp.atras

	def actualizarActivo(self,empresa,departamento,username,id,descripcion):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					print("Match empresa")
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						print("Match departamento")
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):#------------------------------------
							if(temp.AVL==None):
								return "Error"
							else:
								temp.AVL.actualizarDatos(id,descripcion)
								return "Actualizacion Exitosa"
								#--------------------------------------------------------------
							break
						temp = temp.atras

	def eliminarActivo(self,empresa,departamento,username,id):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):#------------------------------------
							if(temp.AVL==None):
								return "Error"
							else:
								self.eliminar(temp.AVL,id)
								if(self.tempArbol._raiz!=None):
									temp.AVL=self.tempArbol
								else:
									temp.AVL = None
								return "Eliminacion Exitosa"
								#--------------------------------------------------------------
							break
						temp = temp.atras
	def eliminar(self,arbol,id):
		self.tempArbol = ArbolAVL()
		self.tempid = id
		self.eliminar1(arbol._raiz)

	def eliminar1(self, a):
		if a == None:
			return 
		if(a._valor != self.tempid):
			self.tempArbol.insertar(a._valor,a._nombre,a._descripcion)
		self.eliminar1(a._izquierdo)
		self.eliminar1(a._derecho)

	def graficarAvl(self,empresa,departamento,username):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):#------------------------------------
							if(temp.AVL==None):
								return "Este usuario no tiene activos"
							else:
								texto = temp.AVL._raiz.getCodigoGraphviz()
								return texto
								#--------------------------------------------------------------
							break
						temp = temp.atras

	def obtenerNombre(self,empresa,departamento,username):
		temp = self.cabeza
		if(temp!=None):
			while(temp!=None):
				if(temp.valor == empresa):
					break
				temp = temp.siguiente
			if(temp!=None):
				temp= temp.abajo
				while(temp!=None):
					if(temp.departamento==departamento):
						break
					temp = temp.abajo
				if(temp!=None):
					while(temp!=None):
						if(temp.nombreUsuario==username):#------------------------------------
							if(temp.AVL==None):
								return "Este usuario no tiene activos"
							else:
								texto = temp.nombreCompleto
								return texto
								#--------------------------------------------------------------
							break
						temp = temp.atras

	def prestar(self,id):
		texto =""
		tempEmpresa = self.cabeza
		while(tempEmpresa!=None):
			print(tempEmpresa.valor)
			aux =tempEmpresa.abajo
			if(aux!=None):
				while(aux != None):
					self.prestar1(aux.AVL._raiz,id)
					aux1 = aux.atras
					if(aux1!=None):
						while(aux1!=None):
							self.prestar1(aux1.AVL._raiz,id)
							aux1 = aux1.atras
					aux = aux.abajo
			tempEmpresa =  tempEmpresa.siguiente
		return texto


	def prestar1(self, a,id):
		if a == None:
			return 
		if(a._valor == id):
			print("SI preste")
			a._estado = "Prestado"
		self.prestar1(a._izquierdo,id)
		self.prestar1(a._derecho,id)

	def devolver(self,id):
		texto =""
		tempEmpresa = self.cabeza
		while(tempEmpresa!=None):
			print(tempEmpresa.valor)
			aux =tempEmpresa.abajo
			if(aux!=None):
				while(aux != None):
					self.devolver1(aux.AVL._raiz,id)
					aux1 = aux.atras
					if(aux1!=None):
						while(aux1!=None):
							self.devolver1(aux1.AVL._raiz,id)
							aux1 = aux1.atras
					aux = aux.abajo
			tempEmpresa =  tempEmpresa.siguiente
		return texto


	def devolver1(self, a,id):
		if a == None:
			return 
		if(a._valor == id):
			a._estado = "Disponible"
		self.devolver1(a._izquierdo,id)
		self.devolver1(a._derecho,id)

	def obtenerDatosID(self,id):
		texto =""
		tempEmpresa = self.cabeza
		while(tempEmpresa!=None):
			print(tempEmpresa.valor)
			aux =tempEmpresa.abajo
			if(aux!=None):
				while(aux != None):
					textoTemp =self.obtenerDatosID1(aux.AVL._raiz,id)
					if(textoTemp != None):
						texto=textoTemp
					aux1 = aux.atras
					if(aux1!=None):
						while(aux1!=None):
							textoTemp =self.obtenerDatosID1(aux1.AVL._raiz,id)
							if(textoTemp != None):
								texto=textoTemp
							aux1 = aux1.atras
					aux = aux.abajo
			tempEmpresa =  tempEmpresa.siguiente
		return texto


	def obtenerDatosID1(self, a,id):
		if a == None:
			return 
		if(a._valor == id):
			print("si lo encontre, pero sber que hongos")
			texto = a._nombre+","+a._descripcion
			return texto
		self.obtenerDatosID1(a._izquierdo,id)
		self.obtenerDatosID1(a._derecho,id)