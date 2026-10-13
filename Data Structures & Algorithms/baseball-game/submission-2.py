class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(0, len(operations)):
            if operations[i] == "+":
                num = record[-1] + record[-2]
                record.append(num)
            elif operations[i] == "D":
                record.append(record[-1] * 2)
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)
                