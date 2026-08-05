class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0 = 0
        count1 = 0
        for i in range(len(students)):
            if students[i] == 0:
                count0 += 1
            else:
                count1 += 1
        for i in range(len(sandwiches)):
            if sandwiches[i] == 0:
                if count0 != 0:
                    count0 -= 1
                else:
                    return count0 + count1
            if sandwiches[i] == 1:
                if count1 != 0:
                    count1 -= 1
                else:
                    return count0 + count1
        return count0 + count1


        