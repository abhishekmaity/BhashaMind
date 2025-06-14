import React, { useState } from 'react';
import axios from 'axios';

export default function Summarizer() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');

  const handleSummarize = async () => {
    const res = await axios.post('http://localhost:8000/api/summarize', { text });
    setSummary(res.data.summary);
  };

  return (
    <div className="p-4 border rounded shadow-lg">
      <h2 className="text-xl font-bold mb-2">Bengali Summarization</h2>
      <textarea value={text} onChange={e => setText(e.target.value)} className="w-full p-2 border rounded" rows="5" placeholder="Enter Bengali text..." />
      <button onClick={handleSummarize} className="mt-2 px-4 py-2 bg-blue-600 text-white rounded">Summarize</button>
      {summary && <p className="mt-4 bg-gray-100 p-3 rounded">{summary}</p>}
    </div>
  );
}
