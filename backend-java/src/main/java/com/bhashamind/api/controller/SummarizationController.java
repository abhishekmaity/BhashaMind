package com.bhashamind.api.controller;

import com.bhashamind.api.service.SummarizationService;
import java.util.Map;
import org.springframework.beans.factory.annotation.Autowired;
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
    private PythonNLPService pythonNLPService;

    @PostMapping("/summarize")
    public ResponseEntity<Map<String, Object>> summarize(@RequestBody Map<String, String> request) {
        try {
            String text = request.get("text");
            if (text == null || text.length() < 10) {
                return ResponseEntity.badRequest().body(Map.of("error", "Text too short for summarization"));
            }
            String summary = pythonNLPService.getSummary(text);
            return ResponseEntity.ok(Map.of("summary", summary));
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(Map.of("error", "Summarization failed: " + e.getMessage()));
        }
    }
}
