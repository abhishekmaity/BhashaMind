package com.bhashamind.api.controller;

import com.bhashamind.api.service.NLPService;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;

// Need DTOs for the test
import com.bhashamind.api.dto.SummarizationRequest;
import com.bhashamind.api.dto.SummarizationResponse;
import com.fasterxml.jackson.databind.ObjectMapper; // For converting DTO to JSON string

// Temporarily reverting to simpler annotation
@WebMvcTest(SummarizationController.class)
public class SummarizationControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private NLPService pythonNLPService;

    @Autowired
    private ObjectMapper objectMapper; // For serializing request DTO

    @Test
    public void testSummarizationEndpoint() throws Exception {
        String inputText = "বাংলাদেশের রাজধানী ঢাকা একটি জনবহুল শহর।";
        String expectedSummary = "ঢাকা বাংলাদেশের রাজধানী।";

        SummarizationRequest requestDto = new SummarizationRequest();
        requestDto.setText(inputText);

        SummarizationResponse mockResponse = new SummarizationResponse();
        mockResponse.setSummary(expectedSummary);

        Mockito.when(pythonNLPService.summarize(Mockito.any(SummarizationRequest.class)))
            .thenReturn(mockResponse);

        mockMvc.perform(post("/api/summarize")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(requestDto))) // Serialize DTO to JSON
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.summary").value(expectedSummary)); // Assumes SummarizationResponse has a 'summary' field
    }
}
