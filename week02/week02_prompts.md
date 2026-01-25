## Problem 1: Debugging

**My Prompt:**
```text
Context: I have a Python function that is supposed to calculate the sum of all even numbers in a list, but it contains a logical error.
Code:
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1: 
            total += num
    return total

Persona: You are an expert Python debugger and instructor.
Task: Identify the bug in the code above and rewrite the function so it correctly sums only the even numbers.
Format: Provide the fixed Python code in a code block, followed by a one-sentence explanation of what was wrong.

Corrected code:

def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed: Check for remainder 0 to identify even numbers
            total += num
    return total

Explanation:
The AI helped me understand that by changing the code to num % 2 == 0, it correctly targets even numbers.

## Problem 2: Refactoring

**My Prompt:**
```text
Context: I have a Python function that filters a list of users, but it is written in a verbose, non-Pythonic way using index-based loops.
Code:
def get_names_of_adults(users):
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results

Persona: You are a Senior Python Developer who loves clean, concise code.
Task: Refactor this function to use a "list comprehension" instead of a for-loop. The goal is to make it more readable and Pythonic.
Format: Return only the refactored function code followed by a brief bullet point explaining the change.

Corrected code:

def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users who are 18 or older."""
    return [user['name'] for user in users if user['age'] >= 18]

Explanation: 

The AI helped me understand that "for" and "append" needed to be replaced by a single-line list comprehension.

## Problem 3: Documenting

**My Prompt:**
```text
Context: I have a working Python function that calculates area, but it lacks professional documentation.
Code:
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

Persona: You are a strict Python Technical Writer who follows the NumPy documentation style guide.
Task: Add a comprehensive NumPy-style docstring to this function. You must explicitly document the "Parameters", "Returns", and "Raises" sections (specifically mentioning the ValueError).
Format: Return the complete, documented Python code block.

Documented code:

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle.
    width : float or int
        The width of the rectangle.

    Returns
    -------
    float or int
        The calculated area (length * width).

    Raises
    ------
    ValueError
        If length or width is less than or equal to 0.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

    Explanation:

    The AI helped created a Num-py style docstring that documents the inputs, outputs, and potential errors.