"""
 Resources needed for a 72h emergency kit based on the number of people (and disaster type?).
 source: https://www.calgary.ca/emergencies/preparedness/72-hour-kit.html
"""
from langfuse import observe

class ResourcesCalculator:
    def __init__(self, num_people: int, disaster_type: str) -> str:
        """
        Initialize resources needed for a 72h emergency kit.

        Args:
            num_people: Number of people to prepare for
            disaster_type: Type of natural disaster or emergency (e.g., "earthquake", "flood")
        """
        self.num_people = num_people
        self.disaster_type = disaster_type
        self.resources = self.calculate_resources()
    
    @observe(as_type="calculation")
    def calculate_resources(self) -> dict:
        """
        Calculate resources needed based on number of people and disaster type.

        Returns:
            Dictionary of resources and their quantities
        """
        resources_list = {
            "water (liters)": 4 * self.num_people * 3,  # 4 liters per person per day for 3 days
            "non-perishable food (meals)": 3 * self.num_people,  # 3 meals per person for 3 days
            "first aid kit": 1,
            "flashlight": self.num_people,
            "batteries (sets)": self.num_people,
            "blankets": self.num_people,
            "personal hygiene items": self.num_people,
            "medications": "as needed",
            "important documents (copies)": "1 per person",
            "multi-tool or Swiss Army knife": 1,
            "portable phone charger": 1,
            "cash": "small bills and coins",
            "emergency whistle": self.num_people,
        }

        # Additional resources based on disaster type
        if self.disaster_type == "earthquake":
            resources_list["dust masks"] = self.num_people
            resources_list["sturdy shoes"] = self.num_people
        elif self.disaster_type == "flood":
            resources_list["waterproof bags"] = self.num_people
            resources_list["life jackets"] = self.num_people
        elif (self.disaster_type == "hurricane") or (self.disaster_type == "tornado") or (self.disaster_type == "storm") or (self.disaster_type == "typhoon"):
            resources_list["plywood"] = "as needed for windows"
            resources_list["extra fuel"] = "as needed"
        
        return resources_list