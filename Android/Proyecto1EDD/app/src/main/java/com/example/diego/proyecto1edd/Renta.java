package com.example.diego.proyecto1edd;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

import java.util.LinkedList;

public class Renta extends AppCompatActivity {
    Spinner ids;
    Button boton;
    String bandera;
    String[] identificadores;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_renta);
        ids = (Spinner) findViewById(R.id.spidProducto);
        boton = (Button) findViewById(R.id.btrentar);
        boton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View view) {
                new Thread (new Runnable() {
                    @Override
                    public void run() {
                        try{
                            TestWebServer test = new TestWebServer();
                            bandera=test.idproductos();


                            identificadores=bandera.split(",");
                            System.out.print("HOA");
                        } catch (Exception e){


                        }
                    }
                }).start();
            }
        });

    }
}
