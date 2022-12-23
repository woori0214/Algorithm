
# ** Case 1
# * Input: s = "ab", goal = "ba"
# * Output: true
# * Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# ** Case 2
# * Input: s = "ab", goal = "ab"
# * Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # Compare length
        if len(s) != len(goal):
            return False

        # Convert stirng -> list
        else:
            list_s = list(s)
            list_goal = list(goal)
            buddyString1 = []
            buddyString2 = []

            # compare charIndex
            for i in range(len(list_s)):
                if list_s[i] != list_goal[i]:
                    buddyString1.append(list_s[i])
                    buddyString2.append(list_goal[i])

                    if len(buddyString1) > 2:
                        return False

            if len(buddyString1) == 2 and buddyString1 == buddyString2[::-1]:
                return True

            if len(buddyString1) == 0:
                if len(list_s) > len(set(list_s)):
                    return True
                return False