package com.example.diego.proyecto1edd;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class Login extends AppCompatActivity {


    Button siguiente;
    EditText name,contra,empre,departamento;
    String nombre,pass,empresa,depto;
    boolean bandera;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        siguiente = (Button) findViewById(R.id.bentrar);
        name = (EditText) findViewById(R.id.edUser);
        contra = (EditText) findViewById(R.id.edPassword);
        empre = (EditText) findViewById(R.id.edEmpresa);
        departamento = (EditText) findViewById(R.id.edDepto);

        siguiente.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                nombre= name.getText().toString();
                pass= contra.getText().toString();
                empresa=empre.getText().toString();
                depto = departamento.getText().toString();
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        TestWebServer test = new TestWebServer();
                        bandera=test.Login(nombre,pass,empresa,depto);
                    }
                }).start();
                bandera=true;
                if (bandera==true){

                    Intent siguiente = new Intent(Login.this,Menu.class);
                    startActivity(siguiente);
                } else {

                    Toast.makeText(Login.this, "Usuario o Contraseña Invalidos", Toast.LENGTH_SHORT).show();
                }


            }
        });
    }


}
