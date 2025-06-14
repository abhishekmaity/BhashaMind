package com.bhashamind.api.controller;

import com.bhashamind.api.service.SummarizationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class SummarizationController {

    @Autowired
    private SummarizationService summarizationService;

    @PostMapping("/summarize")
    public String summarize(@RequestBody String text) {
        return summarizationService.summarize(text);
    }
}
