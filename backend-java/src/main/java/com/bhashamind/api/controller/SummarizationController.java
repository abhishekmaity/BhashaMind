package com.bhashamind.api.controller;

import com.bhashamind.api.service.SummarizationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class SummarizationController {

    @Autowired
    private SummarizationService service;

    @PostMapping("/summarize")
    public String summarize(@RequestBody Map<String, String> request) {
        return service.getSummary(request.get("text"));
    }
}
