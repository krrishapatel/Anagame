import time
import random
from valid_anagame_words import get_valid_word_list
from AnagramExplorer import AnagramExplorer

def generate_letters(fun_factor: int, distribution: str, explorer:AnagramExplorer) -> list:
   '''Generates a list of 7 randomly-chosen lowercase letters which can form at least 
      fun_factor unique anagramable words

         Args:
          fun_factor (int): minimum number of unique anagram words offered by the chosen letters
          distribution (str): The type of distribution to use in order to choose letters
                            "uniform" - chooses letters based on a uniform distribution, with replacement
                            "scrabble" - chooses letters based on a scrabble distribution, without replacement
          explorer (AnagramExplorer): helper object used to facilitate computing anagrams based on specific letters.
         
         Returns:
             set: A set of 7 lowercase letters

         Example
         -------
         >>> explorer = AnagramExplorer(get_valid_word_list())
         >>> generate_letters(75, "scrabble", explorer)
         ["p", "o", "t", "s", "r", "i", "a"]
   '''
   letters = ["p", "o", "t", "s", "r", "i", "a"]  # Tip: Start with a consistent list of letters for testing purposes

   ### BEGIN SOLUTION

   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   if distribution == "uniform":
        while True:
            letters.clear()
            for i in range (7):
                number = random.randint(0, 25)
                letters.append(alphabet[number])
            if len(explorer.get_all_anagrams(letters)) >= fun_factor:
                break
   else:
        while True:
            scrabble_distribution = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 
        'b', 'b', 
        'c', 'c', 
        'd', 'd', 'd', 'd', 
        'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 
        'f', 'f', 
        'g', 'g', 'g', 
        'h', 'h', 
        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 
        'j', 
        'k', 
        'l', 'l', 'l', 'l', 
        'm', 'm', 
        'n', 'n', 'n', 'n', 'n', 'n', 
        'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
        'p', 'p', 
        'q', 
        'r', 'r', 'r', 'r', 'r', 'r', 
        's', 's', 's', 's', 
        't', 't', 't', 't', 't', 't', 
        'u', 'u', 'u', 'u', 
        'v', 'v', 
        'w', 'w', 
        'x', 
        'y', 'y', 
        'z']

            letters.clear()
            for i in range (7):
                number = random.randint(0, len(scrabble_distribution)-1)
                letters.append(scrabble_distribution[number])
                scrabble_distribution.pop(number)
            if len(explorer.get_all_anagrams(letters)) >= fun_factor:
                break
    
   return letters


   ### END SOLUTION 
   return letters

def parse_guess(guess:str) -> tuple:
    '''Splits an entered guess into a two word tuple with all white space removed
        Args:
            guess (str): A single string reprsenting the player guess

        Returns:
            tuple: A tuple of two words. ("", "") in case of invalid input.

        Examples
        --------
        >>> parse_guess("eat, tea")
        ("eat", "tea")

        >>> parse_guess("eat , tea")
        ("eat", "tea")

        >>> parse_guess("eat,tea")
        ("eat", "tea")

        >>> parse_guess("eat tea")
        ("", "")
    '''
    ### BEGIN SOLUTION
    
    for i in range(len(guess)):
        if guess[i:i+1] == " " or guess[i+1:i] == " " or guess[i:i+1] == "  ":
            guess = guess[0:i] + guess[i+1:]
            i -= 1
    guess = guess.split(",")
    if len(guess) != 2:
        return "",""
    else:
        return guess[0], guess[1]


   ### END SOLUTION 

def play_game(time_limit: int, letters: list, explorer:AnagramExplorer) -> list:
    '''Plays a single game of AnaGame

       Args:
         time_limit: Time limit in seconds
         letters: A list of valid letters from which the player can create an anagram
         explorer (AnagramExplorer): helper object used to compute anagrams of letters.

       Returns:
          A list of tuples reprsenting all player guesses
   '''
    ### BEGIN SOLUTION

    start_time = time.time()
    guesses = []

    while time.time() - start_time < time_limit:
        guess = input("Enter your guess: ") 
        if guess.lower() == 'quit':
            break
        if guess.lower() == 'hint': 
            print(f"Hint: Try finding words using these letters: {letters}")
            continue
        parsed_guess = parse_guess(guess)
        if parsed_guess == ("", ""): 
            print("Invalid guess format. Please use the format 'word1,word2'.")
            continue
        guesses.append(parsed_guess)


    ### END SOLUTION

