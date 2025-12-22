import React, { useState } from 'react';
import backgroundImage from '../assets/wallpaper.png';

{/*This is the Login page component that handles user authentication,
 allowing users to sign up for a new account or log in to an existing one.
 It manages form state, handles API requests, and displays error messages.*/}

export default function Login({ onBack, onLogin }) {
  const [isSignup, setIsSignup] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    country: '',
    city: '',
    age: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (isSignup) {
        const response = await fetch('https://chatcat-backend.onrender.com/user/create', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name: formData.name,
            email: formData.email,
            country: formData.country,
            city: formData.city,
            age: formData.age ? parseInt(formData.age) : null
          })
        });

        const data = await response.json();

        if (response.ok) {
          const userId = data.user_id;
          const userResponse = await fetch(`https://chatcat-backend.onrender.com/user/${userId}`);
          const userData = await userResponse.json();
          onLogin(userData);
        } else {
          setError(data.error || 'Signup failed');
        }
      } else {
        const response = await fetch(`https://chatcat-backend.onrender.com/user/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: formData.email })
        });

        const data = await response.json();

        if (response.ok) {
          onLogin(data);
        } else {
          setError(data.error || 'Login failed - email not found');
        }
      }
    } catch (error) {
      console.error('Error:', error);
      setError('Error connecting to server');
    } finally {
      setLoading(false);
    }
  };

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
        padding: '3rem',
        borderRadius: '24px',
        maxWidth: '500px',
        width: '100%',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)'
      }}>
        <h1 style={{ 
          fontSize: '2rem', 
          marginBottom: '0.5rem', 
          textAlign: 'center',
          color: '#1f2937'
        }}>
          {isSignup ? 'Create Account' : 'Welcome!'}
        </h1>
        <p style={{ 
          textAlign: 'center', 
          color: '#6b7280', 
          marginBottom: '2rem',
          fontSize: '0.9rem'
        }}>
          {isSignup ? 'Sign up to get started' : 'Login to continue'}
        </p>

        {error && (
          <div style={{
            backgroundColor: '#fee2e2',
            color: '#ef4444',
            padding: '0.75rem',
            borderRadius: '8px',
            marginBottom: '1rem',
            fontSize: '0.9rem'
          }}>
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          {isSignup && (
            <input
              type="text"
              name="name"
              placeholder="Full Name"
              value={formData.name}
              onChange={handleChange}
              required
              style={{
                width: '100%',
                padding: '0.75rem',
                marginBottom: '1rem',
                borderRadius: '8px',
                border: '2px solid #e5e7eb',
                boxSizing: 'border-box',
                fontSize: '1rem',
                transition: 'border-color 0.2s'
              }}
            />
          )}

          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
            style={{
              width: '100%',
              padding: '0.75rem',
              marginBottom: '1rem',
              borderRadius: '8px',
              border: '2px solid #e5e7eb',
              boxSizing: 'border-box',
              fontSize: '1rem'
            }}
          />

          {isSignup && (
            <>
              <input
                type="text"
                name="country"
                placeholder="Country"
                value={formData.country}
                onChange={handleChange}
                required
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  marginBottom: '1rem',
                  borderRadius: '8px',
                  border: '2px solid #e5e7eb',
                  boxSizing: 'border-box',
                  fontSize: '1rem'
                }}
              />

              <input
                type="text"
                name="city"
                placeholder="City"
                value={formData.city}
                onChange={handleChange}
                required
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  marginBottom: '1rem',
                  borderRadius: '8px',
                  border: '2px solid #e5e7eb',
                  boxSizing: 'border-box',
                  fontSize: '1rem'
                }}
              />

              <input
                type="number"
                name="age"
                placeholder="Age (optional)"
                value={formData.age}
                onChange={handleChange}
                min="1"
                max="120"
                style={{
                  width: '100%',
                  padding: '0.75rem',
                  marginBottom: '1rem',
                  borderRadius: '8px',
                  border: '2px solid #e5e7eb',
                  boxSizing: 'border-box',
                  fontSize: '1rem'
                }}
              />
            </>
          )}

          <button
            type="submit"
            disabled={loading}
            style={{
              width: '100%',
              backgroundColor: loading ? '#d1d5db' : '#f4bf41',
              color: 'white',
              padding: '0.875rem',
              borderRadius: '8px',
              border: 'none',
              cursor: loading ? 'not-allowed' : 'pointer',
              fontWeight: '600',
              fontSize: '1rem',
              marginBottom: '1rem',
              transition: 'background-color 0.2s', 
              boxSizing: 'border-box'
            }}
          >
            {loading ? 'Please wait...' : (isSignup ? 'Sign Up' : 'Login')}
          </button>
        </form>

        <div style={{
          textAlign: 'center',
          padding: '1rem 0',
          borderTop: '1px solid #e5e7eb',
          borderBottom: '1px solid #e5e7eb',
          margin: '1rem 0'
        }}>
          <p style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '0.5rem' }}>
            {isSignup ? 'Already have an account?' : "Don't have an account?"}
          </p>
          <button
            onClick={() => {
              setIsSignup(!isSignup);
              setError('');
              setFormData({
                name: '',
                email: '',
                country: '',
                city: '',
                age: ''
              });
            }}
            style={{
              color: '#f4bf41',
              background: 'none',
              border: 'none',
              cursor: 'pointer',
              fontWeight: '600',
              fontSize: '1rem',
              textDecoration: 'underline'
            }}
          >
            {isSignup ? 'Login here' : 'Sign up here'}
          </button>
        </div>

        <button
          onClick={onBack}
          style={{
            width: '100%',
            backgroundColor: '#6b7280',
            color: 'white',
            padding: '0.75rem',
            borderRadius: '8px',
            border: 'none',
            cursor: 'pointer',
            fontWeight: '600',
            fontSize: '1rem'
          }}
        >
          Back to ChatCat
        </button>
      </div>
    </div>
  );
}