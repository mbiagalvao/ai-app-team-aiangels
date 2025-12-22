import React from 'react';
import catIcon from '../assets/kitty.png';
import backgroundImage from '../assets/wallpaper.png';

{/*This is the About page component that provides information
 about the ChatCAT application and we AIAngels!
 It includes details about the project's purpose,
 target users, us.*/}

export default function About() {
  return (
    <div style={{
      minHeight: '100vh',
      backgroundImage: `url(${backgroundImage})`,
      backgroundPosition: 'center',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '2rem',
      paddingTop: '100px'
    }}>

      {/* text container */}
      <div style={{
        backgroundColor: 'white',
        padding: '3rem',
        borderRadius: '24px',
        maxWidth: '800px',
        width: '100%',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)'
      }}>
        {/* header */}
        <div style={{ 
          textAlign: 'center', 
          marginBottom: '2rem',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: '1rem'
        }}>
          <img src={catIcon} width={60} height={80} alt="Cat icon" />
          <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#1f2937' }}>
            About ChatCAT and AIAngels 
          </h1>
        </div>

        {/* Descrição do Projeto */}
        <div style={{ marginBottom: '2rem' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: '600', marginBottom: '1rem', color: '#f4bf41' }}>
            The project
          </h2>
          <p style={{ lineHeight: '1.6', color: '#4b5563' }}>
           CATastrophe assists people in preparing for, responding to, and recovering from natural disasters.The target users of the app is everyone who can make use of AI-assisted disaster preparation, emergency response guidance, and post-disaster support, world-wide.
           This innovation was inspired by the increase in climate changes driven natural disasters and by the systemic failure to disseminate practical and actionable knowledge regarding preparedness for and response to natural disasters. Our team believes effective risk mitigation continues to be restricted by low disaster literacy at the individual and community levels.
           This application will enable a transition from reaction to action, transforming static information into dynamic knowledge.
           The information provided was retrieved from official, authority and thrustworthy sources, accompanied by a connection to the web. We value 24/7 availability and global usage with multiple languages' integration.
           <h2 style={{ fontSize: '1.5rem', fontWeight: '600', marginBottom: '1rem', color: '#f4bf41' }}>
            Who we are
          </h2>
           AIAngels is a women-founded and woman-lead partnership. 
           Along this project, starting in 2025, we have focused on creating responsible, human-centered technology that prioritizes safety, accessibility, and well-being.
           The core values for the AI Angels team are uplifting energy, strong communication and cooperation. 
           We are working towards being a more sustainable and responsable business are commited to further minimizing our impact. 
           At AIAngels, we believe AI has the power to give everyday life wings. We hope you enjoy using ChatCAT as much as we enjoyed creating it!
          </p>
        </div>

        {/*team*/}
        <div style={{ 
          textAlign: 'center',
          paddingTop: '2rem',
          borderTop: '2px solid #e5e7eb'
        }}>
          <p style={{ color: '#6b7280', fontSize: '0.9rem' }}>
            Guardian Angels, Powered by AI ִֶָ𓂃 ࣪ ִֶָ🪽་༘࿐
          </p>
          
        </div>
      </div>
    </div>
  );
}