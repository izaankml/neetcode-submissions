class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        closing_brackets = set([')', '}', ']'])
        closing_brackets_stack = []
        for char in s:
            if char in closing_brackets:
                if (not closing_brackets_stack or char != closing_brackets_stack[-1]):
                    return False
                closing_brackets_stack.pop()
            else:
                closing_brackets_stack.append(brackets_map[char])
        
        return len(closing_brackets_stack) == 0
