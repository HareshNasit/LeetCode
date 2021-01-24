def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Runtime: O(mlogk) where m is the non repeating words and k is given
        # Space: O(n)
        freqs = {}
        for word in words:
            if word not in freqs:
                freqs[word] = -1
            else:
                freqs[word] -= 1
        heap = []
        for key in freqs:
            heap.append((freqs[key], key))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


        # Runtime: O(n*logn)
        # Space: O(n)
        # freqs = {}
        # for word in words:
        #     if word not in freqs:
        #         freqs[word] = 1
        #     else:
        #         freqs[word] += 1
        # keys = list(freqs.keys())
        # keys.sort(key = lambda w: (-freqs[w], w))
        # return keys[:k]
