using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;
using System.IO;
using System.Diagnostics;
using ArbolBDestino;

/// <summary>
/// Descripción breve de WebServiceProyecto_EDD_
/// </summary>
[WebService(Namespace = "http://Proyecto1_EDD_Grupo16.org/")]
[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
// Para permitir que se llame a este servicio web desde un script, usando ASP.NET AJAX, quite la marca de comentario de la línea siguiente. 
// [System.Web.Script.Services.ScriptService]
public class WebServiceProyecto_EDD_ : System.Web.Services.WebService
{
    static ArbolDestinos a;
    public WebServiceProyecto_EDD_()
    {
        //Elimine la marca de comentario de la línea siguiente si utiliza los componentes diseñados 
        //InitializeComponent(); 
    }

    [WebMethod(EnableSession = true)]
    public string Insertar(int idTransaccion, int idActivo, string usuario, string empresa, string departamento, string fecha, int duracionRenta)
    {
        a.insertar(idTransaccion, idActivo, usuario, empresa, departamento, fecha, duracionRenta);
        //graficaB(a);
        return "si se pudo";
    }

    [WebMethod(EnableSession = true)]
    public void inicializar()
    {
        a = new ArbolDestinos();
    }
    [WebMethod(EnableSession = true)]
    public void graficar()
    {
        graficaB(a);
    }

    [WebMethod]
    public void graficaB(ArbolBDestino.ArbolDestinos aB)
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
