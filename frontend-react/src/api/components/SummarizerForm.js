import React, { useState } from "react";
import { summarizeText } from "../api/apiClient";

export default function SummarizerForm() {
  const [input, setInput] = useState("");
  const [summary, setSummary] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await summarizeText(input);
    setSummary(result);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Bengali Text Summarization</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full p-2 border rounded mb-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter Bengali text..."
        />
        <button className="bg-blue-500 text-white px-4 py-2 rounded" type="submit">
          Summarize
        </button>
      </form>
      {summary && (
        <div className="mt-4">
          <h3 className="font-semibold">Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}
