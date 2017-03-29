using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ArbolBDestino
{
    public class NodoRamaArbol
    {
        private readonly IComparable idTransaccion;
        private int idActivo;
        private string usuario;
        private string empresa;
        private string departamento;
        private string fecha;
        private int duracionRenta;
        private NodoRamaArbol anterior, siguiente;
        private RamaArbol derecha, izquierda;

        public NodoRamaArbol(IComparable idTransaccion, int idActivo, string usuario, string empresa, string departamento, string fecha, int duracionRenta)
        {
            this.idTransaccion = idTransaccion;
            this.idActivo = idActivo;
            this.usuario = usuario;
            this.empresa = empresa;
            this.departamento = departamento;
            this.fecha = fecha;
            this.duracionRenta = duracionRenta;
        }


        public IComparable getIdTransaccion()
        {
            return idTransaccion;
        }

        
        public int getIdActivo()
        {
            return idActivo;
        }

        public void setIdActivo(int idActivo)
        {
            this.idActivo = idActivo;
        }

        public string getUsuario()
        {
            return usuario;
        }

        public void setUsuario(string usuario)
        {
            this.usuario=usuario;
        }

        public string getEmpresa()
        {
            return empresa;
        }

        public void setEmpresa(string empresa)
        {
            this.empresa = empresa;
        }

        public string getDepartamento()
        {
            return departamento;
        }

        public void setDepartamento(string departamento)
        {
            this.departamento = departamento;
        }

        public string getFecha()
        {
            return fecha;
        }

        public void setFecha(string fecha)
        {
            this.fecha = fecha;
        }

        public int getDuracionRenta()
        {
            return duracionRenta;
        }

        public void setDuracionRenta(int duracionRenta)
        {
            this.duracionRenta = duracionRenta;
        }

        /**
         *
         * @return
         */
        public NodoRamaArbol getAnterior()
        {
            return anterior;
        }

        /**
         *
         * @param anterior
         */
        public void setAnterior(NodoRamaArbol anterior)
        {
            this.anterior = anterior;
        }

        /**
         *
         * @return
         */
        public NodoRamaArbol getSiguiente()
        {
            return siguiente;
        }

        /**
         *
         * @param siguiente
         */
        public void setSiguiente(NodoRamaArbol siguiente)
        {
            this.siguiente = siguiente;
        }

        /**
         *
         * @return
         */
        public RamaArbol getDerecha()
        {
            return derecha;
        }

        /**
         *
         * @param derecha
         */
        public void setDerecha(RamaArbol derecha)
        {
            this.derecha = derecha;
        }

        /**
         *
         * @return
         */
        public RamaArbol getIzquierda()
        {
            return izquierda;
        }

        /**
         *
         * @param izquierda
         */
        public void setIzquierda(RamaArbol izquierda)
        {
            this.izquierda = izquierda;
        }

    }

}
