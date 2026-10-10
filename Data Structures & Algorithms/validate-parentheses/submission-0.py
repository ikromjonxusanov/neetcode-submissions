class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for ch in s:
            if ch in closing_brackets:
                stack.append(ch)
                continue
            if len(stack) == 0:
                return False
            bracket = stack.pop()
            if closing_brackets[bracket] != ch:
                return False
        
        return len(stack) == 0