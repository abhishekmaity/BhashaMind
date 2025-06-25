import React, { useState } from "react";
import axios from "axios";
import ResultBox from "./components/ResultBox";

function App() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [category, setCategory] = useState("");

  const handleSummarize = async () => {
    const res = await axios.post("/api/summarize", { text });
    setSummary(res.data.summary);
  };

  const handleClassify = async () => {
    const res = await axios.post("/api/classify", { text });
    setCategory(res.data.label);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-2xl mx-auto bg-white p-6 rounded-xl shadow-md">
        <h1 className="text-2xl font-bold mb-4 text-center">BhashaMind UI</h1>
        <textarea
          className="w-full p-3 border rounded"
          rows={6}
          placeholder="বাংলা টেক্সট দিন..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <div className="flex justify-between mt-4 gap-2">
          <button className="btn bg-blue-600 text-white" onClick={handleSummarize}>
            🔄 Summarize
          </button>
          <button className="btn bg-green-600 text-white" onClick={handleClassify}>
            🧠 Classify
          </button>
        </div>

        {(summary || category) && (
          <ResultBox summary={summary} category={category} />
        )}
      </div>
    </div>
  );
}

export default App;
