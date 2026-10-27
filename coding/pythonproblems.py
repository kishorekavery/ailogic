
#problem 1
def search(nums, t):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = l + (r - l) // 2
        
        if nums[mid] == t:
            return mid
        
        if nums[l] <= nums[mid]:
            if nums[l] <= t < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < t <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1 

print(search([4, 5, 6, 7, 0, 1, 2],0))



#3 problem
def permute(s):
    res = []
    path = []
    used = [False] * len(s)

    def backtrack():
        if len(path) == len(s):
            res.append("".join(path))
            return
        
        for i in range(len(s)):
            if used[i]:
                continue
            
            used[i] = True
            path.append(s[i])

            backtrack()

            path.pop()
            used[i] = False

    backtrack()
    return res

print(permute('abc'))
