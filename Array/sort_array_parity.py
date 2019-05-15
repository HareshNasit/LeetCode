def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_index = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                temp = A[even_index]
                A[even_index] = A[i]
                A[i] = temp
                even_index += 1
        print A
        return A

        #Brute Force
        # odd = []
        # even = []
        # for i in range(len(A)):
        #     h = A.pop()
        #     if h % 2 == 0:
        #         even.append(h)
        #     else:
        #         odd.append(h)
        # return even + odd
