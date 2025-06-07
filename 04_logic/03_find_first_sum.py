"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
def find_first_sum(nums, goal : int):
    total = len(nums)
    for p1 in range(total):
        for p2 in range(p1 + 1, total):
            if nums[p1] + nums[p2] == goal:
                return [p1, p2]
    return None

def find_first_sum_dic(nums, goal : int):
    dic = {}
    for index, value in enumerate(nums):
        desired = goal - value 
        if desired in dic:
            return [dic[desired], index]
        
        dic[value] = index
    return None


nums = [4, 4, 2, 6, 2]
print(find_first_sum(nums,8))
print(find_first_sum_dic(nums,8))
