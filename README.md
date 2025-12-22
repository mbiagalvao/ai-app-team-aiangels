# CATastrophe

<img width="100" height="150" alt="image" src="https://github.com/user-attachments/assets/2ec02c91-a19f-4501-8a93-c9d6860de462" />

CATastrophe assists people in preparing for, responding to, and recovering from natural disasters.

## Overview

The target users of the app is anyone who can make use of AI-assisted disaster preparation, emergency response guidance, and post-disaster support, world-wide.

This innovation was inspired by the increase in climate changes driven natural disasters and by the systemic failure to disseminate practical and actionable knowledge regarding preparedness for and response to natural disasters. Our team believes effective risk mitigation continues to be restricted by low disaster literacy at the individual and community levels.

This application will enable a transition from reaction to action, transforming static information into dynamic knowledge.

The information provided was retrieved from official, authority and thrustworthy sources, accompanied by a connection to the wide web.The application is designed for 24/7 availability, global usage and multilingual support

This project is provided for educational purposes.

All components are individually explained.


## Features

- AI-powered disaster guidance
- Quizzes - to test users' knowledge
- Weather API connection - to maintain up-to-date meteorology
- Global design - to reach worldwide users

## Tech Stack

**Backend:**
- Python
- Google Gemini API
- Flask

**Frontend:**
- React

**Database:**
- MongoDB

**AI/ML:**
- Langfuse for observability
- Weather API
- RAG
- Function/tool calling


## Architecture

- Architecture diagram 
<img width="590" height="853" alt="image" src="https://github.com/user-attachments/assets/dd3bdf57-6738-44d2-904c-daded491390b" />

- Layer structure (UI, Service, AI, Tools)
<img width="475" height="821" alt="image" src="https://github.com/user-attachments/assets/83c32cfb-7254-41d4-b883-de34fafa61ed" />


## Installation & Setup

### Prerequisites
- Python 3.x
- API keys for required services (Google Gemini, Langfuse, Weather API)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/mbiagalvao/ai-app-team-aiangels
cd ai-app-team-aiangels
```

2. Install dependencies:
```bash
uv sync
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run the application:
```bash
uv run streamlit run app.py
```

## Usage
The UI Layer built in React will have a total of four pages:

• Main page: Page with the chatbot for the user to make requests and questions;
the AI Agent strictly answers in text;

• User page: Page where the user optionally provides his name, age, country and
city;

• Quizzes page: Pagewithquizzes for simulating various emergencies related actions
and learning what to do in different situations;

• About us page: Introduction about the company and chatbot.

**Example**
- Launch the application locally
- Navigate through the Streamlit interface
- Enter a query related to disaster preparedness, response, or recovery
- Interact with the AI assistant
- Explore quizzes, weather insights, and additional features



## Deployment

**Live Application:** https://catastrophe-aiangels.netlify.app/

**Deployment Platform:** Netlify


## Project Structure

```
project
|
├── docs/              # Documents retrieved from the web
├── frontend/          # Frontend components
├── prompts/           # Prompts for content generation
├── rag/               # Rag functionalities
├── services/          # Business logic and external integrations
├── tests/             # Function calling to test our tools
├── tools/             # Code for AI Agent's tools
├── utils/             # Prompt and tracing functions
|               
├── .env               # Configuration file used to store environment variables
├── .gitignore
├── ARCHITETURE.md     # Architecture decisions and technical justifications
├── frontend_app.py    # Single entry point file for the frontend
├── pyproject.toml     # Configuration file
├── README.md          # Comprehensive overview and setup instructions
└── requirements.txt   # Dependencies
```

## Team

- Team Member 1 - Ines Chainho: product developer and Q/A tester
- Team Member 2 - Mª Beatriz Galvao: AI developer
- Team Member 3 - Mª Eduarda Francisco: product researcher and UI designer
- Team Member 4 - Sofia Curto: UI/UX developer

### What the AI can do
- Provide disaster preparedness checklists
- Suggest response actions during emergencies
- Explain recovery steps after disasters
- Use weather and retrieved documents for grounded answers

### What the AI cannot do
- Replace emergency services
- Provide medical or legal advice
- Guarantee real-time accuracy in life-threatening situations
