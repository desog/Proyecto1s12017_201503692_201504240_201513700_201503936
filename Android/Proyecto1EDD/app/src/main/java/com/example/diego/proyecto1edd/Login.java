package com.example.diego.proyecto1edd;

import android.content.Intent;
import android.os.Looper;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;


public class Login extends AppCompatActivity {


    Button siguiente;
    EditText name,contra,empre,departamento;
    String nombre,pass,empresa,depto,bandera;
    TextView texto;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        siguiente = (Button) findViewById(R.id.bentrar);
        name = (EditText) findViewById(R.id.edUser);
        contra = (EditText) findViewById(R.id.edPassword);
        empre = (EditText) findViewById(R.id.edEmpresa);
        departamento = (EditText) findViewById(R.id.edDepto);
        texto = (TextView) findViewById(R.id.tvlog);

        siguiente.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                nombre= name.getText().toString();
                pass= contra.getText().toString();
                empresa=empre.getText().toString();
                depto = departamento.getText().toString();


                new Thread (new Runnable() {
                    @Override
                    public void run() {
                        try{
                        TestWebServer test = new TestWebServer();
                        bandera=test.Login(nombre,pass,empresa,depto);

                        if (bandera.equals("SI")){

                            Intent siguiente = new Intent(Login.this,Menu.class);
                            startActivity(siguiente);
                        } else {
                            texto.setText("Incorrecto");

                        }} catch (Exception e){


                        }
                    }
                }).start();




            }
        });
    }





}
