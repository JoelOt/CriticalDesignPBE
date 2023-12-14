package com.example.cdr;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class IniciCourseManager extends AppCompatActivity {
    private Button button;
    private TextView path;
    private TextView username;
    private TextView uid;
    private TextView text;
    OkHttpClient client = new OkHttpClient();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.inici);
        button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                path = (TextView) findViewById(R.id.pathText);
                username = (TextView) findViewById(R.id.usernameText);
                uid = (TextView) findViewById(R.id.uidPasswordText);
                text = (TextView) findViewById(R.id.WelcomeText);
                //String url = path + "/students?uid=" + uid + "&userName=" + username;
                String url = "http://localhost/index.php/students?uid=938B506&userName=Ariadna_Marcos";
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
                    try {
                        String responseBody = response.body().string();
                        if (!responseBody.isEmpty()) {
                            // Parse the single JSON object
                            JSONObject jsonObject = new JSONObject(responseBody);

                            // Access individual fields
                            String uid = jsonObject.getString("uid");
                            String userName = jsonObject.getString("userName");
                            String a = "UID: " + uid + ", UserName: " + userName;
                            text.setText(a);
                        }
                    }catch(JSONException e){
                        e.printStackTrace();
                    }

                }
            }
        });
    }
}
