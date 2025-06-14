import React, { useState } from "react";
import { classifyText } from "../api/apiClient";

export default function ClassifierForm() {
  const [input, setInput] = useState("");
  const [label, setLabel] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await classifyText(input);
    setLabel(result);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Bengali Text Classification</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full p-2 border rounded mb-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter Bengali text..."
        />
        <button className="bg-green-500 text-white px-4 py-2 rounded" type="submit">
          Classify
        </button>
      </form>
      {label && (
        <div className="mt-4">
          <h3 className="font-semibold">Predicted Label:</h3>
          <p>{label}</p>
        </div>
      )}
    </div>
  );
}
