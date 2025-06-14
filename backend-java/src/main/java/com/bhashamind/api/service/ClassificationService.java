package com.bhashamind.api.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;

import java.util.HashMap;
import java.util.Map;

@Service
public class ClassificationService {

    private final String FASTAPI_URL = "http://localhost:8000/classify";
    private final RestTemplate restTemplate = new RestTemplate();

    public String classify(String text) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> payload = new HashMap<>();
        payload.put("text", text);

        HttpEntity<Map<String, String>> request = new HttpEntity<>(payload, headers);

        ResponseEntity<Map> response = restTemplate.postForEntity(FASTAPI_URL, request, Map.class);
        return response.getBody().get("label").toString();
    }
}
