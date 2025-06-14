const BASE_URL = "http://localhost:8080/api";

export async function summarizeText(text) {
  const response = await fetch(`${BASE_URL}/summarize`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(text),
  });
  return response.text();
}

export async function classifyText(text) {
  const response = await fetch(`${BASE_URL}/classify`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(text),
  });
  return response.text();
}
