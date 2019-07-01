def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        answer = []
        text_split = text.split(" ")
        for i in range(2,len(text_split)):
            if text_split[i-2] == first and text_split[i-1] == second:
                answer.append(text_split[i])
        return answer
