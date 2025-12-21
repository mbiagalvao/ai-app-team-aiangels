import React, { useState } from 'react';
import Navbar from './components/navbar';
import Main from './pages/main';
import Quiz from './pages/quiz';
import About from './pages/about';

export default function App() {
  const [currentPage, setCurrentPage] = useState('main');

  const renderPage = () => {
    switch(currentPage) {
      case 'main':
        return <Main />;
      case 'quiz':
        return <Quiz onBack={() => setCurrentPage('main')} />;
      case 'about':
        return <About />;
      default:
        return <Main />;
    }
  };

  return (
    <div>
      <Navbar currentPage={currentPage} setCurrentPage={setCurrentPage} />
      {renderPage()}
    </div>
  );
}