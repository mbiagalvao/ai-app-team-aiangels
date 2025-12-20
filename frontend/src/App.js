//React components return JSX
// a syntax that looks like HTML but is JavaScript.


import React, { useState, useRef, useEffect} from 'react';
import catIcon from './catIcon.png'; // Import the cat icon image
// useState is a hook that connects the function to the react

export default function ChatCat() {
  const [messages, setMessages] = useState([]); // box that contains chat history and setmesages changes whats inside the box
  const [input, setInput] = useState(''); //text input box (empty)
  const [loading, setLoading] = useState(false); //loading state for AI response 
  const messagesEndRef = useRef(null); //scroll automático
  //setMess, setLoad, SetInp are functions you call to update these values
  
useEffect(() => {messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);  
  
  const sendMessage = async () => { //func can wait for async actions
    if (!input.trim()) return; //do nothing if the input is empty or only spaces

    // Adiciona mensagem do usuário
    const userMsg = input; //holds text
    setMessages(prev => [...prev, { type: 'user', text: userMsg }]);
    setInput('');
    setLoading(true);

    try {
      // Chama o backend Python
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMsg })
      });

      const data = await response.json();
      
      // Adiciona resposta do AI
      setMessages(prev => [...prev, { type: 'ai', text: data.response }]);
    } catch (error) {
      setMessages(prev => [...prev, { type: 'ai', text: 'Cat is not working right now' }]);
    }
    
    setLoading(false);
  };

  return (
    <div className="flex flex-col h-screen max-w-2xl mx-auto p-4" style={{ backgroundColor: '#bdbebd', alignItems: 'center',justifyContent: 'center'}}>

     {/*header com icon do gato*/} 
      <h1 className="text-2xl font-bold mb-4flex items-center justify-center gap-2">
      <img src={catIcon} width={40} height={30} alt="Cat icon" />
      Chat Cat
  </h1> 
        
      
      {/* Containter das mensagens */}
    <div style={{ display: 'flex', justifyContent: 'center'}}></div>
      <div className="p-4 overflow-y-auto mb-4"style={{ height: '400px', width: '100%', maxWidth: '600px', margin: '0 auto',  backgroundColor: 'white',  borderRadius: '24px', border: '2px solid #d1d5db' }}>
        {messages.map((msg, i) => (
          <div 
            key={i}
            className={`mb-3 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
            
            <div 
              className={`inline-block p-3 rounded ${
               msg.type === 'user' ? 'bg-orange-500 text-white' : 'bg-red-500 text-black'
            }`}
            style={{ 
                maxWidth: '80%',
                wordWrap: 'break-word',
                overflowWrap: 'break-word',
                whiteSpace: 'pre-wrap',
                overflow: 'hidden' 
              }}
            >
              {msg.text}
            </div>
          </div>
        ))}


        {loading && <div className="text-gray-500">AI is thinking...</div>}
      
        {/* Elemento invisível para scroll automático */}
        <div ref={messagesEndRef} />
      </div>


      {/* Input */}
      <div style={{display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '20px'}}>
       <div style={{ display: 'flex', gap: '8px', maxWidth: '600px', width: '100%'}}>
         <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="What is your emergency?"
          className="flex border rounded px-4 py-2"
          style={{ flex: '1', borderRadius: '24px', border: '2px solid #d1d5db'}}
        />
        <button 
          onClick={sendMessage}
          style={{
            backgroundColor: '#ffa500',
            color: 'white',
            padding: '0.5rem 1.5rem',
            borderRadius: '0.5rem',
            fontWeight: '600',
            boxShadow: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
            transition: 'background-color 0.2s'
       }}
       onMouseEnter={(e) => e.target.style.backgroundColor = '#ea580c'}
       onMouseLeave={(e) => e.target.style.backgroundColor = '#ffa500'}
     >
       Send
      </button>
    </div>
  </div>
</div>)}
