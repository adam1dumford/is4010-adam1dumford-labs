import random
def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "The silly cat jumped over the lazy dog and laughed."
    
    >>> generate_mad_lib("brave", "knight", "battled") 
    "Once upon a time, a brave knight battled dragons and saved the kingdom."
    """
# Create the story using an f-string
    story = f"The {adjective} alien landed its spaceship on a {noun} and {verb} wildly."
    
    # Return the result
    return story

def guessing_game():
    """
    Plays a number guessing game with the user.
    """
    # 1. Generate a random secret number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    
    # 2. Prompt the user with clear instructions
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    guess = 0 # Initialize with a number that cannot be the secret
    
    # 3. Use a while loop to continue until the user guesses correctly
    while guess != secret_number:
        # 4. For each guess: Convert user input to integer
        guess = int(input("Enter your guess: "))
        attempts += 1 # Count attempts
        
        # Compare guess to secret number
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            # 5. When correct, congratulate user and show number of attempts
            print(f"Congratulations! You guessed it in {attempts} attempts!")

if __name__ == "__main__":
    # --- Test Part 1: Mad Libs ---
    print("--- Testing Mad Libs ---")
    my_story = generate_mad_lib("shiny", "banana", "exploded")
    print(my_story)
    
    # --- Test Part 2: Guessing Game ---
    print("\n--- Testing Guessing Game ---")
    guessing_game()