"""
user_creation.py - User creation for chatbot application
"""

class User:
    def__init__(self, user_id: str, name: str, email: str, location: str, age: int = None):
        """Initialize User
        
        Args:
            user_id: Unique identifier for the user
            name: Name of the user
            email: Email address of the user
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.location = location
        self.age = age
    )
    
    