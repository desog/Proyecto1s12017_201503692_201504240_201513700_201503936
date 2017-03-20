package com.example.diego.proyecto1edd;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Diego
 */
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
public class TestWebServer {
     public static OkHttpClient webClient = new OkHttpClient();



    public  boolean Login(String dato,String pass,String empresa,String depto){
        RequestBody Cuerpo = new FormEncodingBuilder()
                .add("dato", dato)
                .add("dato1",pass)
                .add("dato2",empresa)
                .add("dato3",depto)

                .build();
        String r = getString("metodoWeb", Cuerpo);
        if (r=="HECHO"){
            return true;

        } else {
            return false;
        }


    }





    
    
 
     public  String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.168.0.100:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(com.example.diego.proyecto1edd.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(com.example.diego.proyecto1edd.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

}
