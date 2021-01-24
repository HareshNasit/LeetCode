def defangIPaddr(self, address: str) -> str:
        # Runtime: O(N)
        # Space: O(N)
        result = ""
        for s in address:
            if s == '.':
                result += '[.]'
            else:
                result += s
        return result

        #   (OR)
        # address = address.replace(".","[.]")
        # return address
