package com.example.productapp;

import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    DatabaseHelper myDb;
    EditText editProductName, editQuantity, editPrice;
    Button btnAddProduct, btnViewProducts;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        myDb = new DatabaseHelper(this);

        editProductName = findViewById(R.id.editText_productName);
        editQuantity = findViewById(R.id.editText_quantity);
        editPrice = findViewById(R.id.editText_price);
        btnAddProduct = findViewById(R.id.button_add);
        btnViewProducts = findViewById(R.id.button_view);

        addProduct();
        viewAllProducts();
    }

    public void addProduct() {
        btnAddProduct.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean isInserted = myDb.insertData(editProductName.getText().toString(), 
                        editQuantity.getText().toString(), 
                        editPrice.getText().toString());
                if (isInserted) {
                    Toast.makeText(MainActivity.this, "Produto Inserido", Toast.LENGTH_LONG).show();
                } else {
                    Toast.makeText(MainActivity.this, "Erro ao Inserir Produto", Toast.LENGTH_LONG).show();
                }
            }
        });
    }

    public void viewAllProducts() {
        btnViewProducts.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Cursor res = myDb.getAllData();
                if (res.getCount() == 0) {
                    showMessage("Erro", "Nenhum Produto Encontrado");
                    return;
                }

                StringBuilder buffer = new StringBuilder();
                while (res.moveToNext()) {
                    buffer.append("ID: ").append(res.getString(0)).append("\n");
                    buffer.append("Nome: ").append(res.getString(1)).append("\n");
                    buffer.append("Quantidade: ").append(res.getString(2)).append("\n");
                    buffer.append("Preço: ").append(res.getString(3)).append("\n\n");
                }

                showMessage("Lista de Produtos", buffer.toString());
            }
        });
    }

    public void showMessage(String title, String message) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setTitle(title);
        builder.setMessage(message);
        builder.show();
    }
}
