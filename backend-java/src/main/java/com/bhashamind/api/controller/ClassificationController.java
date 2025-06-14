package com.bhashamind.api.controller;

import com.bhashamind.api.service.ClassificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class ClassificationController {

    @Autowired
    private ClassificationService service;

    @PostMapping("/classify")
    public String classify(@RequestBody Map<String, String> request) {
        return service.classify(request.get("text"));
    }
}
