import itertools

def basic_checks(word1:str, word2:str)-> tuple[bool, str, str]:
    '''Implements top-level checks common to each is_anagram approach. 
       Anagram basic checks include ensuring the two input words:
        -aren't be the same word
        -are case insensitive
        -don't include characters other than A-Z, a-z
        -have the same length, with at least two letters

       Args:
         word1: The first word
         word2: The second word

       Returns:
         bool: False if the two words fail a basic check, True otherwise
         str: A lowercase version of word1 only containing A-Z, a-z
         str: A lowercase version of word2 only containing A-Z, a-z
        
       Examples:
        >>> basic_checks("baste2", "Beast")
        True, baste, beast
        >>> basic_checks("baste", "Beasts")
        False, baste, beasts
    '''

    word1 = word1.lower()
    word2 = word2.lower()

    x = ""
    y = ""

    for i in range (0, len(word1)):
        if ord(word1[i]) <= 122 and ord(word1[i]) >= 97:
            x += word1[i]
    word1 = x

    for i in range (0, len(word2)):
        if ord(word2[i]) <= 122 and ord(word2[i]) >= 97:
            y += word2[i]
    word2 = y

    if word1 == word2:
        return False, word1, word2

    if len(word1) == len(word2):
        return True, word1, word2
    else:
        return False, word1, word2
 

def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    
    check, word1, word2 = basic_checks(word1, word2)
    if (check == False):
        return False

    permutation_list = list(itertools.permutations(word1))
    x = tuple(word2)
    if x in permutation_list:
        return True
    else: return False


def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''

    check, word1, word2 = basic_checks(word1, word2)
    if (check == False):
        return False
    
    word2_list = list(word2)
    word1_list = list(word1)

    for char in word1_list:
        if char in word2_list:
            word2_list[word2_list.index(char)] = None
            word1_list[word1_list.index(char)] = None

        else: return False

    return True


def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''Two approaches:
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. chr(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''

    check, word1, word2 = basic_checks(word1, word2)
    if (check == False):
        return False

    dictionary1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
    'w': 0, 'x': 0, 'y': 0, 'z': 0 }

    dictionary2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
    'w': 0, 'x': 0, 'y': 0, 'z': 0 }

    for char in word1:
        dictionary1[char] = dictionary1[char] + 1

    for char in word2:
        dictionary2[char] = dictionary2[char] + 1
    if dictionary1 == dictionary2:
        return True
    return False


def is_anagram_sort_hash(word1:str, word2:str)->bool:
    '''Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''

    check, word1, word2 = basic_checks(word1, word2)
    if (check == False):
        return False
    
    list1 = list(word1)
    list2 = list(word2)

    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)

    if list1_sorted == list2_sorted:
        return True
    return False


ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def is_anagram_prime_hash(word1:str, word2:str)->bool:
    '''Create a dictionary of prime numbers (see chToprime above). Use the ascii value of each letter in both
      words to construct a unique numeric representation of the word (called a 'hash').
      Words with the same hash value are anagrams of each other.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''

    check, word1, word2 = basic_checks(word1, word2)
    if (check == False):
        return False    
    
    product1 = 1
    product2 = 1

    for char in word1:
        product1 = product1 * ch_to_prime[char] 

    for char in word2:
        product2 = product2 * ch_to_prime[char] 

    if product1 == product2:
        return True
    return False


if __name__ == "__main__":
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort_hash, is_anagram_prime_hash]
    word1 = "Beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")
