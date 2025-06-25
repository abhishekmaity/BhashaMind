import React from "react";

const ResultBox = ({ summary, category }) => (
  <div className="mt-6 bg-gray-50 p-4 border rounded-lg">
    {summary && (
      <div className="mb-2">
        <strong>📝 Summary:</strong>
        <p className="mt-1 text-gray-700">{summary}</p>
      </div>
    )}
    {category && (
      <div>
        <strong>📂 Category:</strong>
        <p className="mt-1 text-gray-700">{category}</p>
      </div>
    )}
  </div>
);

export default ResultBox;
