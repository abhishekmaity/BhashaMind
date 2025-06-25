import React, { useState } from 'react';

function Classifier() {
  const [text, setText] = useState('');
  const [label, setLabel] = useState('');

  const handleClassify = async () => {
    try {
      const res = await fetch("http://localhost:8080/api/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      setLabel(data.label || data.error);
    } catch (err) {
      setLabel("Error connecting to server");
    }
  };

  return (
    <div className="p-4 border rounded-lg shadow-md">
      <h2 className="text-xl font-semibold mb-2">📌 Bengali Classification</h2>
      <textarea
        className="w-full p-2 border"
        rows="5"
        placeholder="বাংলা লেখাটি এখানে লিখুন..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleClassify} className="mt-2 bg-green-600 text-white px-4 py-2 rounded">
        Classify
      </button>
      {label && (
        <div className="mt-3 p-3 bg-gray-100 border rounded">Predicted Label: {label}</div>
      )}
    </div>
  );
}

export default Classifier;
