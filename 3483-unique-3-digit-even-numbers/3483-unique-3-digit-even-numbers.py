class Solution:
    def totalNumbers(self, digits: List[int]) -> List[int]:
        selected = []
        used = [False] * len(digits)
        output = set()

        def recursion():
            if len(selected) == 3:
                if selected[0] == 0:
                    return

                number = selected[0] * 100 + selected[1] * 10 + selected[2]

                if number % 2 == 0:
                    output.add(number)

                return

            tried_digits = set()

            for i in range(len(digits)):
                if used[i] or digits[i] in tried_digits:
                    continue

                tried_digits.add(digits[i])
                used[i] = True
                selected.append(digits[i])

                recursion()

                selected.pop()
                used[i] = False

        recursion()
        return len(output)