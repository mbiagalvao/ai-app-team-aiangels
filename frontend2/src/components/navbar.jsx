import React from 'react';
import catIcon from '../assets/kitty.png';

{/*This is the Navbar component that provides navigation
 between different pages of the ChatCAT application.
 It identifies current page and allows users to switch
 between the main chat, quiz, and about pages.*/}

export default function Navbar({ currentPage, setCurrentPage }) {
  return (
    <nav style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      backgroundColor: 'rgba(255, 255, 255, 0.95)',
      borderBottom: '2px solid #f4bf41',
      padding: '1rem 2rem',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      zIndex: 1000,
      backdropFilter: 'blur(10px)'
    }}>
    {/*chatcat logo and title */}
      <div 
        style={{ 
          display: 'flex', 
          alignItems: 'center', 
          gap: '0.5rem',
          cursor: 'pointer'
        }}
        onClick={() => setCurrentPage('main')}
      >
        <img src={catIcon} width={43} height={63} alt="Cat icon" />
        <span style={{ fontSize: '1.7rem', fontWeight: 'bold' }}>ChatCAT</span>
      </div>

      {/*buttons */}
      <div style={{ display: 'flex', gap: '1rem' }}>
        <button
          onClick={() => setCurrentPage('main')}
          style={{
            backgroundColor: currentPage === 'main' ? '#f4bf41' : 'transparent',
            color: currentPage === 'main' ? 'white' : 'black',
            padding: '0.5rem 1rem',
            borderRadius: '0.5rem',
            border: 'none',
            cursor: 'pointer',
            fontWeight: '600',
            transition: 'all 0.2s'
          }}
        >
          ChatCat
        </button>

        <button
          onClick={() => setCurrentPage('quiz')}
          style={{
            backgroundColor: currentPage === 'quiz' ? '#ffa500' : 'transparent',
            color: currentPage === 'quiz' ? 'white' : 'black',
            padding: '0.5rem 1rem',
            borderRadius: '0.5rem',
            border: 'none',
            cursor: 'pointer',
            fontWeight: '600',
            transition: 'all 0.2s'
          }}
        >
          Preparation Quizz
        </button>

        <button
          onClick={() => setCurrentPage('about')}
          style={{
            backgroundColor: currentPage === 'about' ? '#6b7280' : 'transparent',
            color: currentPage === 'about' ? 'white' : 'black',
            padding: '0.5rem 1rem',
            borderRadius: '0.5rem',
            border: 'none',
            cursor: 'pointer',
            fontWeight: '600',
            transition: 'all 0.2s'
          }}
        >
          About us 
        </button>
      </div>
    </nav>
  );
}