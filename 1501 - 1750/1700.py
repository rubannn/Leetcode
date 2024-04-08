from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                if students.count(sandwiches[0]) == 0:
                    return len(students)
                else:
                    students = students[1:] + [students[0]]
        return 0
