class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0

            while j < len(words):
                word = s[i + j * word_len : i + (j + 1) * word_len]

                if word not in word_count:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > word_count[word]:
                    break

                j += 1

            if j == len(words):
                result.append(i)

        return result
