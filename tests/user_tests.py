from services.user_creation import (create_profile, get_profile, update_profile, delete_profile, users_collection)

new_user_id = create_profile(name = "Inês", email = "test@example.com", country = "Portugal", city = "Lisbon", age = 30)
print(new_user_id)
