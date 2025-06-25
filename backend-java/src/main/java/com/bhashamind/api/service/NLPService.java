package com.bhashamind.api.service;

import com.bhashamind.api.dto.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class NLPService {

    @Value("${backend.python.url:http://backend-python:8000}")
    private String pythonBaseUrl;

    private final RestTemplate restTemplate = new RestTemplate();

    public SummarizationResponse summarize(SummarizationRequest request) {
        return restTemplate.postForObject(
            pythonBaseUrl + "/summarize",
            request,
            SummarizationResponse.class
        );
    }

    public ClassificationResponse classify(ClassificationRequest request) {
        return restTemplate.postForObject(
            pythonBaseUrl + "/classify",
            request,
            ClassificationResponse.class
        );
    }
}
