"""
 Resources needed for a 72h emergency kit based on the number of people (and disaster type?).
 source: https://www.calgary.ca/emergencies/preparedness/72-hour-kit.html
"""
from langfuse import observe

    
@observe(as_type="tool")
def resources_calculator_tool(disaster_type: str, num_people: int) -> dict:
    """
    Use this tool ONLY to calculate, estimate, or compute
    resources and items needed for a 72h emergency kit based on the disaster type and number of people.
    DO NOT use web search.

    Args:
        disaster_type: Type of natural disaster or emergency (e.g., "earthquake", "flood")
        num_people: Number of people to prepare for

    Returns:
        List of resources and their quantities
    """

    resources_list = {
            "water (liters)": 4 * num_people * 3,  # 4 liters per person per day for 3 days
            "non-perishable food (meals)": 3 * num_people * 3,  # 3 meals per person for 3 days
            "first aid kit": 1,
            "flashlight": num_people,
            "batteries (sets)": num_people,
            "blankets": num_people,
            "personal hygiene items": num_people,
            "medications": "as needed",
            "important documents (copies)": "1 per person",
            "multi-tool or Swiss Army knife": 1,
            "portable phone charger": 1,
            "cash": "small bills and coins",
            "emergency whistle": num_people,
        }

    # Additional resources based on disaster type
    if disaster_type == "earthquake":
        resources_list["dust masks"] = num_people
        resources_list["sturdy shoes"] = num_people
    elif disaster_type == "flood":
        resources_list["waterproof bags"] = num_people
        resources_list["life jackets"] = num_people
    elif (disaster_type == "hurricane") or (disaster_type == "tornado") or (disaster_type == "storm") or (disaster_type == "typhoon"):
        resources_list["plywood"] = "as needed for windows"
        resources_list["extra fuel"] = "as needed"
    
    return resources_list

