class TodoList:
    def __init__(self, disaster_type: str) -> str:
        """
        Intialize a to-do list for disaster preparation and/or response.

        Args:
            disaster_type: Type of natural disaster or emergency (e.g., "earthquake", "fire")

        Returns:
            TodoList
        """
        self.disaster_type = disaster_type
        self.tasks = []
    
    def add_task():




    @observe(as_type="generation")
    def to_do_list(self, message: str, context: str=None):
        """
        Generate a to-do list for a given natural disaster or emergency.
        
        Args:
            message: User request for a to-do list (disaster type included in the message)
            context: Optional context (possibly retrieved from the vector DB)

        Returns:
            To-do list as a string    
        """
        disaster_type = self.extract_disaster_type(message)

        system_prompt = self.prompts.format(
            "to_do_list_system",
            disaster= disaster_type)

        # Format context section
        user_prompt = message
        if context:
            user_prompt = f"{message}\n\nRELEVANT CONTEXT:\n{context}"
        
        try:
            response = self.client.models.generate_content(
                model = self.model_name,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    system_instruction=system_prompt
                )
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"