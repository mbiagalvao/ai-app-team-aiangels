import React, { useState, useEffect } from 'react';
import backgroundImage from '../assets/wallpaper.png';

{/*This is the Quiz page component that fetches 
quiz questions from the backend, 
displays them to the user, and handles user interactions 
such as answering questions and showing the final score.*/}

export default function Quiz({ onBack }) {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState(null);

  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    setLoading(true);
    try {
      const response = await fetch('https://chatcat-backend.onrender.com/quiz/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          topic: 'natural disasters',
          questions: 5
        })
      });

      const data = await response.json();
      console.log("RECEIVED:", data);
      
      if (data.questions && data.questions.length > 0) {
        setQuestions(data.questions);
      }
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  const handleAnswer = (index) => {
    setSelectedAnswer(index);

    if (index === questions[currentQuestionIndex].correct) {
      setScore(score + 1);
    }

    setTimeout(() => {
      if (currentQuestionIndex + 1 < questions.length) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setSelectedAnswer(null);
      } else {
        setShowResult(true);
      }
    }, 1000);
  };

  const resetQuiz = () => {
    setCurrentQuestionIndex(0);
    setScore(0);
    setShowResult(false);
    setSelectedAnswer(null);
    fetchQuestions();
  };

  if (loading) {
    return (
      <div style={{ 
              backgroundImage: `url(${backgroundImage})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              backgroundRepeat: 'no-repeat',
              alignItems: 'center',
              flexDirection: 'column',
              justifyContent: 'center',
              display: 'flex',
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              margin: 0,
              padding: 0
            }} >
        <h2 style={{ fontSize: '1.5rem', color: '#1f2937' }}> Loading questions... Thank you for your patience!</h2>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div style={{
        minHeight: '100vh',
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        flexDirection: 'column',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        paddingTop: '80px'
      }}>
        <div style={{ textAlign: 'center' }}>
          <p style={{ fontSize: '1.2rem', marginBottom: '1rem' }}>No questions available :(</p>
          <button onClick={resetQuiz} style={{
            backgroundColor: '#f4bf41',
            color: 'white',
            padding: '0.75rem 1.5rem',
            borderRadius: '0.5rem',
            border: 'none',
            cursor: 'pointer',
            fontWeight: '600'
          }}>
            Try Again
          </button>
        </div>
      </div>
    );
  }

  if (showResult) {
    return (
      <div style={{
        minHeight: '100vh',
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem',
        paddingTop: '100px'
      }}>
        <div style={{
          backgroundColor: 'white',
          padding: '3rem',
          borderRadius: '24px',
          textAlign: 'center',
          maxWidth: '500px',
          width: '100%',
          boxShadow: '0 4px 6px rgba(0,0,0,0.1)'
        }}>
          <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}> Quiz ended! </h1>
          <p style={{ fontSize: '1.5rem', marginBottom: '2rem' }}>
            Score: {score} / {questions.length}
          </p>
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <button onClick={resetQuiz} style={{
              backgroundColor: '#f4bf41',
              color: 'white',
              padding: '0.75rem 1.5rem',
              borderRadius: '0.5rem',
              border: 'none',
              cursor: 'pointer',
              fontWeight: '600',
              fontSize: '1rem'
            }}>
              New Quiz
            </button>
            <button onClick={onBack} style={{
              backgroundColor: '#6b7280',
              color: 'white',
              padding: '0.75rem 1.5rem',
              borderRadius: '0.5rem',
              border: 'none',
              cursor: 'pointer',
              fontWeight: '600',
              fontSize: '1rem'
            }}>
              Back
            </button>
          </div>
        </div>
      </div>
    );
  }

  const currentQuestion = questions[currentQuestionIndex];

  return (
    <div style={{
      minHeight: '100vh',
      backgroundImage: `url(${backgroundImage})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '2rem',
      paddingTop: '100px'
    }}>
      <div style={{
        backgroundColor: 'white',
        padding: '2rem',
        borderRadius: '24px',
        maxWidth: '600px',
        width: '100%',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)'
      }}>
        <div style={{ marginBottom: '1rem', display: 'flex', justifyContent: 'space-between' }}>
          <span style={{ color: '#6b7280', fontWeight: '600' }}>
            Question {currentQuestionIndex + 1} / {questions.length}
          </span>
          <span style={{ color: '#ffa500', fontWeight: '600' }}>
            Score: {score}
          </span>
        </div>

        <h2 style={{ fontSize: '1.5rem', marginBottom: '2rem', color: '#1f2937' }}>
          {currentQuestion.question}
        </h2>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {currentQuestion.answers.map((answer, index) => (
            <button
              key={index}
              onClick={() => handleAnswer(index)}
              disabled={selectedAnswer !== null}
              style={{
                padding: '1rem',
                borderRadius: '12px',
                border: '2px solid',
                borderColor: 
                  selectedAnswer === index 
                    ? (index === currentQuestion.correct ? '#22c55e' : '#ef4444')
                    : '#d1d5db',
                backgroundColor: 
                  selectedAnswer === index
                    ? (index === currentQuestion.correct ? '#dcfce7' : '#fee2e2')
                    : 'white',
                cursor: selectedAnswer !== null ? 'not-allowed' : 'pointer',
                fontSize: '1rem',
                textAlign: 'left',
                fontWeight: '500'
              }}
            >
              {answer}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}