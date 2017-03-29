using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;

namespace ArbolBDestino
{

    public class ArbolDestinos
    {

        private RamaArbol raiz;
        private String nodos = "";

        /**
         * Constructor de Arbol B para destinos
         */
        public ArbolDestinos()
        {
        }

        /**
         * Verifica el contenido del árbol
         * @return true - Si el árbol está vacío; false - Si no lo está
         */
        public Boolean estaVacio()
        {
            return raiz == null;
        }

        /**
         *
         * @param val
         */
        public void insertar(IComparable idTransaccion, int idActivo, string usuario, string empresa, string departamento, string fecha, int duracionRenta)
        {
            NodoRamaArbol nodo = new NodoRamaArbol(idTransaccion, idActivo, usuario, empresa, departamento, fecha, duracionRenta);
            if (estaVacio())
            {
                raiz = new RamaArbol();
                raiz.insertar(nodo);
            }
            else
            {
                Object obj = inserta(nodo, raiz);
                if (obj is NodoRamaArbol)
                {
                    raiz = new RamaArbol();
                    raiz.insertar((NodoRamaArbol)obj);
                    raiz.setHoja(false);
                }
            }
            Console.WriteLine(nodo);
        }




        private Object inserta(NodoRamaArbol nodo, RamaArbol rama)
        {
            if (rama.esHoja())
            {
                rama.insertar(nodo);
                if (rama.getCuenta() == 5)
                {
                    return dividir(rama);
                }
                else
                {
                    return rama;
                }
            }
            else
            {
                NodoRamaArbol temp = rama.getPrimero();
                do
                {
                    if (nodo.getIdTransaccion().CompareTo(temp.getIdTransaccion()) == 0)
                    {
                        return rama;
                    }
                    else if (nodo.getIdTransaccion().CompareTo(temp.getIdTransaccion()) < 0)
                    {
                        Object obj = inserta(nodo, temp.getIzquierda());
                        if (obj is NodoRamaArbol)
                        {
                            rama.insertar((NodoRamaArbol)obj);
                            if (rama.getCuenta() == 5)
                            {
                                return dividir(rama);
                            }
                        }
                        return rama;
                    }
                    else if (temp.getSiguiente() == null)
                    {
                        Object obj = inserta(nodo, temp.getDerecha());
                        if (obj is NodoRamaArbol)
                        {
                            rama.insertar((NodoRamaArbol)obj);
                            if (rama.getCuenta() == 5)
                            {
                                return dividir(rama);
                            }
                        }
                        return rama;
                    }
                    temp = temp.getSiguiente();
                } while (temp != null);
            }
            return rama;
        }

        private NodoRamaArbol dividir(RamaArbol rama)
        {
            RamaArbol derecha = new RamaArbol(), izquierda = new RamaArbol();
            NodoRamaArbol medio = null, temp = rama.getPrimero();
            for (int i = 1; i < 6; i++, temp = temp.getSiguiente())
            {
                NodoRamaArbol nodo = new NodoRamaArbol(temp.getIdTransaccion(), temp.getIdActivo(), temp.getUsuario(), temp.getEmpresa(), temp.getDepartamento(), temp.getFecha(), temp.getDuracionRenta());
                nodo.setIzquierda(temp.getIzquierda());
                nodo.setDerecha(temp.getDerecha());
                if (nodo.getDerecha() != null && nodo.getIzquierda() != null)
                {
                    izquierda.setHoja(false);
                    derecha.setHoja(false);
                }
                switch (i)
                {
                    case 1:
                    case 2:
                        izquierda.insertar(nodo);
                        break;
                    case 3:
                        medio = nodo;
                        break;
                    case 4:
                    case 5:
                        derecha.insertar(nodo);
                        break;
                }
            }
            medio.setIzquierda(izquierda);
            medio.setDerecha(derecha);
            return medio;
        }

        /**
         *
         * Genera el contenido del archivo fuente para GraphViz
         * @return Un String con el contenido del archivo.
         */
        public String getDot()
        {
            String aux = "digraph lista{ \nnode [shape = record, style=filled];";
            aux += "splines=line; \n";
            getGrafNodos(raiz);
            aux += nodos;
            aux += "}";
            return aux;

        }

        private void getGrafNodos(RamaArbol raiz)
        {
            if (raiz == null)
            {
                return;
            }
            nodos += raiz.getGraphNodo();
            NodoRamaArbol aux = raiz.getPrimero();
            while (aux != null)
            {
                getGrafNodos(aux.getIzquierda());
                aux = aux.getSiguiente();
            }
            aux = raiz.getPrimero();
            while (aux.getSiguiente() != null)
            {
                aux = aux.getSiguiente();
            }
            getGrafNodos(aux.getDerecha());
        }

        public NodoRamaArbol busqueda(int numero)
        {
            if (!estaVacio())
            {
                return busca(numero, raiz);
            }
            else
            {
                return null;
            }
        }

        private NodoRamaArbol busca(int idTransaccion, RamaArbol rama)
        {
            NodoRamaArbol nodo = rama.getPrimero();
            while (nodo != null)
            {

                if (idTransaccion.CompareTo(nodo.getIdTransaccion()) < 0)
                {
                    if (rama.esHoja())
                    {
                        return null;
                    }
                    else
                    {
                        return busca(idTransaccion, nodo.getIzquierda());
                    }
                }
                else if (idTransaccion.CompareTo(nodo.getIdTransaccion()) == 0)
                {
                    return nodo;
                }
                else if (nodo.getSiguiente() == null)
                {
                    if (rama.esHoja())
                    {
                        return null;
                    }
                    else
                    {
                        return busca(idTransaccion, nodo.getDerecha());
                    }
                }
                nodo = nodo.getSiguiente();
            }
            return null;
        }

        private void busca(int idTransaccion, RamaArbol rama, RamaArbol salida)
        {
            if (rama == null)
            {
                return;
            }
            NodoRamaArbol nodo = rama.getPrimero();
            while (nodo != null)
            {
                if (!rama.esHoja())
                {
                    busca(idTransaccion, nodo.getIzquierda(), salida);
                    busca(idTransaccion, nodo.getDerecha(), salida);
                }
                if (idTransaccion.CompareTo(nodo.getIdTransaccion()) == 0)
                {
                    salida.insertar(new NodoRamaArbol(nodo.getIdTransaccion(), nodo.getIdActivo(), nodo.getUsuario(), nodo.getEmpresa(), nodo.getDepartamento(), nodo.getFecha(), nodo.getDuracionRenta()));
                }
                nodo = nodo.getSiguiente();
            }
        }

        public void graficaBBB(ArbolDestinos aB)
        {

            StreamWriter fichero = null;
            try
            {
                fichero = new StreamWriter("arbolBDestino.dot");
                fichero.Write(aB.getDot());
            }
            catch (Exception e) { Console.WriteLine(e.ToString()); }
            finally
            {
                try
                {
                    if (null != fichero)
                        fichero.Close();
                }
                catch (Exception e2) { Console.WriteLine(e2.ToString()); }
            }
            try
            {
                ProcessStartInfo startInfo = new ProcessStartInfo("C:\\Program Files (x86)\\Graphviz\\bin\\dot.exe");
                startInfo.Arguments = "-Tpng  arbolBDestino.dot  -o  arbolBDestino.png ";
                Process.Start(startInfo);
                Process.Start("arbolBDestino.png ");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error en generar archivo dot " + ex.ToString());
            }



        }
    }
}

