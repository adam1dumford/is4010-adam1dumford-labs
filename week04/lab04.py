def find_common_elements(list1, list2):
    """
    Find the common elements between two lists using sets.
    """
    # Convert the lists to sets to remove duplicates and enable fast intersection
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection (items present in both)
    common_set = set1.intersection(set2)
    
    # Convert back to a list to meet the return requirement
    return list(common_set)
def find_user_by_name(users, name):
    """
    Find a user's profile by name from a list of user data.
    """
    # Convert the list of dictionaries into a single dictionary 
    # where the 'name' is the key and the whole user object is the value.
    user_map = {user['name']: user for user in users}
    
    # Use the .get() method for an efficient O(1) lookup
    return user_map.get(name)
def get_list_of_even_numbers(numbers):
    """
    Return a new list containing only the even numbers from the input list.
    """
    # Use a list comprehension to filter for even numbers (num % 2 == 0)
    # This automatically preserves the order of the original list.
    return [num for num in numbers if num % 2 == 0]