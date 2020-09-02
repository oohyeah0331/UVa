class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, 0
        for i, n in enumerate(nums):
            a = target - n
            # print('i = ',i,'n = ',n)
            # print('a = ',a)
            for j, m in enumerate(nums[i+1:], start=i+1):
                # print('j = ',j,'m = ',m)
                if m == a:
                    return [i, j]
        return [i, j]


class Solution2:
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        m = {}  # val:idx
        for i in range(len(nums)):
            t = target - nums[i]
            if t in m:
                return [m[t], i]
            m[nums[i]] = i
            # print(m)
        return []


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # nums = [3, 2, 4]
    nums = [1, 3, 2, 3]
    target = 6

    print(Solution2().twoSum(nums, target))
