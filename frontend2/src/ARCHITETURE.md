**App Purpose**

The aim of our CATastrophe app is to assist people in preparing for, responding to, and recovering from natural disasters. The target users of the app is everyone who can make use of AI-assisted disaster preparation, emergency response guidance, and post-disaster support, world-wide, regardless of their age and location.



**Backend**

To build the backend of our app, Python was used in VS Code and Git Hub, so all members could code at the same time.

Google Gemini API was chosen to ensure alignment with the course methodology, and also due to the fact that it is a free API developer tool.

Lastly, Flask was used for the communication with the Interface Adapter because it is user-friendly, and very recommended to use with React.



**Frontend**

The frontend was fully built on React, because it is more modern, and the developer has more freedom in the design choices. It was programmed using HTML, CSS and JavaScript.



**Database**

For the information database, MongoDB was chosen due to the members' familiarity with it.

For the Users Collection, we decided MongoDB would generate the user_ids, so when creating our functions to handle the profiles, we did not create that variable, only the ones that the users will input in the Login page of the app (name, email, city, country, age).

For the Documents Collection, we created a function that implements the document ingestion pipeline responsible for transforming unstructured PDF content into structured, searchable data stored in MongoDB.



**AI/ML**

The AI Agent's traces are monitored by the observability platform Langfuse.

A Weather API was used, because there is a need for access to real-time, historical, and forecast weather data.

RAG was implemented to let our LLM access and use external, up-to-date information to generate more complete and reliable answers to the users' requests.

