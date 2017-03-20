package com.example.diego.proyecto1edd;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class Menu extends AppCompatActivity {
    Button siguientes;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);


        siguientes = (Button) findViewById(R.id.btrentar);
        siguientes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent siguientea = new Intent(Menu.this,Renta.class);
                startActivity(siguientea);

            }
        });
    }
}
