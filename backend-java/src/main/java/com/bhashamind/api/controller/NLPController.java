package com.bhashamind.api.controller;

import com.bhashamind.api.dto.*;
import com.bhashamind.api.service.NLPService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class NLPController {

    private final NLPService nlpService;

    public NLPController(NLPService nlpService) {
        this.nlpService = nlpService;
    }

    @PostMapping("/summarize")
    public SummarizationResponse summarize(@RequestBody SummarizationRequest request) {
        return nlpService.summarize(request);
    }

    @PostMapping("/classify")
    public ClassificationResponse classify(@RequestBody ClassificationRequest request) {
        return nlpService.classify(request);
    }
}
