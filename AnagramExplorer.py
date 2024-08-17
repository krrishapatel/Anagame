
from collections import Counter
from itertools import combinations

class AnagramExplorer:
    def __init__(self, all_words: list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.build_lookup_dict() # Only calculated once, when the explorer object is created

    @property
    def corpus(self):
      return self.__corpus

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str]) -> bool:
        '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)
            -are both at least 3 letters long (and the same)
            -form a valid anagram pair
            -consist entirely of letters chosen at the beginning of the game

            Args:
                pair (tuple): Two strings representing the guessed pair
                letters (list): A list of letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
        '''
        ### BEGIN SOLUTION

        word1 = pair[0]
        word2 = pair[1]

        if word1.lower() not in self.corpus or word2.lower() not in self.corpus:
          return False
        if len(word1) < 3:
           return False
        if len(word1) != len(word2):
           return False
        if word1.lower() == word2.lower():
           return False
        if sorted(word1.lower()) != sorted(word2.lower()):
           return False
        if word1.lower() not in map(str.lower, self.corpus) or word2.lower() not in map(str.lower, self.corpus):
           return False
        for letter in word1.lower():
           if letter not in letters:
              return False
           
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        letters_count = Counter(letters)
        for letter in word1_count:
         if word1_count[letter] > letters_count[letter]:
            return False
        
        return True


        ### END SOLUTION 
        
    def build_lookup_dict(self) -> dict:
        '''Creates a fast dictionary look-up (via either prime hash or sorted tuple) of all anagrams in a word corpus.
       
            Args:
                corpus (list): A list of words which should be considered

            Returns:
                dict: Returns a dictionary with  keys that return sorted lists of all anagrams of the key (per the corpus)
        '''
        ### BEGIN SOLUTION

        lookup_dict = {}
        for word in self.corpus:
           #creates tuple of sorted letters as the key
           sorted_word = tuple(sorted(word))
           if sorted_word not in lookup_dict:
              lookup_dict[sorted_word] = [word] 
           else:
              lookup_dict[sorted_word].append(word)
              for key in lookup_dict:
                 lookup_dict[key] = sorted(lookup_dict[key])
        return lookup_dict

        ### END SOLUTION 

    def get_all_anagrams(self, letters: list[str]) -> set:
         '''
         Creates a set of all unique words that could have been used to form an anagram pair.
         Words which can't create any anagram pairs should not be included in the set.

            Ex)
            corpus: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
            all_anagrams: {"abed",  "abled", "baled", "bead", "blade"}

            Args:
              letters (list): A list of letters from which the anagrams should be createdin 

            Returns:
              set: all unique words in corpus which form at least 1 anagram pair
         '''
        ### BEGIN SOLUTION

         result = set()
         for key in self.anagram_lookup:
          is_valid = True
          letters_list = letters.copy()
          for letter in key:
             if letter not in letters_list:
                is_valid = False
             else:
                letters_list.remove(letter)
          anagrams = self.anagram_lookup[key]
          if len(anagrams) > 1 and is_valid and len(anagrams[0]) > 2:
             for anagram in anagrams:
               result.add(anagram)

         return result

   
        ### END SOLUTION 

    def get_most_anagrams(self, letters:list[str]) -> str:
        '''Returns any word from one of the largest lists of anagrams that 
           can be formed using the given letters.
           
            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              str: a single word from the largest anagram families
        '''
  
        ### BEGIN SOLUTION
        
        max_anagram = ""
        max_length = 0
        for anagrams in self.anagram_lookup.values():
         is_valid = True
         letters_list = letters.copy()
         if len(anagrams) > max_length:
            for letter in anagrams[0]:
               if letter not in letters_list:
                is_valid = False
               else:
                  letters_list.remove(letter)
            if is_valid:
               max_length = len(anagrams)
               max_anagram = anagrams[0]
        return max_anagram
    

        ### END SOLUTION 

if __name__ == "__main__":
  words1 = [
     "abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
     "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
     "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"
  ]
  words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

  letters = ["p", "o", "t", "s", "r", "i", "a"]

  my_explorer = AnagramExplorer(words2)

  print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_all_anagrams(letters))