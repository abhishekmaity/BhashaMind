package com.bhashamind.api.controller;

import com.bhashamind.api.dto.*;
import com.bhashamind.api.service.NLPService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException; // For catch block
import java.util.Map;     // For error response body

@RestController
@RequestMapping("/api")
public class NLPController {

    private final NLPService nlpService;

    public NLPController(NLPService nlpService) {
        this.nlpService = nlpService;
    }

    @PostMapping("/summarize")
    public ResponseEntity<?> summarize(@RequestBody SummarizationRequest request) {
        try {
            SummarizationResponse response = nlpService.summarize(request);
            return ResponseEntity.ok(response);
        } catch (IOException | InterruptedException e) {
            // Log the exception server-side (optional, good practice)
            // e.printStackTrace();
            Thread.currentThread().interrupt(); // Restore interrupted status if InterruptedException
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                 .body(Map.of("error", "Error processing summarization request: " + e.getMessage()));
        }
    }

    @PostMapping("/classify")
    public ResponseEntity<?> classify(@RequestBody ClassificationRequest request) {
        try {
            ClassificationResponse response = nlpService.classify(request);
            return ResponseEntity.ok(response);
        } catch (IOException | InterruptedException e) {
            // Log the exception server-side (optional, good practice)
            // e.printStackTrace();
            Thread.currentThread().interrupt(); // Restore interrupted status if InterruptedException
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                 .body(Map.of("error", "Error processing classification request: " + e.getMessage()));
        }
    }
}