def calc_stats(guesses: list, letters: list, explorer) -> dict:
    '''Aggregates several statistics into a single dictionary with the following key-value pairs:
        "valid" - list of valid guesses
        "invalid" - list of invalid/duplicate guesses
        "score" - per the rules of the game
        "accuracy" -  truncated int percentage representing valid player guesses out of all player guesses
                      3 valid and 5 invalid guesses would result in an accuracy of 37 --> 3/8 = .375
        "guessed" - set of unique words guessed from valid guesses
        "not guessed" - set of unique words not guessed
        "skill" - truncated int percentage representing the total number of unique anagram words guessed out of all possible unique anagram words
                  Guessing 66 out of 99 unique words would result in a skill of 66 --> 66/99 = .66666666
     Args:
      guesses (list): A list of tuples representing all word pairs guesses by the user
      letters (list): The list of valid letters from which user should create anagrams
      explorer (AnagramExplorer): helper object used to compute anagrams of letters.

     Returns:
      dict: Returns a dictionary with seven keys: "valid", "invalid", "score", "accuracy", "guessed", "not guessed", "skill"
    
     Example
     -------
     >>> letters = ["p", "o", "t", "s", "r", "i", "a"]
     >>> guesses = [("star","tarts"),("far","rat"),("rat","art"),("rat","art"),("art","rat")]
     >>> explorer = AnagramExplorer(get_valid_word_list())
     >>> calc_stats(guesses, letters, explorer)
     {
        "valid":[("rat","art")],
        "invalid":[("star","tarts"),("far","rat"),("rat","art"),("art","rat")],
        "score": 1,
        "accuracy": 20,
        "guessed": { "rat", "art" },
        "not_guessed": { ...73 other unique },
        "skill": 2
     }
    '''
    stats = {}
    stats["valid"] = []   #list of tuples
    stats["invalid"] = [] #list of tuples
    stats["score"] = 0    #total score per the rules of the game
    stats["accuracy"] = 0 #truncated int percentage representing valid player guesses out of all player guesses
    stats["skill"] = 0    #truncated int percentage representing unique guessed words out of all possible unique anagram words
    stats["guessed"] = set() #unique valid guessed words
    stats["not guessed"] = set() #unique words the player could have guessed, but didn’t
    ### BEGIN SOLUTION

    all_possible_anagrams = set(explorer.get_all_anagrams(letters)) 
    unique_valid_guesses = set()

    for guess in guesses:
        word1, word2 = guess
        if word1 in all_possible_anagrams and word2 in all_possible_anagrams and word1 != word2:
            if guess not in stats["valid"]: 
                stats["valid"].append(guess)
                unique_valid_guesses.add(word1)
                unique_valid_guesses.add(word2)
                stats["score"] += 1
            else:
                stats["invalid"].append(guess)
        else:
            stats["invalid"].append(guess)

    if guesses:
        stats["accuracy"] = int((len(stats["valid"]) / len(guesses)) * 100) 
    else:
        0
    stats["guessed"] = unique_valid_guesses
    stats["not guessed"] = all_possible_anagrams - unique_valid_guesses
    if all_possible_anagrams:
        stats["skill"] = int((len(unique_valid_guesses) / len(all_possible_anagrams)) * 100) 
    else:
        0

    ### END SOLUTION 

    return stats

def display_stats(stats):
    '''Prints a string representation of the game results

        Args:
          score_info (dict): a dictionery of game play information
    '''
    
    print("\nThanks for playing Anagame!\n")
    print("------------")
    print(f"Accuracy: {round(stats['accuracy'], 2)}%")
    print(f" valid guesses ({len(stats['valid'])}):", end=" ")
    for guess in stats['valid']:
        print(f"  {guess[0]},{guess[1]}", end=" ")
    print(f"\n invalid guesses ({len(stats['invalid'])}):", end=" ")
    for guess in stats['invalid']:
        print(f"  {guess[0]},{guess[1]}", end=" ")
    print("\n------------")
    print(f"Skill: {stats['skill']}% ")
    print(f" Unique words used:", end=" ")
    for guess in sorted(stats['guessed']):
        print(f"  {guess}", end=" ")
    print(f"\n Words you could have used:", end=" ")
    for guess in sorted(stats['not guessed']):
        print(f"  {guess}", end=" ")
    print("\n------------")
    print(f"AnaGame - Final Score: {stats['score']}")
    print("------------")


if __name__ == "__main__":
  time_limit = 60

  explorer = AnagramExplorer(get_valid_word_list()) #helper object
  letters = generate_letters(100, "scrabble", explorer)

  print("\nWelcome to Anagame!\n")
  print("Please enter your anagram guessess separated by a comma: eat,tea")
  print("Enter 'quit' to end the game early, or 'hint' to get a useful word!\n")
  print(f"You have {time_limit} seconds to guess as many anagrams as possible!")
  print(f"{letters}")

  guesses = play_game(time_limit, letters, explorer)
  stats_dict = calc_stats(guesses, letters, explorer)
  display_stats(stats_dict)