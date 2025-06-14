import React from 'react';
import Summarizer from './components/Summarizer';
import Classifier from './components/Classifier';

function App() {
  return (
    <div className="max-w-4xl mx-auto p-6 font-sans">
      <h1 className="text-3xl font-extrabold mb-4 text-center">🧠 BhashaMind Frontend</h1>
      <Summarizer />
      <Classifier />
    </div>
  );
}

export default App;
