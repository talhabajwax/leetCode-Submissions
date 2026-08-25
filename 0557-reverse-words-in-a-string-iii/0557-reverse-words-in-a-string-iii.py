class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)

        left = 0
        right = 0

        while right <= len(chars):

            # end of a word
            if right == len(chars) or chars[right] == " ":
                end = right - 1

                # reverse current word
                while left < end:
                    chars[left], chars[end] = chars[end], chars[left]
                    left += 1
                    end -= 1

                # start of next word
                left = right + 1

            right += 1

        return "".join(chars)