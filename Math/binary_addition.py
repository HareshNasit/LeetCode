def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #print(bin(int(a,2) + int(b,2)))
        return str(bin(int(a,2) + int(b,2)))[2:]
        
