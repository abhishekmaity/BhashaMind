import React, { useState } from 'react';

function Summarizer() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');

  const handleSummarize = async () => {
    try {
      const res = await fetch("http://localhost:8080/api/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      setSummary(data.summary || data.error);
    } catch (err) {
      setSummary("Error connecting to server");
    }
  };

  return (
    <div className="p-4 border rounded-lg shadow-md">
      <h2 className="text-xl font-semibold mb-2">📌 Bengali Summarization</h2>
      <textarea
        className="w-full p-2 border"
        rows="5"
        placeholder="বাংলা লেখাটি এখানে লিখুন..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleSummarize} className="mt-2 bg-blue-600 text-white px-4 py-2 rounded">
        Summarize
      </button>
      {summary && (
        <div className="mt-3 p-3 bg-gray-100 border rounded">{summary}</div>
      )}
    </div>
  );
}

export default Summarizer;
