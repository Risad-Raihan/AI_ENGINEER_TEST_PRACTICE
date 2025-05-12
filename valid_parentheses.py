def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Invalid character (not expected in this problem)
            return False
    return not stack

# Example usage and test cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    for s, expected in test_cases:
        result = isValid(s)
        print(f"Input: {s}, Output: {result}, Expected: {expected}, Pass: {result == expected}") 