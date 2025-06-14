package com.bhashamind.api.controller;

import com.bhashamind.api.service.ClassificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class ClassificationController {

    @Autowired
    private ClassificationService classificationService;

    @PostMapping("/classify")
    public String classify(@RequestBody String text) {
        return classificationService.classify(text);
    }
}
