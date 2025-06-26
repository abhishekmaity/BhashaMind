package com.bhashamind.api.controller;

import com.bhashamind.api.service.SummarizationService;
import com.bhashamind.api.service.NLPService; // Added import for NLPService
import com.bhashamind.api.dto.SummarizationRequest; // Added import for DTO
import com.bhashamind.api.dto.SummarizationResponse; // Added import for DTO
import java.util.Map;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller for handling text summarization requests.
 */
@RestController
@RequestMapping("/api")
public class SummarizationController {

    @Autowired
    private SummarizationService service;

    /**
     * Endpoint to summarize text.
     * @param request A map containing the text to summarize under the key "text".
     * @return The summarized text.
     */
    @Autowired
    private NLPService pythonNLPService;

    @PostMapping("/summarize")
    public ResponseEntity<?> summarize(@RequestBody SummarizationRequest requestDto) { // Changed to DTO and wildcard response
        try {
            String text = requestDto.getText();
            if (text == null || text.trim().isEmpty() || text.length() < 10) { // Added trim and isEmpty check
                // Returning a Map for error, consistent with original error structure
                return ResponseEntity.badRequest().body(Map.of("error", "Input text too short for summarization."));
            }
            SummarizationResponse summaryResponse = pythonNLPService.summarize(requestDto);
            return ResponseEntity.ok(summaryResponse);
        } catch (Exception e) {
            // Returning a Map for error, consistent with original error structure
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(Map.of("error", "Summarization failed: " + e.getMessage()));
        }
    }
}
