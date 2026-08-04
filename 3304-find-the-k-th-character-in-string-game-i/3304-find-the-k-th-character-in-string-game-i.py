class Solution:
    def kthCharacter(self, k: int) -> str:
        word ='a'
        def recursion(k,word):
            if len(word) >= k:
                return word[k-1]
            if word == 'a':
                word ='ab'
                return recursion (k,word)
            next_word=''
            for i in word:
                next_word+=chr(ord(i) + 1)
            word+=next_word
            return recursion(k,word)
        return recursion(k,word)

                