def average(salary: list[int]) -> float:
    # set_of_salaries = set(salary[0])
    s = 0
    mx, mn = salary[0], salary[1]
    if mx < mn:
        mx, mn = mn, mx

    c = 0

    for sal in salary[2:]:
        c += 1
        if sal > mx:
            s += mx
            mx = sal
        elif sal < mn:
            s += mn
            mn = sal
        else:
            s += sal

    return s / c

# salary = [1000,2000,3000]
# print(average(salary))

def lengthOfLongestSubstring(s: str) -> int:
    c = 0
    s_res = ''
    mx_c = 0
    for i in s:
        if i not in s_res:
            s_res += i
            c += 1
            if c > mx_c:
                mx_c = c
                mx_s = s_res
        else:
            idx = s_res.find(i)
            c -= idx
            s_res = s_res[idx+1:] + i
    return mx_c, mx_s

# s = "abcabcbb"
# print(lengthOfLongestSubstring(s))


def arraySign(nums: list[int]) -> int:
    c_odd = 0

    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            c_odd += 1
    return 1 if c_odd % 2 == 0 else -1

# nums = [-1,1,-1,1,-1]
# print(arraySign(nums))


def maxArea1(height: list[int]) -> int:
    n = len(height)
    height_l = 0
    idx_l = 0
    for i in range(len(height)-1):
        if (height[i]-height_l) - (i-idx_l) > 0:
            height_l = height[i]
            idx_l = i

    height_r = 0
    idx_r = n - 1
    for i in range(len(height)-1,idx_l,-1):
        if (height[i]-height_r) - (idx_r-i) > 0:
            height_r = height[i]
            idx_r = i

    res = min(height_l,height_r) * (idx_r-idx_l)
    for i in range(idx_l):
        if min(height[i],height_r) * (idx_r-i) > res:
            res = min(height[i],height_r) * (idx_r-i)

    for i in range(idx_r+1,n):
        if min(height_l,height[i]) * (i-idx_l) > res:
            res = min(height_l,height[i]) * (i-idx_l)

    return res


def maxArea2(height: list[int]) -> int:
    mx = -1
    idxs = []
    lng = 0
    for i in range(len(height)):
        lng += 1
        if height[i] == mx:
            idxs.append(i)
        elif height[i] > mx:
            mx = height[i]
            idxs = [i]

    res = 0
    for i in idxs:
        for l in range(i):
            if height[l] * (i - l) > res:
                res = height[l] * (i - l)
        if i <= lng - 3:
            for r in range(i+2,lng):
                if height[r] * (r - i) > res:
                    res = height[r] * (r - i)

    return res


def maxArea3(height: list[int]) -> int:
    n = len(height)

    idx_l = 0
    idx_r = n - 1
    hl = height[idx_l]
    hr = height[idx_r]

    res = min(hl, hr) * (idx_r-idx_l)
    c = 0

    while c < n-1:
        c += 1

        # when hl == hr?
        if hl > hr:
            idx_r -= 1
            hr = height[idx_r]
        elif hl <= hr:
            idx_l += 1
            hl = height[idx_l]
        # else:
        #     for k in range(1, (idx_r - idx_l)//2 + 1):
        #         if height[idx_l + k] > height[idx_r - k]:
        #             idx_l += k
        #             hl = height[idx_l]
        #             break
        #         elif height[idx_l + k] < height[idx_r - k]:
        #             idx_r -= k
        #             hr = height[idx_r]
        #             break

        if min(hl, hr) * (idx_r-idx_l) > res:
            res = min(hl, hr) * (idx_r-idx_l)

    return res

# height = [1,8,6,2,5,4,8,25,7]
# print(maxArea3(height))
#
# height = [1,2,3,4,5,6,7,8,9,10]
# print(maxArea3(height))
#


def predictPartyVictory(senate: str) -> str:
    def check(s):
        return ('R' in s) and ('D' in s)

    idx = 0
    while idx < len(senate):
        def check(s):
            return ('R' in s) and ('D' in s)

        def rep(s, sym):
            for i in range(len(s)):
                if s[i] == sym:
                    return ''.join([s[:i], s[i + 1:]])

        idx = 0
        while check(senate):
            # print(senate)
            cur = senate[idx]
            if cur == 'R':
                if 'D' in senate[idx + 1:]:
                    start = senate[:idx + 1]
                    end = rep(senate[idx + 1:], 'D')
                else:
                    start = rep(senate[:idx + 1], 'D')
                    end = senate[idx + 1:]
                senate = ''.join([start, end])

            else:
                if 'R' in senate[idx + 1:]:
                    start = senate[:idx + 1]
                    end = rep(senate[idx + 1:], 'R')
                else:
                    start = rep(senate[:idx + 1], 'R')
                    end = senate[idx + 1:]
                senate = ''.join([start, end])

            idx += 1
            if idx > len(senate) - 1:
                idx = 0

        return 'Radiant' if senate[0] == 'R' else 'Dire'

# senate = "DRRD"
# print(predictPartyVictory(senate))

def add_brackets(lis):
    new_lis = []
    lis = list(lis)
    for i in range(len(lis)):
        for j in range(len(lis[i])-1):
            if lis[i][j:j+2] == '()':
                new_lis.append(''.join([lis[i][:j],'()',lis[i][j:]]))
                new_lis.append(''.join([lis[i][:j+2], '()', lis[i][j+2:]]))
                new_lis.append(''.join([lis[i][:j], '(())', lis[i][j+2:]]))
    return set(new_lis)

def generateParenthesis(n: int) -> list[str]:
    st = set(['()'])
    for i in range(n-1):
            st = add_brackets(st)
    return st


# print(generateParenthesis(1))


def twoSum(nums: list[int], target: int) -> list[int]:
    s = set()
    for i in range(len(nums)):
        if target-nums[i] in s:
            return [nums.index(target-nums[i]), i]
        else:
            s.add(nums[i])

    return 'No solution'



def removeDuplicates(nums: list[int]) -> int:
    mx = nums[-1]
    n = len(nums)
    idx = 0
    k = 0
    while nums[idx] < mx:
        print(nums, idx)
        if nums[idx] == nums[idx-1]:
            for j in range(idx,n-k-1):
                nums[j] = nums[j+1]
            k += 1
        else:
            idx += 1
    return idx+1, nums
