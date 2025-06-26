package com.bhashamind.api.controller;

import com.bhashamind.api.service.ClassificationService;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(controllers = ClassificationController.class,
    properties = {
        "spring.autoconfigure.exclude=" +
            "org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration," +
            "org.springframework.boot.autoconfigure.security.servlet.UserDetailsServiceAutoConfiguration," +
            "org.springframework.boot.autoconfigure.security.servlet.SecurityFilterAutoConfiguration," +
            "org.springframework.boot.autoconfigure.security.oauth2.client.servlet.OAuth2ClientAutoConfiguration," +
            "org.springframework.boot.autoconfigure.security.oauth2.resource.servlet.OAuth2ResourceServerAutoConfiguration," +
            "org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration," +
            "org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration," +
            "org.springframework.boot.autoconfigure.data.jpa.JpaRepositoriesAutoConfiguration," +
            "org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration"
    }
)
public class ClassificationControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ClassificationService classificationService;

    @Test
    public void testClassificationEndpointSuccess() throws Exception {
        String inputText = "বিশ্বব্যাপী অর্থনৈতিক প্রবৃদ্ধি ধীর হয়েছে।";
        String expectedLabel = "economy";

        // Mock the classify method of ClassificationService
        Mockito.when(classificationService.classify(Mockito.anyString()))
                .thenReturn(expectedLabel);

        mockMvc.perform(post("/api/classify")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"text\": \"" + inputText + "\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.label").value(expectedLabel));
    }

    @Test
    public void testClassificationErrorShortInput() throws Exception {
        mockMvc.perform(post("/api/classify")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"text\": \"hi\"}"))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.error").exists());
    }
}
