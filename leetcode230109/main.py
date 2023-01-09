
# ** Case 1
# * Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
# * Output: 3

# ** Case 2
# * Input: words = ["a","a"], s = "aa"
# * Output: 2

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        answer = 0

        for word in words:
            check = True
            if len(word) > len(s): continue
            for i in range(len(word)):
                if word[i] != s[i]:
                    check = False
                    break;
            if check:
                answer += 1

        return answer