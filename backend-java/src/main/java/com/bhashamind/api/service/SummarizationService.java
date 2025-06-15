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
 * Service for text summarization.
 */
@Service
public class SummarizationService {

    private static final String FASTAPI_BASE_URL = "http://localhost:8000/summarize";
    private final RestTemplate restTemplate = new RestTemplate();

    /**
     * Retrieves a summary for the given text.
     * @param text The text to summarize.
     * @return The summarized text, or null if summarization fails.
     */
    public String getSummary(String text) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> payload = new HashMap<>();
        payload.put("text", text);

        HttpEntity<Map<String, String>> request = new HttpEntity<>(payload, headers);

        ResponseEntity<Map> response = restTemplate.postForEntity(FASTAPI_BASE_URL, request, Map.class);
        // Assuming the response body is a Map and contains the summary
        if (response.getBody() != null && response.getBody().get("summary") != null) {
            return response.getBody().get("summary").toString();
        }
        return null; // Or throw an exception, or handle error appropriately
    }
}
