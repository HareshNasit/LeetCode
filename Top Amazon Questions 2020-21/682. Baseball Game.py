def calPoints(self, ops: List[str]) -> int:
        # Runtime: O(N) as access in list is O(1)
        # Space: O(N) as we create mew list records
        records = []
        for op in ops:
            if op == 'C':
                records.pop()
            elif op == 'D':
                records.append(records[-1]*2)
            elif op == '+':
                records.append(records[-1] + records[-2])
            else:
                records.append(int(op))
        return sum(records)
