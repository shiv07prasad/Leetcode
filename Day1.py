import numpy as np
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        word = word1[0] + word2[0]
       
        if len1 > len2 :
            list1 = list(np.arange(1,len2))
            
            for i in list1 :
                word = word + word1[i] + word2[i]
            if len2 == 1:
                word = word + word1[1:]
            else :
                word = word + word1[i+1:]

        elif len2 > len1 :
            list1 = list(np.arange(1,len1))
            
            for i in list1 :
                word = word + word1[i] + word2[i]
            if len1 == 1:
                word = word + word2[1:]
            else :
                word = word + word2[i+1:]

        else :
            list3 = list(np.arange(1,len1))
           
            for i in list3 :
                word = word + word1[i] + word2[i]
                print(word)
        
        return word
