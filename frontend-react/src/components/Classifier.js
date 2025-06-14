import React, { useState } from 'react';
import axios from 'axios';

export default function Classifier() {
  const [text, setText] = useState('');
  const [label, setLabel] = useState('');

  const handleClassify = async () => {
    const res = await axios.post('http://localhost:8000/api/classify', { text });
    setLabel(res.data.label);
  };

  return (
    <div className="p-4 border rounded shadow-lg mt-8">
      <h2 className="text-xl font-bold mb-2">Bengali Classification</h2>
      <textarea value={text} onChange={e => setText(e.target.value)} className="w-full p-2 border rounded" rows="5" placeholder="Enter Bengali text..." />
      <button onClick={handleClassify} className="mt-2 px-4 py-2 bg-green-600 text-white rounded">Classify</button>
      {label && <p className="mt-4 bg-gray-100 p-3 rounded">Predicted Label: <strong>{label}</strong></p>}
    </div>
  );
}
