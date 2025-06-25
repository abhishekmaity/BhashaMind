@WebMvcTest(SummarizationController.class)
public class SummarizationControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private NLPService pythonNLPService;

    @Test
    public void testSummarizationEndpoint() throws Exception {
        String inputText = "বাংলাদেশের রাজধানী ঢাকা একটি জনবহুল শহর।";
        String expectedSummary = "ঢাকা বাংলাদেশের রাজধানী।";

        Mockito.when(pythonNLPService.getSummary(Mockito.anyString()))
            .thenReturn(expectedSummary);

        mockMvc.perform(post("/api/summarize")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"text\": \"" + inputText + "\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.summary").value(expectedSummary));
    }
}
