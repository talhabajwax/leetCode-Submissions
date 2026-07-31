class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency={}
        count=1 
        push =0
        total=0
        contribution=0
        for i in range(len(word)): 
         if word[i] not in frequency:
            frequency[word[i]] = count           
         elif word[i] in frequency:            
            frequency[word[i]] +=1 
        frequency1=[]
        for f in frequency:
         frequency1.append(frequency[f])
        frequency1.sort(reverse=True)
        for i in range(len(frequency1)):
            if i <8:
                push=1
                contribution = frequency1[i] * push
            elif i <16:
                push=2
                contribution = frequency1[i] * push
            elif i <24:
                push=3
                contribution = frequency1[i] * push
            else:
                push=4
                contribution = frequency1[i] * push
            total=total+contribution
        return total

              
        