package com.bhashamind.api.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class SummarizationService {

    private final RestTemplate restTemplate = new RestTemplate();
    private final String PYTHON_BACKEND_URL = "http://localhost:8000/summarize";

    public String summarize(String text) {
        return restTemplate.postForObject(PYTHON_BACKEND_URL, text, String.class);
    }
}
