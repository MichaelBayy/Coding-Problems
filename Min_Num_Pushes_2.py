'''
3016. Minimum Number of Pushes to Type Word II

You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.
'''

class Solution:
    def minimumPushes(self, word: str) -> int:
        #create a dictionary that gets the frequency of characters in the word and sorts descending by count
        freq = {}
        for c in set(word):
          freq[c] = word.count(c)

        freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse = True))
      
        #For the cost, assign a character cost of 'press' multiplied by the count
        #'press' cost increments after the digit 9 is met (ie all the first character slots are taken)
        press = 1
        cost = 0
        button = 2

        for keys, items in freq.items():
            if button > 9:
                press += 1
                button = 2
            cost += (press*items)
            button += 1
          
        return cost
