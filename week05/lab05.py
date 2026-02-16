# Messy script to be refactored
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

# Calculate total age and count users for average
total_age = 0
user_count_for_age = 0
for user in users:
    if isinstance(user.get("age"), int):
        total_age += user["age"]
        user_count_for_age += 1
average_age = total_age / user_count_for_age
print(f"average user age: {average_age:.2f}")

# Get a list of all active user emails
active_user_emails = []
for user in users:
    if user.get("is_active") and user.get("email"):
        active_user_emails.append(user["email"])
print(f"active user emails: {active_user_emails}")

# lab05.py

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
    {}, # Empty dict to test missing keys
    "invalid_user" # String to test TypeErrors
]

def calculate_average_age(user_list):
    """
    Calculates the average age of users, handling empty lists and invalid data.
    
    Parameters
    ----------
    user_list : list
        A list of dictionaries representing users.

    Returns
    -------
    float
        The average age, or 0.0 if calculation fails.
    """
    total_age = 0
    count = 0

    for user in user_list:
        try:
            # removing .get() here to demonstrate strict type checking handling
            # logic: if user isn't a dict, this might raise TypeError
            if isinstance(user, dict) and isinstance(user.get("age"), int):
                total_age += user["age"]
                count += 1
        except (AttributeError, TypeError):
            print(f"Warning: Skipping invalid user data: {user}")
            continue

    try:
        average = total_age / count
        return average
    except ZeroDivisionError:
        print("Error: Cannot calculate average age (no valid user ages found).")
        return 0.0


def get_active_user_emails(user_list):
    """
    Retrieves emails for active users, robustly skipping malformed data.
    
    Parameters
    ----------
    user_list : list
        A list of dictionaries representing users.

    Returns
    -------
    list
        A list of active user emails.
    """
    active_emails = []

    for user in user_list:
        try:
            # We explicitly check keys to ensure data integrity
            # If 'is_active' or 'email' is missing, user['key'] raises KeyError
            if user['is_active'] is True:
                active_emails.append(user['email'])
        
        except KeyError as e:
            # This handles cases where a user dict exists but is missing required keys
            print(f"Warning: Skipping user {user.get('name', 'unknown')} - missing key: {e}")
        
        except TypeError:
            # This handles cases where 'user' is not a dictionary (e.g. "invalid_user")
            print(f"Warning: Found invalid data type in list: {user}")

    return active_emails


if __name__ == '__main__':
    # Call your functions and print results
    avg_age = calculate_average_age(users)
    print(f"Average user age: {avg_age:.2f}")
    print("-" * 20)
    
    active_emails = get_active_user_emails(users)
    print(f"Active user emails: {active_emails}")