def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid_nums = []
        for i in range(N):
            temp_num = ""
            str_num = str(i)
            for j in range(i):
                if str_num[j] == 2:
                    temp_num += "5"
                elif str_num[j] == 5:
                    temp_num += "2"
                elif str_num[j] == 
