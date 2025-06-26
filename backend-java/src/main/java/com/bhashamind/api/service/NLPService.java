package com.bhashamind.api.service;

import com.bhashamind.api.dto.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import org.json.JSONObject;

@Service
public class NLPService {

    private final String pythonBaseUrl = "http://localhost:8000"; // TODO: Make configurable

    public SummarizationResponse summarize(SummarizationRequest summarizationRequest) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        String text = summarizationRequest.getText();
        String bodyJson = String.format("{\"text\": \"%s\"}", text.replace("\"", "\\\""));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(pythonBaseUrl + "/api/summarize"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(bodyJson))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            String responseBody = response.body();
            String summaryText = new JSONObject(responseBody).getString("summary");
            SummarizationResponse sr = new SummarizationResponse();
            sr.setSummary(summaryText);
            return sr;
        } else {
            // Consider creating a custom exception
            throw new RuntimeException("Python backend summarization error: " + response.statusCode() + " " + response.body());
        }
    }

    public ClassificationResponse classify(ClassificationRequest classificationRequest) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        String text = classificationRequest.getText();
        String bodyJson = String.format("{\"text\": \"%s\"}", text.replace("\"", "\\\""));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(pythonBaseUrl + "/api/classify")) // Assuming this is the Python classification endpoint
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(bodyJson))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            String responseBody = response.body();
            // Assuming Python service returns a JSON like {"label": "some_label"}
            String labelText = new JSONObject(responseBody).getString("label");
            ClassificationResponse cr = new ClassificationResponse();
            cr.setLabel(labelText);
            return cr;
        } else {
            // Consider creating a custom exception
            throw new RuntimeException("Python backend classification error: " + response.statusCode() + " " + response.body());
        }
    }
}
