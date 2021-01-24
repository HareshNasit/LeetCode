def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Runtime: O(M+N) where N is num of chars in paragraph and M is
        # num of chars in banned list.
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        print(normalized_str)
        split_words = normalized_str.split()
        words_freq = {}
        for word in split_words:
            if word not in words_freq and word not in banned:
                words_freq[word] = 1
            elif word in words_freq:
                words_freq[word] += 1
        return max(words_freq.items(), key=operator.itemgetter(1))[0]
