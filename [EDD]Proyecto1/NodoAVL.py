
class NodoAVL(object):
    def __init__(self, valor,nombre,descripcion):
        self._correlativo = 1
        self._valor = valor#Este es el atributo id (pero con otro nombre...)
        self._nombre = nombre
        self._descripcion = descripcion
        self._estado = "Disponible"
        self._izquierdo = None
        self._altura=0
        self._derecho = None
        self._id = self._correlativo =self._correlativo+1

    def insertar(self, val):
        if val.compareTo(self._valor) < 0:
            if self._izquierdo == None:
                self._izquierdo = NodoAVL(val)
            else:
                self._izquierdo.insertar(val)
        elif val.compareTo(self._valor) > 0:
            if self._derecho == None:
                self._derecho = NodoAVL(val)
            else:
                self._derecho.insertar(val)
        else:
            print("No se permiten los valores duplicados: \"" + String.valueOf(val) + "\".")

    def getCodigoGraphviz(self):
        return "digraph grafica{\n" + "rankdir=TB;\n" + "node [shape = record, style=filled, fillcolor=seashell2];\n" + self.getCodigoInterno() + "}\n"

    def getCodigoInterno(self):
        if self._izquierdo == None and self._derecho == None:
            etiqueta = "nodo" + str(self._id) + " [ label =\"" + self._valor+"\n"+self._nombre+"\n"+self._descripcion+"\n"+self._estado+"\n"+ "\"];\n"
        else:
            etiqueta = "nodo" + str(self._id) + " [ label =\"<C0>|" + self._valor + "|<C1>\"];\n"
        if self._izquierdo != None:
            etiqueta = etiqueta + self._izquierdo.getCodigoInterno() + "nodo" + str(self._id) + ":C0->nodo" + str(self._izquierdo._id) + "\n"
        if self._derecho != None:
            etiqueta = etiqueta + self._derecho.getCodigoInterno() + "nodo" + str(self._id) + ":C1->nodo" + str(self._derecho._id) + "\n"
        return etiqueta

