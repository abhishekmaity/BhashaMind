import React from "react";
import SummarizerForm from "./components/SummarizerForm";
import ClassifierForm from "./components/ClassifierForm";

function App() {
  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4 text-center">BhashaMind</h1>
      <SummarizerForm />
      <hr className="my-6" />
      <ClassifierForm />
    </div>
  );
}

export default App;
