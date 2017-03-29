from MatrizDispersa import MatrizDispersa
from ArbolAVL import ArbolAVL
from flask import Flask, request, Response,render_template
from random import SystemRandom

app = Flask(__name__)

class principal():
    global lista
    global matriz
    matriz = MatrizDispersa()

    @app.route('/') 
    def metodo1():
        return "WEB SERVICE PROYECTO 1 FUNCIONANDO"

    @app.route('/ingresarUsuario',methods=['GET'])
    def metodo2():
        return render_template('index.html')
    #Este metodo ingresara un usuario a la matriz dispersa PARAMETROS:empresa, departamento, username,password,nombrecompleto
    @app.route('/ingresarUsuario',methods=['POST'])#Este metodo ingresa un usuario [Retorna SI se pudo crear el usuario de lo contrario retorna NO]
    def metodo3():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        parametro4 = str(request.form['password'])
        parametro5 = str(request.form['nombrecompleto'])
        texto = ""
        if(matriz.verificarExistencia(parametro1,parametro2,parametro3,parametro5)==0):
            encabezadoEmpresa = matriz.insertar(parametro1)#Envio mi empresa y recibo un nodo empresa
            encabezadoDepartamento = matriz.insertar1(parametro2)#Envio mi depto y recibo el nodo depto
            Nodo = matriz.insertarValor(encabezadoEmpresa,parametro3,parametro2,parametro3,parametro4,parametro5)
            matriz.unir(encabezadoDepartamento,Nodo)
            texto = "SI"
        else:
            texto = "NO"
        return texto

    @app.route('/crearActivo',methods=['GET'])
    def metodo4():
        return render_template('b.html')


    @app.route('/crearActivo',methods=['POST'])#Este metodo crea activos, Recibe empresa,departamento,username,nombreActivo y descripcionActivo
    def metodo5():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        parametro4 = str(request.form['nombreActivo'])
        parametro5 = str(request.form['descripcionActivo'])
        matriz.insertarActivo(parametro1,parametro2,parametro3,parametro4,parametro5)
        return "Activo ingresado!!!"

    @app.route('/inicioSesion',methods=['GET'])#Este metodo verifica si se puede iniciar sesion [Retorna SI o No dependiendo si concuerdan los parametros]
    def metodo7():
        return render_template('a.html')

    @app.route('/inicioSesion',methods=['POST'])#Este metodo es para el login[Retorna NO si los datos son incorrectos de lo contrario retorna SI]
    def metodo8():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        parametro4 = str(request.form['password'])
        print("Empresa "+parametro1+" Departamento "+parametro2+" username "+parametro3+" password "+parametro4)
        bandera = matriz.iniciarSesion(parametro1,parametro2,parametro3,parametro4)
        if bandera == 0:
            texto="NO"
        else:
            texto="SI"
        print(str(bandera))
        return texto

    @app.route('/obtenerIds',methods=['GET'])
    def metodo9():
        return render_template('c.html')

    @app.route('/obtenerIds',methods=['POST'])#Este metodo retorna una lista con TODOS los ids del username ingresado
    def metodo10():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        lista = matriz.obtenerIds(parametro1,parametro2,parametro3)
        return lista


    @app.route('/graficarMatriz',methods=['GET'])#Para graficar la matriz
    def metodo11():
        texto = matriz.getCodigoGraphviz()
        print(texto)
        return texto

    @app.route('/obtenerDatos',methods=['GET'])
    def metodo12():
        return render_template('d.html')

    @app.route('/obtenerDatos',methods=['POST']) #Este metodo obtiene los datos segun el id enviado. [Retorna una lista donde la posicion 0 es el nombre del activo y la pos 1 es su descripcion]
    def metodo13():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        parametro4 = str(request.form['id'])
        lista = matriz.obtenerDatos(parametro1,parametro2,parametro3,parametro4)
        return lista


    @app.route('/actualizarDescripcion',methods=['GET'])
    def metodo14():
        return render_template('e.html')

    @app.route('/actualizarDescripcion',methods=['POST'])#Este metodo modifica la descripcion de algun activo[*el id es el del activo]
    def metodo15():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        parametro4 = str(request.form['id'])
        parametro5 = str(request.form['descripcion'])
        texto = matriz.actualizarActivo(parametro1,parametro2,parametro3,parametro4,parametro5)
        return texto

    @app.route('/eliminarActivo',methods=['GET'])
    def metodo16():
        return render_template('f.html')

    @app.route('/eliminarActivo',methods=['POST'])#Este metodo elimina activos
    def metodo17():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        parametro4 = str(request.form['id'])
        texto = matriz.eliminarActivo(parametro1,parametro2,parametro3,parametro4)
        return texto

    @app.route('/graficarAvl',methods=['GET'])
    def metodo18():
        return render_template('g.html')

    @app.route('/graficarAvl',methods=['POST'])#Para graficar el AVL
    def metodo19():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        texto = matriz.graficarAvl(parametro1,parametro2,parametro3)
        print(texto)
        return texto

    @app.route('/obtenerNombre',methods=['GET'])
    def metodo20():
        return render_template('h.html')#Falta crearlo

    @app.route('/obtenerNombre',methods=['POST'])#Para obtener el nombre [Retorna el nombre del usuario ingresado]
    def metodo21():
        parametro1 = str(request.form['empresa'])
        parametro2 = str(request.form['departamento'])  
        parametro3 = str(request.form['username'])
        texto = matriz.obtenerNombre(parametro1,parametro2,parametro3)
        return texto

    @app.route('/prueba',methods=['POST'])#Metodo por molestar
    def metodo22():
        parametro1 = str(request.form['nombre'])
        return "Si se pudo!!!"

    @app.route('/nuevo',methods=['GET'])
    def metodo23():
        return render_template('i.html')#Falta crearlo

    @app.route('/nuevo',methods=['POST'])#Este metodo retorna una lista con TODOS los ids del username ingresado
    def metodo24():
        parametro1 = str(request.form['nombre'])
        lista = matriz.listadoIds()
        return lista

    @app.route('/prestarActivo',methods=['GET'])
    def metodo25():
        return render_template('j.html')

    @app.route('/prestarActivo',methods=['POST'])#Este metodo presta activos [Enviamos el id del activo a prestar]
    def metodo26():
        parametro1 = str(request.form['id'])
        texto = matriz.prestar(parametro1)
        return texto

    @app.route('/devolverActivo',methods=['GET'])
    def metodo27():
        return render_template('k.html')

    @app.route('/devolverActivo',methods=['POST'])#Este metodo devuelve activos  [Mandamos el id del activo a devolver]
    def metodo28():
        parametro1 = str(request.form['id'])
        texto = matriz.devolver(parametro1)
        return texto

    @app.route('/obtenerDatosID',methods=['GET'])
    def metodo29():
        return render_template('l.html')

    @app.route('/obtenerDatosID',methods=['POST'])#Este metodo devuelve activos  [Mandamos el id del activo a devolver]
    def metodo30():
        parametro1 = str(request.form['id'])
        texto = matriz.obtenerDatosID(parametro1)
        return texto

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')