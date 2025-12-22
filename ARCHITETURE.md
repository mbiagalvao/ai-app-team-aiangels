**App Purpose**

The aim of our CATastrophe app is to assist people in preparing for, responding to, and recovering from natural disasters. The target users of the app is everyone who can make use of AI-assisted disaster preparation, emergency response guidance, and post-disaster support, world-wide, regardless of their age and location.



**Backend**

To build the backend of our app, Python was used in VS Code and Git Hub, so all members could code at the same time. Google Gemini API was chosen to ensure alignment with the course methodology, and also due to the fact that it is a free API developer tool.

Some of the more challenging decisions during backend development involved choosing which tools were truly necessary to implement, given that AI agents already provide certain built-in capabilities, such as returning answers in a step-by-step format. Nevertheless, it was decided to implement the todo_lists tool, as it was required for the AI agent to retrieve context-relevant documents from the vector database, enabling more complete and accurate responses. For this reason, we used a wrapper tool to combine our custom tools with content-generation tools, such as websearch, which retrieves information from the web; rag, which retrieves data from the vector database; quiz_service and weather_report. All of these processes result in API calls.



**Frontend**

The frontend was fully built on React, because it is more modern, and the developer has more freedom in the design choices. It was programmed using HTML, CSS and JavaScript. In addition, Flask was used for the communication with the Interface Adapter because it is user-friendly, and very recommended to use with React.

The technical difficulties related to the frontend have more to do with the structure of the app and how to conjugate the backend into something readable and easily-usable. For example, every detail about how the quiz logic could be implemented into the frontend was important, such as the score and the visualization of the correct options.



**Database**

For the information database, MongoDB was chosen due to the members' familiarity with it. For the Users collection, it was decided that MongoDB would generate the user_ids. Therefore, when creating the functions to handle user profiles, this variable was not explicitly defined; only the fields provided by users on the app’s login page were included (name, email, city, country, and age).



**AI/ML**

The AI Agent's traces are monitored by the observability platform Langfuse.

A Weather API was used, because there is a need for access to real-time, historical, and forecast weather data.

RAG was implemented to let our LLM access and use external, up-to-date information to generate more complete and reliable answers to the users' requests.



**Deployment**

The platform chosen for deployment was Netlify, since this is the most recommend for UI interfaces built in React.

