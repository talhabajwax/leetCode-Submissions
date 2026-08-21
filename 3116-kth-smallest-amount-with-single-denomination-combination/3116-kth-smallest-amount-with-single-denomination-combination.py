class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        left=1
        right=min(coins)*k
        while left <= right:
            middle = (left + right) // 2
            count=0
            for mask in range(1, 1 << len(coins)):
                selected = 0
                lcm = 1
                for i in range(len(coins)):
                    if mask & (1 << i):
                        selected += 1
                        lcm = math.lcm(lcm, coins[i])
                if selected % 2 == 1:
                    count += middle // lcm
                else:
                    count -= middle // lcm
            if count >= k:
                right = middle - 1
            else:
                left = middle + 1
        return left
            


            





'''        numbers=[]
        for i in range(0,len(coins)):
            numbers.append(coins[i])
            num=coins[i]
            count=1
            while count < k:
                num=num+coins[i]
                numbers.append(num)
                count+=1
        numbers=sorted(set(numbers))
        return numbers[k-1]
         for coin in coins:
                count += middle // coin
            for i in range(0,len(coins)):
                for m in range(i+1,len(coins)):
                    lcm = math.lcm(coins[i], coins[m])
                    count -= middle // lcm
                    for mask in range(1, 1 << len(coins)): '''

            