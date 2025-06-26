package com.bhashamind.api.controller;

import com.bhashamind.api.dto.SummarizationRequest;
import com.bhashamind.api.dto.SummarizationResponse;
import com.bhashamind.api.service.NLPService;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc; // Added import
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.boot.autoconfigure.data.jpa.JpaRepositoriesAutoConfiguration;
import org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration;
import org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration;
import org.springframework.boot.autoconfigure.security.servlet.SecurityFilterAutoConfiguration;
import org.springframework.boot.autoconfigure.security.oauth2.client.servlet.OAuth2ClientAutoConfiguration;
import org.springframework.boot.autoconfigure.security.oauth2.resource.servlet.OAuth2ResourceServerAutoConfiguration;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration;
import org.springframework.boot.autoconfigure.security.servlet.SecurityFilterAutoConfiguration;
import org.springframework.boot.autoconfigure.security.oauth2.client.servlet.OAuth2ClientAutoConfiguration;
import org.springframework.boot.autoconfigure.security.oauth2.resource.servlet.OAuth2ResourceServerAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.boot.autoconfigure.data.jpa.JpaRepositoriesAutoConfiguration;
import org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;

// Need DTOs for the test
import com.bhashamind.api.dto.SummarizationRequest;
import com.bhashamind.api.dto.SummarizationResponse;
import com.fasterxml.jackson.databind.ObjectMapper; // For converting DTO to JSON string

@WebMvcTest(controllers = SummarizationController.class,
    excludeAutoConfiguration = {
        SecurityAutoConfiguration.class,
        UserDetailsServiceAutoConfiguration.class,
        SecurityFilterAutoConfiguration.class,
        OAuth2ClientAutoConfiguration.class,
        OAuth2ResourceServerAutoConfiguration.class,
        DataSourceAutoConfiguration.class,
        HibernateJpaAutoConfiguration.class,
        JpaRepositoriesAutoConfiguration.class,
        RabbitAutoConfiguration.class
    }
)
// @AutoConfigureMockMvc // secure=false is invalid; @WebMvcTest provides MockMvc
public class SummarizationControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private NLPService pythonNLPService;

    @Autowired
    private ObjectMapper objectMapper;

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
                .content(objectMapper.writeValueAsString(requestDto)))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.summary").value(expectedSummary));
    }
}
