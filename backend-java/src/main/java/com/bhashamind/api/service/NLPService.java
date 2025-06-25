package com.bhashamind.api.service;

import com.bhashamind.api.dto.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class NLPService {

    private final String pythonBaseUrl = "http://localhost:8000";

    public String getSummary(String text) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        String bodyJson = String.format("{\"text\": \"%s\"}", text.replace("\"", "\\\""));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(pythonBaseUrl + "/api/summarize"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(bodyJson))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            // Extract "summary" from response JSON
            String responseBody = response.body();
            return new JSONObject(responseBody).getString("summary");
        } else {
            throw new RuntimeException("Python backend error: " + response.body());
        }
    }
}
