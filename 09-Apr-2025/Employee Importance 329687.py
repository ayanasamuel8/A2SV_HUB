# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        indecies_map = {}
        n = len(employees)

        for i in range(n):
            indecies_map[employees[i].id] = i
        
        start = indecies_map[id]

        def countImportance(employee):
            count = employee.importance

            subordinates = employee.subordinates
            for subordinate in subordinates:
                index = indecies_map[subordinate]
                count += countImportance(employees[index])
            return count
        return countImportance(employees[start])