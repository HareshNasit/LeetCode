def replaceWords(self, dict, sentence):
        """
        https://leetcode.com/problems/replace-words/
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # list_sentence = sentence.split(' ')
        # for i in range(len(list_sentence)):
        #     shortest_word = ""
        #     for letter in list_sentence[i]:
        #         shortest_word += letter
        #         if shortest_word in dict:
        #             list_sentence[i] = shortest_word
        #             break
        # return ' '.join(list_sentence)
        #           OR
        new_sentence = []
        for word in sentence.split():
            for dict_word in dict:
                if word.find(dict_word) == 0:
                    new_sentence.append(dict_word)
                    break
            else:
                new_sentence.append(word)
        return ' '.join(new_sentence)
