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
    @PostMapping("/summarize")
    public String summarize(@RequestBody Map<String, String> request) {
        return service.getSummary(request.get("text"));
    }
}
