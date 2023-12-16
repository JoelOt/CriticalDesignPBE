package com.example.cdr;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;


import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.Iterator;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class CourseManager extends AppCompatActivity {
    private Button login;
    private Button logout;
    private Button send;
    private TextView path;
    private TableLayout tableLayout;
    private boolean is_inici;
    OkHttpClient client = new OkHttpClient();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        inici();
        //taules("");
    }
    private void inici(){
        is_inici = true;
        setContentView(R.layout.inici);
        login = (Button) findViewById(R.id.login);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                path = (TextView) findViewById(R.id.pathText);
                TextView username = (TextView) findViewById(R.id.usernameText);
                TextView uid = (TextView) findViewById(R.id.uidText);
                String url = "http://10.0.2.2/index.php/students?uid=938B506&userName=Ariadna_Marcos";
                //url = path.getText() + "/index.php/students?uid=" + uid.getText() + "&userName=" + username.getText();
                if(path != null ){
                    get(url);
                }
            }
        });
    }
    private void taules(String username){
        is_inici = false;
        setContentView(R.layout.taules);
        TextView welcomeText = (TextView) findViewById(R.id.welcomeText);
        welcomeText.setText("Welcome "+ username);
        tableLayout = findViewById(R.id.taula);
        logout = (Button) findViewById(R.id.logout);
        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setContentView(R.layout.inici);
            }
        });
        send = (Button) findViewById(R.id.send);
        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                TextView consulta = (TextView) findViewById(R.id.consultaText);
                String url = path.getText()+ "/" + consulta.getText();
                get(url);
            }
        });
    }

    public void get(String url){
        Request request = new Request.Builder().url(url).build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                e.printStackTrace();
            }
            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
                if (response.isSuccessful()){
                        String responseBody = response.body().string();
                        if(is_inici){
                            updatelog(responseBody);
                        }else{
                            updatetaula(responseBody);
                        }
                }
            }
        });
    }

    public void updatetaula(String responseBody){
        // Clear existing rows from the table
        tableLayout.removeAllViews();
        try {
            JSONArray jsonArray = new JSONArray(responseBody);

            // Create the header row based on keys in the first JSON object
            if (jsonArray.length() > 0) {
                JSONObject firstObject = jsonArray.getJSONObject(0);
                createHeaderRow(firstObject.keys());
            }

            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject jsonObject = jsonArray.getJSONObject(i);

                // Create a new row
                TableRow row = new TableRow(this);

                // Iterate over the keys and create TextViews for each key-value pair
                Iterator<String> keys = jsonObject.keys();
                while (keys.hasNext()) {
                    String key = keys.next();
                    String value = jsonObject.getString(key);

                    // Create TextViews for each column
                    TextView textView = createTextView(value);

                    // Add TextView to the row
                    row.addView(textView);
                }

                // Add the row to the table
                tableLayout.addView(row);
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    private void createHeaderRow(Iterator<String> keys) {
        TableRow headerRow = new TableRow(this);

        while (keys.hasNext()) {
            String key = keys.next();
            TextView headerTextView = createTextView(key);
            headerTextView.setTypeface(null, android.graphics.Typeface.BOLD);

            // Add header TextView to the header row
            headerRow.addView(headerTextView);
        }

        // Add the header row to the table
        tableLayout.addView(headerRow);
    }

    private TextView createTextView(String text) {
        TextView textView = new TextView(this);
        textView.setText(text);
        textView.setPadding(16, 8, 16, 8);
        return textView;
    }

    public void updatelog(String responseBody){
        try {
            if (!responseBody.isEmpty()) {
                // Parse the single JSON object
                JSONObject jsonObject = new JSONObject(responseBody);
                String userName = jsonObject.getString("userName");
                taules(userName);
            }
        }catch(JSONException e){
            e.printStackTrace();
        }
    }
}
