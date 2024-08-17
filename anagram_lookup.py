from itertools import combinations

def build_sorted_hash_dict(corpus: list) -> dict:
    '''Creates a fast dictionary look-up of words in a word corpus by anagrammability.
      
       Args:
        corpus (list): A list of words which should be considered

       Returns:
        dict: Returns a dictionary with sorted tuple keys that return sorted lists of all anagrams of the key (per the corpus)
              Keys: tuples of sorted letters
              Values: alphabetized list of words from the corpus which are all anagrams of each other

       Examples
       ----------
       >>> get_prime_hash_dict(["abed", "abled", "bade", "baled", "bead", "blade"])
       {
           ("a", "b", "d", "e"): ["abed", "bade", "bead"],
           ("a", "b", "d", "e", "l"): ["abled", "baled", "blade"]
       }
    
    '''
    ### BEGIN SOLUTION

    dictionary = {}
    for word in corpus:
        sorted_word = tuple(sorted(word))
        if sorted_word not in dictionary:
            dictionary[sorted_word] = [word]
        else:
            dictionary[sorted_word].append(word)
    for key in dictionary:
        dictionary[key] = sorted(dictionary[key])
    return dictionary


    ### END SOLUTION 


prime_map = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }


def prime_hash(word: str):
  #calculates the prime hash value for a given word
  hash_value = 1
  for letter in word:
     hash_value *= prime_map[letter]
  return hash_value


def build_prime_hash_dict(corpus):
    '''Creates a fast dictionary look-up of words in a word corpus by anagrammability.

       Args:
        corpus (list): A list of words which should be considered

       Returns:
        dict: Returns a dictionary with prime hash keys that return sorted lists of all anagrams of the key (per the corpus)
              Keys: Prime hash values (ie. each letter mapped to a prime number, then multiplied together)
              Values: alphabetized list of words from the corpus which are all anagrams of each other

       Examples
       ----------
       >>> get_prime_hash_dict(["abed", "abled", "bade", "baled", "bead", "blade"])
       {
           462: ["abed", "bade", "bead"],
           17094: ["abled", "baled, "blade"]
       }
    '''
    ### BEGIN SOLUTION

    prime_dictionary = {}
    for word in corpus:
        hash = prime_hash(word)
        if hash not in prime_dictionary:
            prime_dictionary[hash] = [word]
        else:
            prime_dictionary[hash].append(word)
    for key in prime_dictionary:
        prime_dictionary[key] = sorted(prime_dictionary[key])
    return prime_dictionary


    ### END SOLUTION 


def get_most_anagrams(corpus:list)->list:
    '''Uses a fast dictionary look-up to explore all anagram combinations in a word corpus.
  
       Args:
        corpus (list): A list of words which should be considered

       Returns:
        list: An alphabetized list of words
              -The returned list contains the alphabetized list of the first word 
               in the alphabetized list of words in each anagram group that produces 
               the maximum number of anagrams. 
               If no anagrams can be made from the corpus an empty list is returned.

       Examples
       ----------
       >>> get_most_anagrams(["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ])
       ['art', 'pots']
       
    '''
    ### BEGIN SOLUTION
 
    anagram_dict = build_sorted_hash_dict(corpus)
    max = 1
    result = []
    for words in anagram_dict.values():
        if len(words) > max:
            max = len(words)
            result = [words[0]]
        elif len(words) == max:
            result.append(words[0])
    if max == 1:
        return []
    return sorted(result)


    ### END SOLUTION 

def get_all_anagrams(corpus:list[str])->set:
    '''Creates a set of all unique words in a word corpus that could have been used to form an anagram pair.
        Words which can't create any anagram pairs should not be included in the set.

        Args:
          corpus (list): A list of words which should be considered

        Returns:
          set: all unique words in wordlist which form at least 1 anagram pair

        Examples
        ----------
        >>> get_all_anagrams(["abed","mouse", "bead", "baled", "abled", "rat", "blade"])
        {"abed",  "abled", "baled", "bead", "blade"}
    '''
    ### BEGIN SOLUTION

    anagram_dict = build_sorted_hash_dict(corpus)
    result = set()
    for words in anagram_dict.values():
        if len(words) > 1:
            result.update(words)
    return result


    ### END SOLUTION 

if __name__ == "__main__":
    words1 = ["abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
    "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
    "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"]

    words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

    print(f"Sorting via the prime hashing function: {sorted(words1, key=prime_hash)}\n")
    
    print(f"Sorted tuple lookup dictionary: {build_sorted_hash_dict(words1)}")
    print(f"Prime hash lookup dictionary: {build_prime_hash_dict(words2)}\n")
    
    print(f"Most anagrams in words1:{get_most_anagrams(words1)}\n")
    print(f"Most anagrams in words2: {get_most_anagrams(words2)}")
