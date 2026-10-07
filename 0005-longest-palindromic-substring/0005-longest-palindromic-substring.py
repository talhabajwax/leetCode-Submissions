class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_length = 1
        n = len(s)

        for i in range(n):

            # Odd-length palindrome
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length > max_length:
                    max_length = length
                    start = left

                left -= 1
                right += 1

            # Even-length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length > max_length:
                    max_length = length
                    start = left

                left -= 1
                right += 1

        return s[start:start + max_length]