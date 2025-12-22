import React, { useState } from 'react';
import Navbar from './components/navbar';
import Main from './pages/main';
import Quiz from './pages/quiz';
import About from './pages/about';
import Login from './pages/login';

export default function App() {
  const [currentPage, setCurrentPage] = useState('main');
  const [user, setUser] = useState(null);

  const handleLogin = (userData) => {
    setUser(userData);
    setCurrentPage('main');
  };

  const renderPage = () => {
    switch(currentPage) {
      case 'main':
        return <Main onNavigate={setCurrentPage} user={user} />;
      case 'quiz':
        return <Quiz onBack={() => setCurrentPage('main')} />;
      case 'about':
        return <About />;
      case 'login':
        return <Login onBack={() => setCurrentPage('main')} onLogin={handleLogin} />;
      default:  
        return <Main onNavigate={setCurrentPage} />;
    }
  };

  return (
    <div>
      <Navbar currentPage={currentPage} setCurrentPage={setCurrentPage} user={user} />
      {renderPage()}
    </div>
  );
}