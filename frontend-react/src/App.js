import React from 'react';
import Summarizer from './components/Summarizer';
import Classifier from './components/Classifier';

function App() {
  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4 text-center">🧠 BhashaMind</h1>
      <div className="grid gap-6 md:grid-cols-2">
        <Summarizer />
        <Classifier />
      </div>
    </div>
  );
}

export default App;
