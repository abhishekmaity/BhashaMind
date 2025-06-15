package com.bhashamind.api.controller;

import com.bhashamind.api.service.ClassificationService;
import java.util.Map;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller for handling text classification requests.
 */
@RestController
@RequestMapping("/api")
public class ClassificationController {

    @Autowired
    private ClassificationService service;

    /**
     * Endpoint to classify text.
     * @param request A map containing the text to classify under the key "text".
     * @return The classification label.
     */
    @PostMapping("/classify")
    public String classify(@RequestBody Map<String, String> request) {
        return service.classify(request.get("text"));
    }
}
