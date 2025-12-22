import React, { useState, useRef, useEffect } from 'react';
import backgroundImage from '../assets/wallpaper.png';
import serImage from '../assets/user.png';

{/*This is the Main chat page component that allows users to interact
 with the ChatCAT AI assistant. It handles user input, displays chat messages,
 and manages the conversation state.*/}


export default function Main({ onNavigate, user }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);  
  
  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = input;
    setMessages(prev => [...prev, { type: 'user', text: userMsg }]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMsg })
      });

      const data = await response.json();
      setMessages(prev => [...prev, { type: 'bot', text: data.response }]);
    } catch (error) {
      setMessages(prev => [...prev, { type: 'bot', text: 'Cat is not working right now' }]);
    }
    
    setLoading(false);
  };
  { /*main container*/}
  return ( 
    <div 
      style={{ 
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        margin: 0,
        padding: 0
      }}
    >
      <div style={{
        display: 'flex', 
        flexDirection: 'column', 
        height: '100%', 
        width: '100%', 
        maxWidth: '64rem',
        margin: '0 auto',
        padding: '1rem', 
        justifyContent: 'flex-start',
        paddingTop: '7rem'
      }}>
                
        {/*messages container*/}
        <div style={{ 
          display: 'flex',
          justifyContent: 'center',
          marginBottom: '20px', 
          width: '100%'
        }}>
          <div 
            style={{ 
              height: '300px',
              width: '100%', 
              maxWidth: '700px', 
              backgroundColor: 'white', 
              borderRadius: '24px', 
              border: '2px solid #f4bf41',
              overflowY: 'auto',
              overflowX: 'hidden',
              padding: '15px',
              paddingTop: '80px'
            }}
          >
            {messages.map((msg, i) => (
              <div 
                key={i}
                style={{ 
                  marginBottom: '12px',
                  textAlign: msg.type === 'user' ? 'right' : 'left'  
                }}
              >
                <div 
                  style={{ 
                    display: 'inline-block',
                    padding: '12px',
                    borderRadius: '8px',
                    maxWidth: '80%',
                    backgroundColor: msg.type === 'user' ? '#f4bf41' : '#e5e7eb', 
                    color: msg.type === 'user' ? 'white' : 'black',
                    wordWrap: 'break-word',
                    overflowWrap: 'break-word',
                    whiteSpace: 'pre-wrap'
                  }}
                >
                  {msg.text}
                </div>
              </div>
            ))}

            {loading && <div style={{ color: '#6b7280' }}>ChatCat is thinking...</div>}
            <div ref={messagesEndRef} />
          </div>
        </div>

        {/*input*/}
        <div style={{ 
          display: 'flex',
          justifyContent: 'center',
          width: '100%',
          marginBottom: '70px' 
        }}>
          <div style={{ 
            display: 'flex',
            gap: '2px', 
            maxWidth: '750px', 
            width: '100%' 
          }}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
              placeholder="What is your emergency?"
              style={{ 
                flex: '1', 
                borderRadius: '32px', 
                border: '2px solid #f4bf41',
                padding: '0.5rem 1rem' 
              }}
            />

            {/*send button*/}
            <button 
              onClick={sendMessage}
              style={{
                backgroundColor: '#ff3131',
                color: 'white',
                padding: '0.5rem 1.5rem',
                borderRadius: '0.5rem',
                fontWeight: '600',
                boxShadow: '0 1px 2px 0 rgba(255 255 255 / 0.05)',
                transition: 'background-color 0.2s',
                border: '0.1px #ff3131',
                cursor: 'pointer'
              }}
              onMouseEnter={(e) => e.target.style.backgroundColor = '#cc0000'}
              onMouseLeave={(e) => e.target.style.backgroundColor = '#ff3131'}
            >
              Send
            </button>
            
            {/*login button */}
            <div onClick={() => onNavigate('login')}
              style={{
                position: 'fixed',     
                top: '110px',                 
                left: '30px',                
                zIndex: 200,
                color: 'black',
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem',
                cursor: 'pointer',
                fontWeight: '600',
              }}
              
            >
            <img src={serImage} width={20} height={20} alt="User Icon" />
            <span style={{ textDecoration: 'underline', 
              fontSize: '20px'
             }}>
              
              User Login
             </span>
           </div>
         </div>
        </div>
      </div>
    </div>
  );
}