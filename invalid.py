# The removeInvalidParentheses method removes the minimum number of invalid parentheses to make all resulting strings valid.

# Helper Function:
# - `isValid`: Checks if a string has balanced parentheses by maintaining a balance counter.

# BFS Approach:
# - Use a queue to explore all possible strings by removing one parenthesis at a time.
# - Use a `visited` set to avoid reprocessing strings.
# - Stop further processing once a valid string is found to ensure minimal removals.
# - Collect all valid strings of the same level.

# TC: O(2^n) - Worst case explores all substrings.
# SC: O(2^n) - Space for the queue and visited set.


from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(expression):
            balance = 0
            for char in expression:
                if char == "(":
                    balance += 1
                elif char == ")":
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0
     
        results = []
        visited = set([s])
        queue = deque([s])
        found = False 

        while queue:
            current = queue.popleft()

            if isValid(current):
                results.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] in ("(",")"):
                    next_str = current[:i] + current[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)

        
        return results
