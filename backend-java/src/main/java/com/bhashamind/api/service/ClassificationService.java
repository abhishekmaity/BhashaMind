package com.bhashamind.api.service;

import java.util.HashMap;
import java.util.Map;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

/**
 * Service for text classification.
 */
@Service
public class ClassificationService {

    private static final String FASTAPI_BASE_URL = "http://localhost:8000/classify";
    private final RestTemplate restTemplate = new RestTemplate();

    /**
     * Classifies the given text.
     * @param text The text to classify.
     * @return The classification label, or null if classification fails.
     */
    public String classify(String text) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> payload = new HashMap<>();
        payload.put("text", text);

        HttpEntity<Map<String, String>> request = new HttpEntity<>(payload, headers);

        ResponseEntity<Map> response = restTemplate.postForEntity(FASTAPI_BASE_URL, request, Map.class);
        // Assuming the response body is a Map and contains the label
        if (response.getBody() != null && response.getBody().get("label") != null) {
            return response.getBody().get("label").toString();
        }
        return null; // Or throw an exception, or handle error appropriately
    }
}
