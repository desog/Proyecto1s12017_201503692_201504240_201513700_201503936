using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace ArbolBDestino
{
    static class Program
    {
        /// <summary>
        /// </summary>
        [STAThread]
        static void Main()
        {
            ArbolDestinos aB = new ArbolDestinos();
            aB.insertar("A405",001,"niña","Claro", "Contabilidad","04/03/2015",10);
            aB.insertar("C405", 003, "Cristian", "Tigo", "Pagos", "03/03/2015", 20);
            aB.insertar("B405", 002, "Elmer", "Movistar", "Bodega", "02/03/2015", 30);
            aB.insertar("F405", 005, "Javier", "Telcel", "Gerencia", "05/03/2015", 40);
            aB.insertar("D405", 004, "Diana", "Comcel", "Administracion", "04/03/2015", 50);
            graficaB(aB);


        }


        static void graficaB(ArbolDestinos aB)
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
                Console.WriteLine("Error en generar archivo dot "+ex.ToString());
            }




                       
    }
    }
}
