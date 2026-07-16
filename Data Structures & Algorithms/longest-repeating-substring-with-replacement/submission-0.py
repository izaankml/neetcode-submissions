from collections import Counter, defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        max_substring_length = 0
        left = 0
        char_counts = Counter()
        max_frequency = 0

        for right in range(len(s)):
            char_counts[s[right]] += 1
            max_frequency = max(max_frequency, char_counts[s[right]])

            while (right - left + 1) - max_frequency > k:
                char_counts[s[left]] -= 1
                left += 1

            max_substring_length = max(max_substring_length, right - left + 1)
        
        return max_substring_length
